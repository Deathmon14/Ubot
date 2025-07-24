# agents/tagger_agent.py
from crewai import Agent
from langchain_anthropic import ChatAnthropic
from config.settings import ANTHROPIC_API_KEY, LLM_MODEL_NAME, LLM_TEMPERATURE, UPSC_GS_TOPICS

class TaggerAgents:
    def __init__(self):
        self.llm = ChatAnthropic(
            model=LLM_MODEL_NAME,
            temperature=LLM_TEMPERATURE,
            api_key=ANTHROPIC_API_KEY
        )

    def upsc_tagger_agent(self):
        return Agent(
            role='UPSC Topic Classifier',
            goal='Accurately classify news articles into relevant UPSC General Studies topics based on their content.',
            backstory=(
                "You are an AI expert in the UPSC Civil Services Examination syllabus. "
                "Your task is to read news content and precisely assign one or more "
                "of the predefined UPSC General Studies topics to it. You are meticulous "
                "and ensure that every classification is highly relevant and comprehensive. "
                "You understand the nuances of each GS topic and how current events relate to them."
            ),
            # This agent doesn't need external tools; its "tool" is its internal knowledge of UPSC topics
            tools=[],
            llm=self.llm,
            verbose=True,
            allow_delegation=False, # This agent performs its own classification
            max_iter=3,
            memory=True
        )

# We won't add an additional agent here unless we need another type of tagger.