"""Module for handling OpenAI API interactions."""

import openai
import logging
from typing import Optional

class OpenAIClient:
    """Client for interacting with the OpenAI API."""
    
    def __init__(self, api_key: str):
        """Initialize the OpenAI client."""
        self.logger = logging.getLogger(__name__)
        openai.api_key = api_key
        self.logger.info("OpenAI client initialized")

    def generate_response(self, prompt: str) -> Optional[str]:
        """Generate a response using the OpenAI API."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message["content"].strip()
        except Exception as e:
            self.logger.error(f"OpenAI API error: {e}")
            return None
