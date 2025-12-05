from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# Instantiate an object of AugmentedPromptAgent with the required parameters
augmented_agent = AugmentedPromptAgent(openai_api_key, persona)

# Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = augmented_agent.respond(prompt)

# Print the agent's response
print("Augmented Agent Response:")
print(augmented_agent_response)

# Knowledge Source and Persona Impact:
# - The agent uses the general knowledge from the GPT-3.5-turbo model to answer the question about France's capital.
# - The system prompt with the persona instruction causes the agent to format its response in a specific way,
#   starting with "Dear students," which makes the response sound like it's coming from a college professor.
#   This demonstrates how personas can shape the tone and style of the agent's output while maintaining factual accuracy.
