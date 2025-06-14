# Simple AI Agent with OpenRouter

A simple Python AI agent that uses OpenRouter API to interact with various AI models.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   OPENROUTER_API_URL=https://api.openrouter.ai/v1
   ```

## Usage

### Basic Usage

```python
from main import SimpleAIAgent

# Create agent
agent = SimpleAIAgent()

# Simple chat
response = agent.chat("Hello! How are you?")
print(response)
```

### Chat with Different Models

```python
# Use different models
response = agent.chat("Write a poem", model="anthropic/claude-3-haiku")
response = agent.chat("Explain quantum physics", model="deepseek/deepseek-chat")
```

### Conversation with History

```python
conversation = [
    {"role": "user", "content": "My name is John"},
    {"role": "assistant", "content": "Nice to meet you, John!"},
    {"role": "user", "content": "What's my name?"}
]

response = agent.chat_with_history(conversation)
# Will remember your name is John
```

## Running Examples

- **Interactive chat:** `python main.py`
- **Example scripts:** `python examples.py`

## Available Models

Popular models available through OpenRouter:
- `deepseek/deepseek-chat` - Fast and capable
- `anthropic/claude-3-haiku` - Anthropic's fast model
- `meta-llama/llama-3.1-8b-instruct` - Meta's Llama model
- `openai/gpt-4o-mini` - OpenAI's efficient model

## Features

- ✅ Simple and clean API
- ✅ Support for multiple AI models
- ✅ Conversation history support
- ✅ Error handling
- ✅ Interactive chat mode
- ✅ Easy to extend and customize

## Error Handling

The agent includes built-in error handling. If something goes wrong, it will return an error message instead of crashing.

## Customization

You can easily extend the `SimpleAIAgent` class to add more features like:
- Custom system prompts
- Token counting
- Response streaming
- Custom headers
- Rate limiting