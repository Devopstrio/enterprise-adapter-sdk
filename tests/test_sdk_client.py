from sdk.client import EnterpriseAdapterSDK

def test_sdk_client_sap():
    sdk = EnterpriseAdapterSDK()
    res = sdk.execute_and_translate("sap", {"sap_host": "sap-prod.internal"}, "99482")
    assert res["status"] == "SUCCESS"
    assert res["canonical_payload"]["protocol"] == "SAP_ODATA_V2"

def test_sdk_client_servicenow():
    sdk = EnterpriseAdapterSDK()
    res = sdk.execute_and_translate("servicenow", {"instance_url": "https://sn.internal"}, "1001")
    assert res["status"] == "SUCCESS"
    assert res["canonical_payload"]["protocol"] == "SERVICENOW_REST_V1"
