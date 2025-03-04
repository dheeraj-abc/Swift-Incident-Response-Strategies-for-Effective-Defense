import time
import random

def detect_threat():
    """Simulate threat detection."""
    threats = ["Malware", "Phishing Attack", "DDoS Attack", "Unauthorized Access", "Ransomware"]
    detected_threat = random.choice(threats)
    print(f"[ALERT] Potential Threat Detected: {detected_threat}")
    return detected_threat

def triage_incident(threat):
    """Simulate incident triage."""
    severity_levels = {"Malware": "High", "Phishing Attack": "Medium", "DDoS Attack": "Critical", "Unauthorized Access": "Low", "Ransomware": "Severe"}
    severity = severity_levels.get(threat, "Unknown")
    print(f"[TRIAGE] Threat: {threat}, Severity: {severity}")
    return severity

def contain_threat(threat):
    """Simulate threat containment."""
    print(f"[CONTAINMENT] Containing the threat: {threat}...")
    time.sleep(2)
    print(f"[CONTAINMENT] Threat {threat} has been contained.")

def eradicate_threat(threat):
    """Simulate threat eradication."""
    print(f"[ERADICATION] Removing threat: {threat}...")
    time.sleep(2)
    print(f"[ERADICATION] Threat {threat} has been removed from the system.")

def recover_system():
    """Simulate system recovery."""
    print("[RECOVERY] Restoring system to normal operations...")
    time.sleep(3)
    print("[RECOVERY] System successfully restored.")

def incident_response_pipeline():
    """Execute the incident response process."""
    threat = detect_threat()
    severity = triage_incident(threat)
    contain_threat(threat)
    eradicate_threat(threat)
    recover_system()
    print("[STATUS] Incident Response Process Completed Successfully.")

# Run the simulation
incident_response_pipeline()
