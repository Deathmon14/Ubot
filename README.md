Project Overview: UPSC AI News Assistant
🧠 Objective
To build an intelligent assistant that automates daily news analysis for UPSC aspirants and civil service researchers by:

Extracting relevant news articles

Classifying them based on UPSC subjects (Polity, Economy, Environment, etc.)

Summarizing the content using LLMs

Linking related articles, schemes, or policies across time

This system reduces the burden of manually sorting newspapers or current affairs materials, providing customized, digestible, and traceable updates.

🧱 Architecture Components
1. News Collector
Input: URLs, PDFs, or RSS feeds from sources like PIB, The Hindu, Indian Express, Yojana, etc.

Processing: Cleans HTML, extracts titles, timestamps, and content.

Output: Structured raw article JSONs (title, body, tags)

Tools used: newspaper3k, BeautifulSoup, feedparser, custom scrapers

2. Classifier Agent (LLM + Rule-based Hybrid)
Classifies each news article into UPSC categories such as:

Polity & Governance

Economy

Environment & Ecology

International Relations

Science & Tech

Social Issues

Uses LangChain + LLMChain to generate classification based on:

Custom system prompts

Keyword matching + Named Entity Recognition fallback (NER)

Agents powered by Gemini or local LLM like Mistral/LLama2 using FAISS retrieval context.

3. Summarizer Agent
Takes long-form articles and creates 3–5 line concise summaries.

Ensures factual tone, UPSC-style phrasing, no hallucinations.

Summarization prompt examples:

"Summarize in 3 lines for a civil services aspirant"

"Avoid opinions or emotional language"

Models: Gemini Pro, Mistral (via Transformers + HuggingFace), OpenRouter optional fallback

4. Interlinker Agent
Scans vector embeddings of past articles to find connections like:

“New GST Reform” and “Previous GST Council Meeting”

“Clean Ganga Mission” and “Namami Gange Budget”

Uses FAISS for nearest neighbor search

Outputs: See Also section per article

