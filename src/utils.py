"""Utility functions for the WEN Agent."""

import logging

def validate_input(question: str) -> None:
    """Validate user input."""
    logger = logging.getLogger(__name__)
    if not isinstance(question, str) or not question.strip():
        logger.error("Invalid input: Question must be a non-empty string")
        raise ValueError("Question must be a non-empty string")
    logger.debug(f"Validated input: {question}")
