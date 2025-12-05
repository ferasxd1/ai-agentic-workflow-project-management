from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"

# Instantiate a KnowledgeAugmentedPromptAgent
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

# Get response from the agent
knowledge_agent_response = knowledge_agent.respond(prompt)

# Print the response
print("Knowledge Augmented Agent Response:")
print(knowledge_agent_response)

# Demonstration of knowledge usage:
print("\nKnowledge Source Confirmation:")
print("The agent uses ONLY the provided knowledge (that the capital of France is London) rather than")
print("the model's inherent knowledge (that the capital is actually Paris). This demonstrates how")
print("the KnowledgeAugmentedPromptAgent can be constrained to use specific, provided information.")
