# tools/search_tools.py
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class NewsSearchInput(BaseModel):
    """Input schema for NewsSearchTool."""
    query: str = Field(..., description="Search query for news articles")
    country: str = Field(default="in", description="Country code for news search (default: 'in' for India)")
    language: str = Field(default="en", description="Language code for news search (default: 'en' for English)")

class NewsSearchTool(BaseTool):
    name: str = "UPSC_News_Search"
    description: str = (
        "Search for current news articles relevant to UPSC Civil Services Examination. "
        "This tool searches for news from reputable Indian news sources and returns "
        "relevant articles with titles, descriptions, URLs, and publication dates."
    )
    args_schema: Type[BaseModel] = NewsSearchInput

    def _run(self, query: str, country: str = "in", language: str = "en") -> str:
        """
        Search for news articles using Serper API.
        
        Args:
            query: Search query for news articles
            country: Country code (default: "in" for India)
            language: Language code (default: "en" for English)
            
        Returns:
            Formatted string with news articles information
        """
        try:
            # Get API key from environment
            serper_api_key = os.getenv('SERPER_API_KEY')
            if not serper_api_key:
                return "Error: SERPER_API_KEY not found in environment variables."

            # Serper News API endpoint
            url = "https://google.serper.dev/news"
            
            # Headers for the request
            headers = {
                'X-API-KEY': serper_api_key,
                'Content-Type': 'application/json'
            }
            
            # Payload for the request
            payload = {
                'q': query,
                'gl': country,  # Geographic location
                'hl': language,  # Language
                'num': 10  # Number of results
            }
            
            # Make the API request
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            
            if response.status_code == 200:
                data = response.json()
                return self._format_news_results(data)
            else:
                return f"Error: API request failed with status code {response.status_code}"
                
        except Exception as e:
            return f"Error occurred while searching for news: {str(e)}"

    def _format_news_results(self, data: dict) -> str:
        """
        Format the news search results into a readable string.
        
        Args:
            data: Raw API response data
            
        Returns:
            Formatted string with news articles
        """
        if 'news' not in data or not data['news']:
            return "No news articles found for the given query."
        
        formatted_results = "UPSC Relevant News Articles:\n" + "="*50 + "\n\n"
        
        for i, article in enumerate(data['news'][:10], 1):
            title = article.get('title', 'No title available')
            snippet = article.get('snippet', 'No description available')
            link = article.get('link', 'No URL available')
            date = article.get('date', 'Date not available')
            source = article.get('source', 'Source not available')
            
            formatted_results += f"{i}. {title}\n"
            formatted_results += f"   Source: {source}\n"
            formatted_results += f"   Date: {date}\n"
            formatted_results += f"   Description: {snippet}\n"
            formatted_results += f"   URL: {link}\n"
            formatted_results += "-" * 50 + "\n\n"
        
        return formatted_results

# Create an instance of the tool to be used by agents
upsc_news_search_tool = NewsSearchTool()