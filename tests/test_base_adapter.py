from adapters.sap_adapter import SAPEnterpriseAdapter

def test_base_adapter_interface():
    adapter = SAPEnterpriseAdapter("sap", {"sap_host": "localhost"})
    assert adapter.connect() is True
    res = adapter.execute_query("123", {})
    assert res["status_code"] == 200
    assert "data" in res
