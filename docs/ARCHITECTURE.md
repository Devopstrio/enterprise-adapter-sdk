# Enterprise Adapter SDK Architecture

The **Enterprise Adapter SDK** provides a multi-protocol integration layer, protocol translation matrix (JSON, XML, SOAP $\rightarrow$ Canonical JSON), enterprise token exchange engine, and abstract adapter interfaces for legacy enterprise systems (SAP, ServiceNow, Salesforce, Oracle).

![Enterprise Adapter SDK Architecture](images/architecture_diagram.jpg)

## Component Sequence Flow

```mermaid
flowchart TD
    Client[Enterprise Developer Application] -->|1. Request System Adapter| SDK[Enterprise Adapter SDK Client]
    
    subgraph SDK Core Framework
        SDK --> Registry[Adapter Factory & Base Contract]
        SDK --> Translator[Protocol Payload Translator Engine]
        SDK --> TokenExchange[OAuth2 / SAML Token Exchange Engine]
    end

    Registry --> SAPAdapter[SAP OData / RFC Adapter]
    Registry --> SNAdapter[ServiceNow REST Adapter]
    
    SAPAdapter -->|2. Authenticated RFC Query| SAPSystem[SAP S/4HANA Enterprise ERP]
    SNAdapter -->|3. Authenticated REST Query| SNSystem[ServiceNow Enterprise Instance]
```

## Core Modules

1. **Base Adapter Contract (`core/base_adapter.py`)**
   - Establishes abstract class requirements for connection handling, RPC query execution, and command writes (`connect`, `execute_query`, `send_command`).

2. **Protocol Translator Engine (`core/protocol_translator.py`)**
   - Normalizes SAP OData `ObjectID` structures and ServiceNow `sys_id` records into standardized canonical JSON objects.

3. **Enterprise Token Exchange (`core/token_exchange.py`)**
   - Handles token transformation and secure credential propagation across hybrid enterprise environments.
