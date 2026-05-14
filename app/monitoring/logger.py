import json
import os
from datetime import datetime
from typing import Dict, Any

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'logs')

class InteractionLogger:
    def __init__(self, log_file: str = "interaction_log.json"):
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        self.log_path = os.path.join(LOG_DIR, log_file)

    def log_interaction(self, query: str, agent_name: str, response: str, risk_level: str, response_time_ms: float, guardrail_status: str):
        """
        Logs a single interaction to a JSON lines file.
        """
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "query": query,
            "selected_agent": agent_name,
            "response_length": len(response),
            "risk_level": risk_level,
            "guardrail_status": guardrail_status,
            "response_time_ms": response_time_ms
        }

        try:
            with open(self.log_path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(log_entry) + "\n")
        except Exception as e:
            print(f"Failed to write log: {e}")

# Global logger instance
interaction_logger = InteractionLogger()
