"""Module for processing and providing cultural context."""

import logging
from typing import Dict

class CultureProcessor:
    """Processor for Chinese culture data."""
    
    def __init__(self):
        """Initialize the culture processor with mock data."""
        self.logger = logging.getLogger(__name__)
        self.culture_db: Dict[str, str] = {
            "dragon boat festival": "The Dragon Boat Festival commemorates Qu Yuan with rice dumplings and boat races.",
            "chinese new year": "Chinese New Year marks the lunar new year with family reunions and red envelopes."
        }
        self.logger.info("Culture processor initialized with mock data")

    def get_context(self, question: str) -> str:
        """Retrieve cultural context based on the question."""
        question_lower = question.lower()
        for key, value in self.culture_db.items():
            if key in question_lower:
                return value
        return "General inquiry about Chinese culture."
