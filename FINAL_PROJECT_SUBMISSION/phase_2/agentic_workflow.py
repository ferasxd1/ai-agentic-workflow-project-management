# agentic_workflow.py

from workflow_agents.base_agents import ActionPlanningAgent, KnowledgeAugmentedPromptAgent, EvaluationAgent, RoutingAgent

import os
from dotenv import load_dotenv

# Load the OpenAI key into a variable called openai_api_key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# load the product spec
with open('Product-Spec-Email-Router.txt', 'r', encoding='utf-8') as f:
    product_spec = f.read()

# Instantiate all the agents

# Action Planning Agent
knowledge_action_planning = (
    "Stories are defined from a product spec by identifying a "
    "persona, an action, and a desired outcome for each story. "
    "Each story represents a specific functionality of the product "
    "described in the specification. \n"
    "Features are defined by grouping related user stories. \n"
    "Tasks are defined for each story and represent the engineering "
    "work required to develop the product. \n"
    "A development Plan for a product contains all these components"
)
# Instantiate an action_planning_agent using the 'knowledge_action_planning'
action_planning_agent = ActionPlanningAgent(openai_api_key, knowledge_action_planning)

# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product. "
    f"{product_spec}"
)
# Instantiate a product_manager_knowledge_agent using 'persona_product_manager' and the completed 'knowledge_product_manager'
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_product_manager, knowledge_product_manager)

# Product Manager - Evaluation Agent
persona_product_manager_eval = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria_product_manager = "The answer should be stories that follow the following structure: As a [type of user], I want [an action or feature] so that [benefit/value]."
product_manager_evaluation_agent = EvaluationAgent(openai_api_key, persona_product_manager_eval, evaluation_criteria_product_manager, product_manager_knowledge_agent, max_interactions=10)

# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
knowledge_program_manager = (
    "Features of a product are defined by organizing similar user stories into cohesive groups. "
    "Use the product specification below to understand the product context:\n"
    f"{product_spec}"
)
# Instantiate a program_manager_knowledge_agent using 'persona_program_manager' and 'knowledge_program_manager'
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_program_manager, knowledge_program_manager)

# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."
evaluation_criteria_program_manager = (
    "The answer should be product features that follow the following structure: "
    "Feature Name: A clear, concise title that identifies the capability\n"
    "Description: A brief explanation of what the feature does and its purpose\n"
    "Key Functionality: The specific capabilities or actions the feature provides\n"
    "User Benefit: How this feature creates value for the user"
)
program_manager_evaluation_agent = EvaluationAgent(openai_api_key, persona_program_manager_eval, evaluation_criteria_program_manager, program_manager_knowledge_agent, max_interactions=10)

# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = (
    "Development tasks are defined by identifying what needs to be built to implement each user story. "
    "Use the product specification below to understand the product context and requirements:\n"
    f"{product_spec}"
)
# Instantiate a development_engineer_knowledge_agent using 'persona_dev_engineer' and 'knowledge_dev_engineer'
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona_dev_engineer, knowledge_dev_engineer)

# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that checks the answers of other worker agents."
evaluation_criteria_dev_engineer = (
    "The answer should be tasks following this exact structure: "
    "Task ID: A unique identifier for tracking purposes\n"
    "Task Title: Brief description of the specific development work\n"
    "Related User Story: Reference to the parent user story\n"
    "Description: Detailed explanation of the technical work required\n"
    "Acceptance Criteria: Specific requirements that must be met for completion\n"
    "Estimated Effort: Time or complexity estimation\n"
    "Dependencies: Any tasks that must be completed first"
)
development_engineer_evaluation_agent = EvaluationAgent(openai_api_key, persona_dev_engineer_eval, evaluation_criteria_dev_engineer, development_engineer_knowledge_agent, max_interactions=10)


# Job function persona support functions
def product_manager_support_function(query):
    """Support function for Product Manager route"""
    response = product_manager_knowledge_agent.respond(query)
    evaluation_result = product_manager_evaluation_agent.evaluate(response)
    return evaluation_result['final_response']

def program_manager_support_function(query):
    """Support function for Program Manager route"""
    response = program_manager_knowledge_agent.respond(query)
    evaluation_result = program_manager_evaluation_agent.evaluate(response)
    return evaluation_result['final_response']

def development_engineer_support_function(query):
    """Support function for Development Engineer route"""
    response = development_engineer_knowledge_agent.respond(query)
    evaluation_result = development_engineer_evaluation_agent.evaluate(response)
    return evaluation_result['final_response']

# Routing Agent
routing_agent = RoutingAgent(openai_api_key, [])
agents = [
    {
        "name": "Product Manager",
        "description": "Responsible for defining product personas and user stories only. Does not define features or tasks. Does not group stories",
        "func": lambda x: product_manager_support_function(x)
    },
    {
        "name": "Program Manager",
        "description": "Responsible for defining product features by grouping related user stories. Does not define user stories or tasks",
        "func": lambda x: program_manager_support_function(x)
    },
    {
        "name": "Development Engineer",
        "description": "Responsible for defining development tasks for implementing user stories. Does not define user stories or features",
        "func": lambda x: development_engineer_support_function(x)
    }
]
routing_agent.agents = agents

# Run the workflow

print("\n*** Workflow execution started ***\n")
# Workflow Prompt - Updated to request complete development plan
# ****
workflow_prompt = "Create a complete development plan for the Email Router product, including user stories, features, and development tasks."
# ****
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
# Implement the workflow
workflow_steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
print(f"\nWorkflow Steps Identified:")
for i, step in enumerate(workflow_steps, 1):
    print(f"{i}. {step}")

completed_steps = []

for i, step in enumerate(workflow_steps, 1):
    print(f"\n{'='*80}")
    print(f"Executing Step {i}: {step}")
    print(f"{'='*80}")
    
    result = routing_agent.route(step)
    completed_steps.append(result)
    
    print(f"\nStep {i} Result:")
    print(result)

print(f"\n{'='*80}")
print("FINAL WORKFLOW OUTPUT - EMAIL ROUTER DEVELOPMENT PLAN")
print(f"{'='*80}")
print("\n## Complete Development Plan for Email Router Project\n")
print("This comprehensive plan includes user stories, features, and development tasks.\n")
print("="*80)

# Organize output by type
user_stories = []
features = []
tasks = []

for i, step_result in enumerate(completed_steps, 1):
    step_name = workflow_steps[i-1]
    if "stories" in step_name.lower() or "story" in step_name.lower():
        user_stories.append(step_result)
    elif "features" in step_name.lower() or "feature" in step_name.lower():
        features.append(step_result)
    elif "tasks" in step_name.lower() or "task" in step_name.lower():
        tasks.append(step_result)

# Print organized output
if user_stories:
    print("\n### 1. USER STORIES")
    print("="*80)
    for story in user_stories:
        print(story)
        print("-"*80)

if features:
    print("\n### 2. PRODUCT FEATURES")
    print("="*80)
    for feature in features:
        print(feature)
        print("-"*80)

if tasks:
    print("\n### 3. DEVELOPMENT TASKS")
    print("="*80)
    for task in tasks:
        print(task)
        print("-"*80)

print("\n" + "="*80)
print("END OF EMAIL ROUTER DEVELOPMENT PLAN")
print("="*80)