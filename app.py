import os
import json
import boto3
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.gemini import GeminiModel

# Load environment variables from .env file
load_dotenv()

# Ensure the Gemini model picks up the API key from environment variables
os.environ["GEMINI_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Initialize SNS client for alerts
sns_client = boto3.client('sns', region_name=os.getenv("AWS_REGION", "eu-north-1"))
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")

@tool
def evaluate_multimodal_hazards(temperature_c: float, visibility_m: float) -> str:
    """Evaluates telemetry risks and returns hazard status."""
    severity = "LOW"
    if temperature_c > 45.0 or visibility_m < 150:
        severity = "CRITICAL"
    elif temperature_c > 38.0 or visibility_m < 500:
        severity = "HIGH"

    alerts = []
    if temperature_c > 40.0:
        alerts.append("HEAT_WARNING")
    if visibility_m < 300.0:
        alerts.append("POOR_VISIBILITY")

    return json.dumps({
        "telemetry_metrics": {"temperature_c": temperature_c, "visibility_m": visibility_m},
        "hazard_severity": severity,
        "hazard_alerts": alerts
    })

@tool
def send_emergency_sns_alert(severity: str, hazard_summary: str, location_id: str = "Zone-A") -> str:
    """Dispatches emergency alerts via SNS when hazard severity is CRITICAL."""
    if severity.upper() != "CRITICAL":
        return json.dumps({"status": "SKIPPED", "reason": "Severity is not CRITICAL."})

    try:
        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"🚨 AEGISAGENT ALERT: CRITICAL Hazard in {location_id}",
            Message=f"CRITICAL HAZARD DETECTED\nLocation: {location_id}\nFindings: {hazard_summary}"
        )
        return json.dumps({"status": "DISPATCHED", "message_id": response['MessageId']})
    except Exception as e:
        return json.dumps({"status": "FAILED", "error": str(e)})

# Initialize Strands Agent using corrected GeminiModel parameters
agent = Agent(
    model=GeminiModel(model_id="gemini-2.5-flash"),
    tools=[evaluate_multimodal_hazards, send_emergency_sns_alert],
    system_prompt=(
        "You are AegisAgent. Always run `evaluate_multimodal_hazards` first. "
        "If and ONLY if severity is CRITICAL, immediately call `send_emergency_sns_alert`."
    )
)

if __name__ == "__main__":
    print("\n--- Running Background Agent with Gemini in VS Code ---\n")
    response = agent("Evaluate current sector conditions with temp 48C and visibility 100m.")
    print("Agent Execution Result:")
    print(response)