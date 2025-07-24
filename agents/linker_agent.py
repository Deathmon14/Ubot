# agents/linker_agent.py
from crewai import Agent
from langchain_anthropic import ChatAnthropic
from config.settings import ANTHROPIC_API_KEY, LLM_MODEL_NAME, LLM_TEMPERATURE

class LinkerAgents:
    def __init__(self):
        # Initialize the LLM with Claude settings from config
        if ANTHROPIC_API_KEY is None or LLM_MODEL_NAME is None:
            raise ValueError("ANTHROPIC_API_KEY or LLM_MODEL_NAME not set for LinkerAgent.")
        self.llm = ChatAnthropic(
            model=LLM_MODEL_NAME,
            temperature=LLM_TEMPERATURE,
            api_key=ANTHROPIC_API_KEY
        )

    def linker_agent(self):
        return Agent(
            role='UPSC News Context Linker',
            goal='Identify and explain interconnections, patterns, and contextual links between different news articles, highlighting their significance for UPSC Civil Services Examination.',
            backstory=(
                "You are a highly analytical AI specializing in cross-referencing and contextualizing "
                "news information for UPSC aspirants. Your strength lies in finding hidden relationships "
                "between seemingly disparate articles, identifying evolving trends, and explaining "
                "how various events contribute to a broader understanding of UPSC General Studies topics. "
                "You provide valuable insights into the multi-dimensional nature of current affairs."
            ),
            tools=[], # Linking is an internal LLM task based on provided summaries/articles
            llm=self.llm,
            verbose=True,
            allow_delegation=False, # This agent performs its own linking analysis
            max_iter=3,
            memory=True
        )