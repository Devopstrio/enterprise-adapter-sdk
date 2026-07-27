from typing import Dict, Any, List, Optional, Union

class ProtocolTranslator:
    """
    JSON / XML / SOAP Protocol Payload Translator Engine.
    Translates legacy enterprise payloads into unified REST/JSON structures.
    """

    def translate_to_canonical(self, source_protocol: str, raw_payload: Dict[str, Any]) -> Dict[str, Any]:
        source = source_protocol.lower()
        if source == "sap_odata":
            return {
                "canonical_id": raw_payload.get("ObjectID", "unk"),
                "entity": "MaterialMaster",
                "attributes": raw_payload.get("d", {}),
                "protocol": "SAP_ODATA_V2"
            }
        elif source == "servicenow_rest":
            return {
                "canonical_id": raw_payload.get("sys_id", "unk"),
                "entity": "IncidentTicket",
                "attributes": raw_payload.get("result", {}),
                "protocol": "SERVICENOW_REST_V1"
            }
        return {
            "canonical_id": raw_payload.get("id", "unk"),
            "entity": "GenericEnterpriseEntity",
            "attributes": raw_payload,
            "protocol": source_protocol.upper()
        }
