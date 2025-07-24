# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# --- LLM Configuration ---
LLM_MODEL_NAME = "claude-3-5-sonnet-20240620" # Or "claude-3-haiku-20240307" for a faster, cheaper option
LLM_TEMPERATURE = 0.2 # Lower temperature for more factual/less creative output

# Add any other global configurations here
NEWS_SOURCES = [
    "The Hindu",
    "The Indian Express",
    "Press Information Bureau (PIB)",
    "Business Standard",
    "The Economic Times"
]

# --- UPSC Specific Configuration ---
UPSC_GS_TOPICS = [
    "Indian Economy (Growth, Development, Employment, Inclusive Growth, Government Budgeting, Major Crops, Food Processing, Land Reforms, Liberalization, Infrastructure, Investment Models)",
    "Indian Polity & Governance (Constitution, Political System, Panchayati Raj, Public Policy, Rights Issues, Regulatory Bodies, Welfare Schemes)",
    "International Relations (India and its neighborhood, Bilateral/Regional/Global groupings, International Institutions, Important International events)",
    "Science & Technology (Developments and their applications & effects in everyday life, IT, Space, Computers, Robotics, Nanotechnology, Biotechnology, Intellectual Property Rights)",
    "Environment & Ecology (Biodiversity, Climate Change, Environmental Impact Assessment, Conservation, Pollution)",
    "Geography (Physical Geography, Indian Geography, World Geography, Human Geography, Resources)",
    "History & Culture (Ancient, Medieval, Modern Indian History, Art & Culture, Post-independence consolidation)",
    "Social Issues & Justice (Poverty, Hunger, Health, Education, Human Development, Vulnerable Sections, Role of NGOs)",
    "Internal Security & Disaster Management (Linkages between development and spread of extremism, Role of external state/non-state actors, Cyber security, Border areas, Organized crime, Disaster Management)",
    "Ethics, Integrity, and Aptitude (Not directly news-based, but current events can provide case studies)"
]

OUTPUT_DIR = "output" # Directory to save processed news
os.makedirs(OUTPUT_DIR, exist_ok=True) # Create output directory if it doesn't exist