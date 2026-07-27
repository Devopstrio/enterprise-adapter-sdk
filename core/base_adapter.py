from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional, Union

class BaseEnterpriseAdapter(ABC):
    """
    Abstract Enterprise Protocol Adapter Contract.
    All system adapters (SAP, ServiceNow, Salesforce, Oracle) implement this interface.
    """

    def __init__(self, system_name: str, connection_params: Dict[str, Any]):
        self.system_name = system_name
        self.connection_params = connection_params

    @abstractmethod
    def connect(self) -> bool:
        """Establish session or token handshake with target enterprise system."""
        pass

    @abstractmethod
    def execute_query(self, query_id: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute structured query or remote function call."""
        pass

    @abstractmethod
    def send_command(self, action: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Send command or write payload to target enterprise system."""
        pass
