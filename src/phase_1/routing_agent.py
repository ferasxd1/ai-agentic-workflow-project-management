from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Define the Texas Knowledge Augmented Prompt Agent
persona_texas = "You are a college professor"
knowledge_texas = "You know everything about Texas"
texas_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_texas, knowledge_texas)

# Define the Europe Knowledge Augmented Prompt Agent
persona_europe = "You are a college professor"
knowledge_europe = "You know everything about Europe"
europe_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_europe, knowledge_europe)

# Define the Math Knowledge Augmented Prompt Agent
persona_math = "You are a college math professor"
knowledge_math = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
math_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_math, knowledge_math)

# Create routing agent with agent definitions
routing_agent = RoutingAgent(openai_api_key, [])
agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        "func": lambda x: texas_agent.respond(x)
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        "func": lambda x: europe_agent.respond(x)
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        "func": lambda x: math_agent.respond(x)
    }
]

routing_agent.agents = agents

# Test the routing agent with different prompts
print("="*60)
print("Test 1: Tell me about the history of Rome, Texas")
print("="*60)
response1 = routing_agent.route("Tell me about the history of Rome, Texas")
print(f"\nResponse: {response1}\n")

print("="*60)
print("Test 2: Tell me about the history of Rome, Italy")
print("="*60)
response2 = routing_agent.route("Tell me about the history of Rome, Italy")
print(f"\nResponse: {response2}\n")

print("="*60)
print("Test 3: One story takes 2 days, and there are 20 stories")
print("="*60)
response3 = routing_agent.route("One story takes 2 days, and there are 20 stories")
print(f"\nResponse: {response3}\n")