import re
from typing import Tuple, Dict

# Define risk levels
RISK_SAFE = "SAFE"
RISK_MEDIUM = "MEDIUM"
RISK_HIGH = "HIGH"
RISK_BLOCKED = "BLOCKED"

class GuardrailSystem:
    def __init__(self):
        # Patterns for academic dishonesty
        self.dishonesty_patterns = [
            r"(?i)\b(solve|answer|solution|do my)\b.*\b(assignment|homework|exam|quiz)\b",
            r"(?i)\bwrite.*code for me\b",
            r"(?i)\bgive me the answer\b"
        ]
        
        # Patterns for prompt injection
        self.injection_patterns = [
            r"(?i)ignore (all )?previous instructions",
            r"(?i)you are now",
            r"(?i)system prompt",
            r"(?i)bypass"
        ]

    def check_input(self, query: str) -> Tuple[str, str]:
        """
        Checks the user input against known malicious patterns.
        Returns a tuple: (Risk Level, Status Message)
        """
        # 1. Check for prompt injection (highest risk)
        for pattern in self.injection_patterns:
            if re.search(pattern, query):
                return RISK_BLOCKED, "Prompt injection attempt detected. Query blocked."

        # 2. Check for academic dishonesty
        for pattern in self.dishonesty_patterns:
            if re.search(pattern, query):
                return RISK_HIGH, "Academic dishonesty attempt detected. Switching to guided hint mode."

        # 3. Default safe
        return RISK_SAFE, "Input looks safe."

    def check_output(self, generated_response: str) -> Tuple[str, str, str]:
        """
        Checks the generated AI response to ensure it doesn't leak direct answers.
        Returns: (Risk Level, Status Message, Filtered Response)
        """
        # Very simple heuristic for MVP: If the output contains large blocks of code
        # when we expected hints, we might flag it. 
        # For this MVP, we will rely on the agent's system prompt mostly, but we can do a simple check.
        
        # E.g., if response is literally just code with no explanation
        code_block_count = generated_response.count("```")
        if code_block_count >= 2 and len(generated_response) < 200:
            return RISK_MEDIUM, "Output might contain direct code solution.", "Here is a hint instead: Try to review the concepts of loops and conditionals before writing the code."
            
        return RISK_SAFE, "Output looks safe.", generated_response

guardrails = GuardrailSystem()
