from adapters.sap_adapter import SAPEnterpriseAdapter
from adapters.servicenow_adapter import ServiceNowAdapter

def test_sap_adapter():
    sap = SAPEnterpriseAdapter("sap", {"sap_host": "sap.internal"})
    assert sap.connect() is True
    cmd = sap.send_command("CREATE_PO", {"amount": 1000})
    assert cmd["status"] == "SAP_RFC_SUCCESS"

def test_servicenow_adapter():
    sn = ServiceNowAdapter("servicenow", {"instance_url": "https://sn.internal"})
    assert sn.connect() is True
    cmd = sn.send_command("CREATE_INCIDENT", {"impact": "HIGH"})
    assert cmd["status"] == "INCIDENT_CREATED"
