from main import SimpleAIAgent

# Example 1: Basic usage
def example_basic_chat():
    """Example of basic chat functionality"""
    print("=== Example 1: Basic Chat ===")
    agent = SimpleAIAgent()
    
    questions = [
        "What is Python?",
        "Write a simple hello world program",
        "Explain what APIs are in simple terms"
    ]
    
    for question in questions:
        print(f"\nQ: {question}")
        answer = agent.chat(question)
        print(f"A: {answer}")
        print("-" * 50)

# Example 2: Different models
def example_different_models():
    """Example using different models available on OpenRouter"""
    print("\n=== Example 2: Different Models ===")
    agent = SimpleAIAgent()
    
    models = [
        "deepseek/deepseek-chat",
        "anthropic/claude-3-haiku",
        "meta-llama/llama-3.1-8b-instruct"
    ]
    
    question = "Write a haiku about coding"
    
    for model in models:
        print(f"\nModel: {model}")
        print(f"Q: {question}")
        answer = agent.chat(question, model=model)
        print(f"A: {answer}")
        print("-" * 50)

# Example 3: Conversation with context
def example_conversation():
    """Example of maintaining conversation context"""
    print("\n=== Example 3: Conversation with Context ===")
    agent = SimpleAIAgent()
    
    # Build a conversation
    conversation = [
        {"role": "user", "content": "I'm learning to code. What language should I start with?"},
    ]
    
    # Get first response
    response1 = agent.chat_with_history(conversation)
    print(f"User: {conversation[0]['content']}")
    print(f"AI: {response1}")
    
    # Add to conversation
    conversation.append({"role": "assistant", "content": response1})
    conversation.append({"role": "user", "content": "What are some good resources to learn that language?"})
    
    # Get second response with context
    response2 = agent.chat_with_history(conversation)
    print(f"\nUser: What are some good resources to learn that language?")
    print(f"AI: {response2}")

if __name__ == "__main__":
    try:
        example_basic_chat()
        example_different_models()
        example_conversation()
    except Exception as e:
        print(f"Error running examples: {e}")
