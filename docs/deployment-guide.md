# Developer & Integration Guide: Enterprise Adapter SDK

This guide covers SDK installation, local development setup, custom system adapter development, and Pytest test execution.

## 1. Installation

```bash
# Clone repository
git clone https://github.com/Devopstrio/enterprise-adapter-sdk.git
cd enterprise-adapter-sdk

# Install in editable developer mode
pip install -e .
```

## 2. Python SDK Usage Example

```python
from sdk.client import EnterpriseAdapterSDK

# Initialize SDK Client
sdk = EnterpriseAdapterSDK()

# Query SAP OData and automatically normalize to Canonical JSON
sap_result = sdk.execute_and_translate("sap", {"sap_host": "sap.internal"}, "99482")
print("Normalized Canonical Payload:", sap_result["canonical_payload"])
```

## 3. Running Pytest Test Suite

```bash
python -m pytest -v tests/
```
