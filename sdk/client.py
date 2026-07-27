from typing import Dict, Any, List, Optional, Union
from core.protocol_translator import ProtocolTranslator
from core.token_exchange import EnterpriseTokenExchange
from adapters.sap_adapter import SAPEnterpriseAdapter
from adapters.servicenow_adapter import ServiceNowAdapter

class EnterpriseAdapterSDK:
    """
    Unified Developer SDK Client for Enterprise System Adapters.
    """

    def __init__(self):
        self.translator = ProtocolTranslator()
        self.token_exchange = EnterpriseTokenExchange()

    def get_adapter(self, system_name: str, connection_params: Dict[str, Any]):
        sys_lower = system_name.lower()
        if sys_lower == "sap":
            return SAPEnterpriseAdapter("sap", connection_params)
        elif sys_lower == "servicenow":
            return ServiceNowAdapter("servicenow", connection_params)
        else:
            raise ValueError(f"Unsupported enterprise system '{system_name}'.")

    def execute_and_translate(self, system_name: str, connection_params: Dict[str, Any], query_id: str) -> Dict[str, Any]:
        adapter = self.get_adapter(system_name, connection_params)
        if not adapter.connect():
            raise RuntimeError(f"Failed to connect to system {system_name}")

        raw_result = adapter.execute_query(query_id, {})
        canonical = self.translator.translate_to_canonical(
            source_protocol=raw_result.get("adapter", "generic"),
            raw_payload=raw_result.get("data", {})
        )

        return {
            "system": system_name,
            "raw_response": raw_result,
            "canonical_payload": canonical,
            "status": "SUCCESS"
        }
