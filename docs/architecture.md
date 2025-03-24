# WEN Agent Architecture

## Overview
WEN Agent is designed with a modular, scalable architecture to deliver cultural insights efficiently. The system is built in Python, leveraging OpenAI's GPT models for natural language processing.

## Components
1. **WenAgent**: Core class orchestrating the agent's functionality.
2. **OpenAIClient**: Handles API calls to OpenAI for response generation.
3. **CultureProcessor**: Manages cultural data and context extraction.
4. **Utils**: Provides helper functions like input validation.

## Flow
1. User inputs a question.
2. `WenAgent` validates the input via `utils`.
3. `CultureProcessor` provides context.
4. `OpenAIClient` generates a response.
5. Response is returned to the user.

## Future Enhancements
- Real-time data integration.
- Multi-language support.
- GUI frontend.

![Architecture Diagram](https://via.placeholder.com/600x300.png?text=WEN+Agent+Architecture)
