# main.py
import os
import sys
from dotenv import load_dotenv
from typing import List, Dict
import time # Import time module
import json # Import json for parsing agent outputs

# Load environment variables
load_dotenv()

# Add the project root to the Python path
# Ensure the current script's directory is at the very beginning of sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import necessary components
from agents.news_fetcher_agent import NewsFetcherAgents
from agents.tagger_agent import TaggerAgents
from agents.summarizer_agent import SummarizerAgents
from agents.linker_agent import LinkerAgents
from tools.search_tools import upsc_news_search_tool
from crewai import Task, Crew, Process
from config.settings import UPSC_GS_TOPICS, OUTPUT_DIR


# --- Utility Functions ---
def parse_news_result(result_string: str) -> List[Dict]:
    """
    Parses the news search tool result string into a list of dictionaries.
    Assumes each news item is clearly delineated and has Title, Source, Date, Description, URL.
    This parsing might need to be robustified based on actual search tool output format.
    """
    news_items = []
    current_item = {}
    lines = result_string.strip().split('\n')

    for line in lines:
        line = line.strip()
        if not line: # Skip empty lines
            continue
        
        # Check for numbered list start or explicit "Title:"
        if line.startswith(tuple(f"{i}. " for i in range(1, 11))) or line.startswith("Title:"): # Handles "1. ", "2. ", etc., up to 10
            if current_item: # Save previous item if exists
                news_items.append(current_item)
            current_item = {"Title": line.replace(f"{line.split('.')[0]}.", "", 1).replace("Title:", "").strip()} # Remove number and dot or "Title:"
        elif line.startswith("Source:"):
            current_item["Source"] = line.replace("Source:", "").strip()
        elif line.startswith("Date:"):
            current_item["Date"] = line.replace("Date:", "").strip()
        elif line.startswith("Description:"):
            current_item["Description"] = line.replace("Description:", "").strip()
        elif line.startswith("URL:"):
            current_item["URL"] = line.replace("URL:", "").strip()
        # Handle multi-line descriptions if they don't start with a new key
        elif current_item and "Description" in current_item and not any(line.startswith(key) for key in ["Title:", "Source:", "Date:", "URL:"] + [f"{i}. " for i in range(1,11)]):
            current_item["Description"] += " " + line.strip()

    if current_item: # Add the last item
        news_items.append(current_item)
    return news_items


def format_news_for_tagging(news_items: List[Dict]) -> str:
    """Formats parsed news items into a single string for the TaggerAgent."""
    formatted_string = ""
    for i, item in enumerate(news_items):
        formatted_string += f"Article {i+1}:\n"
        formatted_string += f"Title: {item.get('Title', 'N/A')}\n"
        formatted_string += f"Description: {item.get('Description', 'N/A')}\n"
        formatted_string += f"URL: {item.get('URL', 'N/A')}\n"
        formatted_string += "--------------------\n"
    return formatted_string

def format_news_for_summarization(news_items: List[Dict]) -> str:
    """Formats parsed news items into a single string for the SummarizerAgent."""
    formatted_string = ""
    for i, item in enumerate(news_items):
        formatted_string += f"Article {i+1} Title: {item.get('Title', 'N/A')}\n"
        formatted_string += f"Article {i+1} Content (Description): {item.get('Description', 'N/A')}\n"
        formatted_string += f"Article {i+1} Source: {item.get('Source', 'N/A')}\n"
        formatted_string += f"Article {i+1} URL: {item.get('URL', 'N/A')}\n"
        formatted_string += "---\n"
    return formatted_string

def format_summaries_for_linking(summaries_with_tags: List[Dict]) -> str:
    """Formats summaries and tags into a single string for the LinkerAgent."""
    formatted_string = "Summarized and Tagged Articles for Linking:\n"
    for i, item in enumerate(summaries_with_tags):
        formatted_string += f"Article {i+1}:\n"
        formatted_string += f"Title: {item.get('Title', 'N/A')}\n"
        formatted_string += f"Summary: {item.get('Summary', 'N/A')}\n"
        formatted_string += f"UPSC Topics: {', '.join(item.get('UPSC_Topics', ['N/A']))}\n"
        formatted_string += f"URL: {item.get('URL', 'N/A')}\n"
        formatted_string += "--------------------\n"
    return formatted_string

def save_output_to_file(filename: str, content: str):
    """Saves the given content to a file in the OUTPUT_DIR."""
    filepath = os.path.join(OUTPUT_DIR, filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Output saved to: {filepath}")
    except IOError as e:
        print(f"❌ Error saving output to file {filepath}: {e}")


# --- Test Functions ---
def test_news_fetcher_agent_initialization():
    print("Testing NewsFetcherAgent initialization...")
    try:
        agent_instance = NewsFetcherAgents()
        _ = agent_instance.news_fetcher_agent()
        print("✅ NewsFetcherAgent initialized successfully.")
        return agent_instance
    except Exception as e:
        print(f"❌ NewsFetcherAgent initialization failed: {e}")
        return None

def test_tagger_agent_initialization():
    print("Testing TaggerAgent initialization...")
    try:
        agent_instance = TaggerAgents()
        _ = agent_instance.upsc_tagger_agent()
        print("✅ TaggerAgent initialized successfully.")
        return agent_instance
    except Exception as e:
        print(f"❌ TaggerAgent initialization failed: {e}")
        return None

def test_summarizer_agent_initialization():
    print("Testing SummarizerAgent initialization...")
    try:
        agent_instance = SummarizerAgents()
        _ = agent_instance.summarizer_agent()
        print("✅ SummarizerAgent initialized successfully.")
        return agent_instance
    except Exception as e:
        print(f"❌ SummarizerAgent initialization failed: {e}")
        return None

def test_linker_agent_initialization():
    print("Testing LinkerAgent initialization...")
    try:
        agent_instance = LinkerAgents()
        _ = agent_instance.linker_agent()
        print("✅ LinkerAgent initialized successfully.")
        return agent_instance
    except Exception as e:
        print(f"❌ LinkerAgent initialization failed: {e}")
        return None


def test_tool_directly():
    print("\nTesting Serper API tool directly...")
    try:
        # This is a general query, not UPSC specific, to test tool functionality
        test_query = "latest news headlines"
        result = upsc_news_search_tool._run(query=test_query)
        if result and "No news articles found" not in result:
            print(f"✅ Serper API tool returned results for '{test_query}'. Snippet: {result[:200]}...")
            return True
        else:
            print(f"❌ Serper API tool returned no results or an error for '{test_query}'. Result: {result}")
            return False
    except Exception as e:
        print(f"❌ Error testing Serper API tool: {e}")
        return False

# --- CrewAI Pipeline ---
def run_full_news_processing_crew():
    print("\n🚀 Running Full UPSC News Processing Pipeline...")
    print("=" * 50)

    try:
        # Initialize Agents
        fetcher_agents = NewsFetcherAgents()
        tagger_agents = TaggerAgents()
        summarizer_agents = SummarizerAgents()
        linker_agents = LinkerAgents()

        fetcher_agent = fetcher_agents.news_fetcher_agent()
        tagger_agent = tagger_agents.upsc_tagger_agent()
        summarizer_agent = summarizer_agents.summarizer_agent()
        linker_agent = linker_agents.linker_agent()

        # Define Tasks
        fetch_news_task = Task(
            description=(
                "Fetch the top 5-10 latest news articles relevant to UPSC Civil Services Examination "
                "from specified Indian news sources. Focus on current events, policy updates, "
                "economic developments, international relations, and environmental news. "
                "Compile results with Title, Source, Date, Description, and URL."
            ),
            expected_output="A formatted string containing the Title, Source, Date, Description, and URL for each of the fetched news articles.",
            agent=fetcher_agent,
        )

        tag_news_task = Task(
            description=(
                "Given the raw news articles, classify each article into one or more "
                "relevant UPSC General Studies topics from the predefined list. "
                f"UPSC Topics: {UPSC_GS_TOPICS}. "
                "Return a JSON string where each item includes 'Title', 'Description', 'URL', and 'UPSC_Topics' (a list of strings)."
                "Example: [{\"Title\": \"...\", \"Description\": \"...\", \"URL\": \"...\", \"UPSC_Topics\": [\"Indian Economy\"]}]"
            ),
            expected_output="A JSON string representing a list of dictionaries, each with 'Title', 'Description', 'URL', and 'UPSC_Topics' (list of strings).",
            agent=tagger_agent,
            context=[fetch_news_task] # This task depends on the output of fetch_news_task
        )

        summarize_news_task = Task(
            description=(
                "For each news article provided, generate a concise, objective, "
                "and UPSC-relevant summary. The summary should be short, sharp, "
                "and capture the core information essential for a UPSC aspirant. "
                "Include the original title, URL, and the generated summary for each article."
                "Return a JSON string where each item includes 'Title', 'URL', 'Summary'."
                "Example: [{\"Title\": \"...\", \"URL\": \"...\", \"Summary\": \"...\"}]"
            ),
            expected_output="A JSON string representing a list of dictionaries, each with 'Title', 'URL', and 'Summary'.",
            agent=summarizer_agent,
            context=[tag_news_task], # Summarize the content that has been tagged
            output_file=os.path.join(OUTPUT_DIR, "upsc_news_summaries.json") # Save summaries
        )

        link_news_task = Task(
            description=(
                "Analyze the provided summaries and their UPSC topics to identify "
                "interconnections, recurring themes, and patterns between different articles. "
                "Explain the significance of these links for a UPSC aspirant, connecting "
                "them to broader GS topics or recent trends. "
                "Your output should highlight specific articles and their linked concepts."
                "Format the output as a clear, readable text detailing the connections found."
            ),
            expected_output="A detailed textual explanation of inter-article links and patterns relevant to UPSC, citing specific articles where applicable.",
            agent=linker_agent,
            context=[summarize_news_task], # Link based on summaries
            output_file=os.path.join(OUTPUT_DIR, "upsc_news_links.txt") # Save links
        )


        # Instantiate Crew with a sequential process
        crew = Crew(
            agents=[fetcher_agent, tagger_agent, summarizer_agent, linker_agent],
            tasks=[fetch_news_task, tag_news_task, summarize_news_task, link_news_task],
            process=Process.sequential,
            verbose=True, # Corrected from 2 to True
            full_output=True,
            share_crew=False
        )

        print("Starting crew execution...")
        start_time = time.time()
        result = crew.kickoff()
        end_time = time.time()
        print(f"Crew execution finished in {end_time - start_time:.2f} seconds.")

        print("\n--- Crew Execution Results ---")
        print(result)

        # Process and save tagged news, summaries, and links
        if tag_news_task.output:
            try:
                tagged_news_content = tag_news_task.output.raw_output if hasattr(tag_news_task.output, 'raw_output') else tag_news_task.output
                save_output_to_file("upsc_news_tagged.json", tagged_news_content.raw_output)
            except Exception as e:
                print(f"❌ Error processing tagged news output: {e}")

        if summarize_news_task.output:
             print("\n--- Generated Summaries ---")
             print(summarize_news_task.output.raw_output if hasattr(summarize_news_task.output, 'raw_output') else summarize_news_task.output)

        if link_news_task.output:
            print("\n--- Identified Links and Patterns ---")
            print(link_news_task.output.raw_output if hasattr(link_news_task.output, 'raw_output') else link_news_task.output)


    except Exception as e:
        print(f"\n❌ An error occurred during the full news processing pipeline: {e}")
        return False
    return True


# --- Main Execution ---
def main():
    """Main function to run all tests or the full pipeline."""
    print("🧪 Starting UPSC News Assistant Component Tests")
    print("=" * 50)
    
    # Check environment variables
    required_vars = ['ANTHROPIC_API_KEY', 'SERPER_API_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
        print("Please set these in your .env file")
        return
    
    # Test 1: NewsFetcherAgent initialization
    fetcher_agent = test_news_fetcher_agent_initialization()
    if not fetcher_agent:
        return
    
    # Test 2: TaggerAgent initialization
    tagger_agent = test_tagger_agent_initialization()
    if not tagger_agent:
        return
    
    # Test 3: SummarizerAgent initialization
    summarizer_agent = test_summarizer_agent_initialization()
    if not summarizer_agent:
        return

    # Test 4: LinkerAgent initialization
    linker_agent = test_linker_agent_initialization()
    if not linker_agent:
        return

    # Test 5: Tool functionality (Serper API)
    tool_works = test_tool_directly()
    if not tool_works:
        print("⚠️  Serper tool test failed. News fetching might not work correctly.")
    
    # Test 6: Run the full news processing pipeline
    print("\nDo you want to run the full news processing pipeline (fetch, tag, summarize, link)? This will make API calls. (y/n): ", end="")
    user_input = input().strip().lower()
    
    if user_input == 'y':
        run_full_news_processing_crew()
    else:
        print("✅ All basic tests completed without running the full pipeline.")

if __name__ == "__main__":
    main()