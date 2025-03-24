"""Unit tests for the WenAgent class."""

import unittest
from unittest.mock import patch
from src.wen_agent import WenAgent

class TestWenAgent(unittest.TestCase):
    """Test suite for WenAgent."""

    def setUp(self):
        """Set up test environment."""
        self.agent = WenAgent(api_key="test-api-key", log_level="ERROR")

    @patch("src.api_client.OpenAIClient.generate_response")
    def test_ask_success(self, mock_generate):
        """Test successful question response."""
        mock_generate.return_value = "The Dragon Boat Festival is celebrated with races."
        response = self.agent.ask("What is the Dragon Boat Festival?")
        self.assertEqual(response, "The Dragon Boat Festival is celebrated with races.")

    def test_ask_invalid_input(self):
        """Test invalid input handling."""
        with self.assertRaises(ValueError):
            self.agent.ask("")

if __name__ == "__main__":
    unittest.main()
