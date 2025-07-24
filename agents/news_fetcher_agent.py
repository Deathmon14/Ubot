# agents/news_fetcher_agent.py
from crewai import Agent
from langchain_anthropic import ChatAnthropic
from config.settings import ANTHROPIC_API_KEY, LLM_MODEL_NAME, LLM_TEMPERATURE
from tools.search_tools import upsc_news_search_tool # Updated import

class NewsFetcherAgents:
    def __init__(self):
        # Initialize the LLM with Claude settings from config
        self.llm = ChatAnthropic(
            model=LLM_MODEL_NAME,
            temperature=LLM_TEMPERATURE,
            api_key=ANTHROPIC_API_KEY
        )

    def news_fetcher_agent(self):
        return Agent(
            role='UPSC News Fetcher',
            goal='Identify and fetch daily news articles highly relevant to the UPSC Civil Services Examination syllabus from reputable Indian news sources and government publications.',
            backstory=(
                "You are an expert news analyst with a deep understanding of the UPSC syllabus. "
                "Your primary objective is to find current affairs articles that could be directly "
                "useful for a UPSC aspirant, avoiding irrelevant or sensational content. "
                "You prioritize quality, relevance, and accuracy, leveraging advanced search capabilities. "
                "You focus on topics like governance, economy, environment, science & technology, "
                "international relations, history, geography, and social issues that are crucial for UPSC preparation."
            ),
            tools=[upsc_news_search_tool], # Use the CrewAI-compatible tool
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            max_iter=3, # Limit iterations to prevent infinite loops
            memory=True # Enable memory for better context retention
        )