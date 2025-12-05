from workflow_agents.base_agents import EvaluationAgent, KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
prompt = "What is the capital of France?"

# Parameters for the Knowledge Agent
persona_knowledge = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capitol of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_knowledge, knowledge)

# Parameters for the Evaluation Agent
persona_eval = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria = "The answer should be solely the name of a city, not a sentence."
evaluation_agent = EvaluationAgent(openai_api_key, persona_eval, evaluation_criteria, knowledge_agent, max_interactions=10)

# Evaluate the prompt and print the response from the EvaluationAgent
print("Starting Evaluation Process...")
result = evaluation_agent.evaluate(prompt)

print("\n" + "="*50)
print("FINAL EVALUATION RESULT:")
print("="*50)
print(f"Final Response: {result['final_response']}")
print(f"Evaluation: {result['evaluation']}")
print(f"Number of Iterations: {result['iterations']}")
