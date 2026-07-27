from sdk.client import EnterpriseAdapterSDK

def run_integration_example():
    sdk = EnterpriseAdapterSDK()

    # SAP OData integration
    print("--- Executing SAP Enterprise Adapter ---")
    sap_res = sdk.execute_and_translate("sap", {"sap_host": "sap-prod.internal"}, "99482")
    print("SAP Result:", sap_res)

    # ServiceNow integration
    print("--- Executing ServiceNow Enterprise Adapter ---")
    sn_res = sdk.execute_and_translate("servicenow", {"instance_url": "https://devopstrio.service-now.com"}, "1001")
    print("ServiceNow Result:", sn_res)

if __name__ == "__main__":
    run_integration_example()
