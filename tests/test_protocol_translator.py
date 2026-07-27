from core.protocol_translator import ProtocolTranslator

def test_sap_translation():
    translator = ProtocolTranslator()
    raw = {"ObjectID": "MAT-99", "d": {"Name": "Gear"}}
    res = translator.translate_to_canonical("sap_odata", raw)
    assert res["protocol"] == "SAP_ODATA_V2"
    assert res["canonical_id"] == "MAT-99"

def test_servicenow_translation():
    translator = ProtocolTranslator()
    raw = {"sys_id": "INC-001", "result": {"priority": "1"}}
    res = translator.translate_to_canonical("servicenow_rest", raw)
    assert res["protocol"] == "SERVICENOW_REST_V1"
    assert res["canonical_id"] == "INC-001"
