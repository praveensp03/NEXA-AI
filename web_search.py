import os
from dotenv import load_dotenv
from tavily import TavilyClient
from modules.brain import ask_ai

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")
tavily = TavilyClient(api_key=api_key)


def web_search(query):
    print("WEB SEARCH FUNCTION CALLED")
    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    results = response.get("results", [])
    print("\n--TAVILY RESULTS--")
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Content: {result['content']}")
        print(f"Source: {result['url']}")
        print("--------------------")

    if not results:
        return "I couldn't find any relevant information."

    context = ""

    for result in results:
        title = result.get("title", "")
        content = result.get("content", "")
        url = result.get("url", "")

        context += f"""
Title: {title}
Content: {content}
Source: {url}

"""

    prompt = f"""
You are NEXA, a personal AI assistant.

The user asked:
{query}

Below are LIVE web search results:

{context}

Answer the user's question using the most recent and reliable
information available in these search results.

IMPORTANT:
- Prefer newer information over older information.
- If sources disagree, prefer the most recent reliable source.
- Do not blindly trust old information.
- Give ONLY the final answer.
- Keep the answer short and natural.
"""

    return ask_ai(prompt)