"""Prompt injection detection for web content."""

import re
from typing import Dict, List, Tuple


class PromptInjectionDetector:
    """
    Detects potential prompt injection attempts in web content.

    Common patterns:
    - Hidden instructions to AI systems
    - Role-playing attempts
    - Instruction override attempts
    - Data exfiltration patterns
    """

    PATTERNS = [
        # Direct instruction attempts
        (r"ignore\s+(all\s+)?previous\s+instructions", "instruction_override"),
        (r"disregard\s+(all\s+)?prior", "instruction_override"),
        (r"forget\s+everything", "instruction_override"),
        (r"you\s+are\s+now\s+(a|an|the)", "role_hijack"),
        (r"act\s+as\s+if\s+you", "role_hijack"),
        (r"pretend\s+you\s+are", "role_hijack"),
        # System prompt injection
        (r"system\s*:\s*you\s+are", "system_injection"),
        (r"<\|system\|>", "system_injection"),
        (r"\[system\]", "system_injection"),
        # Data exfiltration
        (r"send\s+(all\s+)?(data|info|details)\s+to", "exfiltration"),
        (r"upload\s+(to|your)\s+(server|api|endpoint)", "exfiltration"),
        # Encoding tricks
        (r"(base64|rot13|hex)\s*(decode|encode)", "encoding_evasion"),
        (r"\x[0-9a-f]{2}", "hex_encoding"),
    ]

    def detect(self, text: str) -> Dict[str, any]:
        """
        Analyze text for prompt injection attempts.

        Returns:
            Dict with 'is_suspicious', 'findings', and 'risk_score'
        """
        findings = []
        text_lower = text.lower()

        for pattern, category in self.PATTERNS:
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            if matches:
                findings.append({
                    "pattern": pattern,
                    "category": category,
                    "matches": matches[:3],
                })

        risk_score = min(len(findings) / 5.0, 1.0)

        return {
            "is_suspicious": len(findings) > 0,
            "findings": findings,
            "risk_score": risk_score,
            "recommendation": self._recommendation(findings, risk_score),
        }

    def _recommendation(self, findings: List[Dict], risk_score: float) -> str:
        if risk_score > 0.6:
            return "BLOCK: High confidence injection attempt. Do not process."
        elif risk_score > 0.3:
            return "WARN: Suspicious patterns found. Review manually."
        elif findings:
            return "CAUTION: Minor patterns detected. Proceed with care."
        return "CLEAN: No injection patterns detected."

    def sanitize(self, text: str) -> str:
        """Remove or neutralize potential injection content."""
        for pattern, _ in self.PATTERNS:
            text = re.sub(pattern, "[REDACTED]", text, flags=re.IGNORECASE)
        return text
