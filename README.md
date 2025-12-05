# AI-Powered Agentic Workflow for Project Management

A sophisticated multi-agent system for automated project management, demonstrated through the Email Router product specification.

## 🎯 Project Overview

This project implements a complete AI-powered agentic workflow system that:
- Uses 7 different AI agent types with specialized capabilities
- Orchestrates multi-agent collaboration for project planning
- Generates comprehensive development plans including user stories, features, and tasks
- Demonstrates advanced prompting strategies and quality assurance

## 📁 Project Structure

```
src/
├── phase_1/              # Agent Library Implementation
│   ├── workflow_agents/
│   │   └── base_agents.py    # 7 agent classes
│   ├── Test scripts (7 files)
│   └── Test outputs (6 files)
│
├── phase_2/              # Workflow Implementation
│   ├── workflow_agents/
│   │   └── base_agents.py
│   ├── agentic_workflow.py   # Main workflow orchestration
│   ├── Product-Spec-Email-Router.txt
│   └── output_phase2.txt     # Workflow results
│
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key (Vocareum)

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your API key:
```bash
# Create .env file in phase_1/ and phase_2/
echo "OPENAI_API_KEY=your-key-here" > src/phase_1/.env
echo "OPENAI_API_KEY=your-key-here" > src/phase_2/.env
```

### Running Phase 1 Tests

```bash
cd src/phase_1
python direct_prompt_agent.py
python augmented_prompt_agent.py
python knowledge_augmented_prompt_agent.py
python evaluation_agent.py
python routing_agent.py
python action_planning_agent.py
```

### Running Phase 2 Workflow

```bash
cd src/phase_2
python agentic_workflow.py
```

## 🤖 Implemented Agents

### Phase 1: Agent Library

1. **DirectPromptAgent** - Direct LLM interaction
2. **AugmentedPromptAgent** - Persona-based responses
3. **KnowledgeAugmentedPromptAgent** - Knowledge-constrained responses
4. **RAGKnowledgePromptAgent** - Retrieval-Augmented Generation
5. **EvaluationAgent** - Iterative quality refinement
6. **RoutingAgent** - Semantic routing using embeddings
7. **ActionPlanningAgent** - Step extraction from prompts

### Phase 2: Workflow Orchestration

- **Product Manager Team**: Generates user stories
- **Program Manager Team**: Defines product features
- **Development Engineer Team**: Creates engineering tasks
- **Routing System**: Intelligently routes tasks to appropriate teams
- **Quality Assurance**: Evaluation agents ensure output quality

## 📊 Features

- ✅ Complete agent library with 7 specialized agents
- ✅ Multi-agent workflow orchestration
- ✅ Semantic routing with embedding-based similarity
- ✅ Iterative quality refinement (up to 10 iterations)
- ✅ Structured output generation
- ✅ Email Router product specification integration
- ✅ Comprehensive test suite

## 🎓 Key Concepts Demonstrated

- Building reusable AI agent libraries
- Implementing diverse prompting strategies
- Orchestrating multi-agent workflows
- Quality assurance through evaluation agents
- Semantic routing with embeddings
- Dynamic action planning
- Production-ready code practices

## 📝 Technical Specifications

- **API**: Vocareum OpenAI API (`https://openai.vocareum.com/v1`)
- **Chat Model**: `gpt-3.5-turbo`
- **Embedding Model**: `text-embedding-3-large`
- **Temperature**: 0 (for consistency)

## 📖 Documentation

- **project_overview.md** - Detailed project requirements and specifications
- **src/README.md** - Complete technical documentation
- **src/phase_2/RUN_WORKFLOW_INSTRUCTIONS.txt** - Workflow execution guide

## 🎯 Expected Output

The workflow produces a comprehensive Email Router development plan:

1. **User Stories** - For Customer Support Representatives, IT Administrators, and SMEs
2. **Product Features** - Email Ingestion, Classification, Knowledge Base, Response Generation, etc.
3. **Development Tasks** - Detailed engineering tasks with IDs, descriptions, and acceptance criteria

## 📦 Project Contents

The complete project includes:
- All source code in `src/` directory
- All test scripts and outputs
- Complete documentation
- Workflow results

## 🔧 Dependencies

```
openai==1.78.1
pandas==2.2.3
python-dotenv==1.1.0
```

## 📄 License

Educational use only.

## 👤 Author

Developed as part of the AI-Powered Agentic Workflow for Project Management course.

---

**Status**: ✅ Complete and Production-Ready
