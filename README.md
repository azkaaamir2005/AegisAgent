# AegisAgent 🛡️

An autonomous infrastructure monitoring and telemetry specialist agent built for real-time cloud anomaly detection, incident response, and automated notification dispatch.

## 🚀 Overview
AegisAgent continuously analyzes system metrics and incoming log data, evaluates threat severity using advanced LLM reasoning, and dispatches critical alerts directly to cloud notification pipelines. It is containerized and optimized for deployment via AWS AgentCore.

## 🤖 Model Agnostic Design & Architecture Decoupling

A core engineering priority for **Aegis Agent** was decoupling the LLM generation tier from the underlying orchestration and governance layer. 

While core configuration logs and initial documentation refer to baseline implementations using **Google Gemini 2.5 Flash**, the system is designed to be completely model-agnostic. The deployment infrastructure on **AWS AgentCore** successfully abstracts the runtime, allowing the **Strands Agents SDK** to execute security guardrails natively across upgraded upstream endpoints—including live validation testing on next-generation architectures like **Gemini 3.6 Flash**. 

### Key Architectural Benefits:
* **Forward Compatibility:** Upgrading the underlying LLM requires zero modifications to the core Aegis governance logic.
* **Infrastructure Stability:** Model latency or version shifts do not impact the stateful agent loops managed by AWS AgentCore.
* **Deterministic Guardrails:** The security gating mechanisms intercept payloads identically, regardless of the token-generation engine version.


## Architecture

```text
       +-------------------------------------------------------+
       |                  Incoming Telemetry &                 |
       |                System Logs / Metrics                  |
       +---------------------------+---------------------------+
                                   |
                                   v
       +-------------------------------------------------------+
       |               AegisAgent (Core Python)                |
       |  - app.py entry point                                 |
       |  - Strands Framework & Agent Loop                     |
       +---------------------------+---------------------------+
                                   |
            +----------------------+----------------------+
            | (Analyze Severity &                         | (Trigger Alert)
            |  Detect Anomalies)                          |
            v                                             v
+-----------------------+                     +-----------------------+
|  Google Gemini 2.5/3.6|                     |    AWS SNS (Topic)    |
|       Flash LLM       |                     | - Automated dispatch  |
| (Reasoning & Parsing) |                     | - Notification push   |
+-----------------------+                     +-----------------------+
            ^                                             |
            |                                             v
            +-------------------+-------------------------+
                                |
                                v
               +---------------------------------+
               |    AWS AgentCore & Container    |
               |    - Docker runtime             |
               |    - Secure AWS Boto3 SDK       |
               +---------------------------------+
```

## 🛠️ Tech Stack
* **Language:** Python
* **Agent Framework:** Strands (`Agent`, `@tool`)
* **Core Intelligence Engine:** Google Gemini Flash Tier (Compatible with 2.5 Flash & Next-Gen 3.6 Flash Runtime)
* **Cloud & Infrastructure:** AWS (`boto3`, SNS), Docker, AWS AgentCore

## 📋 Hackathon Compliance & Disclosures
This project incorporates several pre-existing open-source libraries and cloud SDKs as foundational building blocks:
* **Google Gemini API / Client Libraries:** Utilized for high-speed LLM inference and telemetry reasoning.
* **AWS Boto3 SDK:** Utilized for programmatic interaction with Amazon Simple Notification Service (SNS).
* **Strands Framework:** Utilized for structuring autonomous agent loops and tool definitions.
* **Python Dotenv:** Utilized for secure local environment variable management.

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/azkaaamir2005/AegisAgent.git](https://github.com/azkaaamir2005/AegisAgent.git)
   cd AegisAgent
