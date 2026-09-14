# AegisAgent 🛡️

An autonomous infrastructure monitoring and telemetry specialist agent built for real-time cloud anomaly detection, incident response, and automated notification dispatch.

## 🚀 Overview
AegisAgent continuously analyzes system metrics and incoming log data, evaluates threat severity using advanced LLM reasoning, and dispatches critical alerts directly to cloud notification pipelines. It is containerized and optimized for deployment via AWS AgentCore.

## Architecture
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
|  Google Gemini 2.5    |                     |    AWS SNS (Topic)    |
|       Flash LLM       |                     | - Automated dispatch  |
| (Reasoning & Parsing) |                     | - Notification push   |
+-----------------------+                     +-----------------------+
            ^                                             |
            |                                             v
            +-----------------------------------+-------------------+
                                                |
                                                v
                               +---------------------------------+
                               |    AWS AgentCore & Container    |
                               |    - Docker runtime             |
                               |    - Secure AWS Boto3 SDK       |
                               +---------------------------------+


## 🛠️ Tech Stack
* **Language:** Python
* **Agent Framework:** Strands (`Agent`, `@tool`)
* **Core Intelligence:** Google Gemini 2.5 Flash
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