"""Main module for the WEN Agent, an AI-powered cultural insights platform."""

import logging
from typing import Optional
from .api_client import OpenAIClient
from .culture_data import CultureProcessor
from .utils import validate_input

class WenAgent:
    """WEN Agent class for interacting with Chinese culture insights."""
    
    def __init__(self, api_key: str, log_level: str = "INFO"):
        """Initialize the WEN Agent with an API key."""
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger(__name__)
        self.client = OpenAIClient(api_key)
        self.culture_processor = CultureProcessor()
        self.logger.info("WEN Agent initialized successfully")

    def ask(self, question: str) -> Optional[str]:
        """Ask the agent a question about Chinese culture."""
        try:
            validate_input(question)
            context = self.culture_processor.get_context(question)
            prompt = f"Provide insights on Chinese culture: {question}\nContext: {context}"
            response = self.client.generate_response(prompt)
            self.logger.info(f"Generated response for question: {question}")
            return response
        except Exception as e:
            self.logger.error(f"Error processing question: {e}")
            return None

if __name__ == "__main__":
    import os
    api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")
    agent = WenAgent(api_key)
    print(agent.ask("What is the significance of the Dragon Boat Festival?"))
