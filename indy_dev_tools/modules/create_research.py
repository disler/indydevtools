from exa_py import Exa
from typing import List
import os
from dotenv import load_dotenv
from indy_dev_tools.models import Research

load_dotenv()  # Load environment variables


def create_research(seo_keywords: List[str]) -> List[Research]:
    # Load the Exa API key from .env file
    exa_api_key = os.getenv("EXA_API_KEY")

    # Instantiate the Exa client with the API key from .env
    exa = Exa(exa_api_key)

    research_objects = []

    for keyword in seo_keywords:
        query = keyword if keyword else "General Research"

        # Advanced search with content highlights for each keyword
        results = exa.search_and_contents(query, highlights=True, num_results=2)

        highlights = []
        # Extract highlights from each result and append to all_highlights
        for result in results.results:
            highlights.extend(result.highlights)
            print(f"Results for {keyword}: {result.url}")
            print(f"Highlights for {keyword}: {result.highlights}")

        # Create a Research object for each keyword and its highlights
        research_obj = Research(seo_keyword=keyword, highlights=highlights)
        research_objects.append(research_obj)

    # Optionally, process or save the research_objects list here
    return research_objects


if __name__ == "__main__":
    research_list = create_research(
        ["Apple Vision Pro", "Youtube Automation Tools", "llm coding"]
    )
    for research in research_list:
        print(f"Keyword: {research.seo_keyword}, Highlights: {research.highlights}")
