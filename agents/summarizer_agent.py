# agents/summarizer_agent.py
from crewai import Agent
from langchain_anthropic import ChatAnthropic
from config.settings import ANTHROPIC_API_KEY, LLM_MODEL_NAME, LLM_TEMPERATURE, UPSC_GS_TOPICS

class SummarizerAgents:
    def __init__(self):
        # Initialize the LLM with Claude settings from config
        self.llm = ChatAnthropic(
            model=LLM_MODEL_NAME,
            temperature=LLM_TEMPERATURE,
            api_key=ANTHROPIC_API_KEY
        )

    def summarizer_agent(self):
        return Agent(
            role='UPSC News Summarizer',
            goal='Generate concise, UPSC-relevant summaries for news articles, extracting key information for aspirants.',
            backstory=(
                "You are an AI assistant specialized in distilling complex news articles "
                "into brief, impactful summaries tailored for UPSC Civil Services Examination preparation. "
                "You focus on objectivity, accuracy, and highlighting facts that are crucial "
                "from an examination perspective. You ensure summaries are to the point, "
                "avoiding jargon where simpler language suffices, and maintaining the core message."
            ),
            tools=[], # This agent does not require external tools for summarization itself
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            max_iter=3,
            memory=True
        )