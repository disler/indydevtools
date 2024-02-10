from exa_py import Exa
from typing import Optional


def create_research(draft_title: str, seo_keywords: Optional[str]):

    # instantiate the Exa client
    exa = Exa("YOUR API KEY")

    query = draft_title if draft_title else "Research Topic"
    if seo_keywords:
        query += f" {seo_keywords}"

    # advanced search with content highlights
    results = exa.search_and_contents(query, include_highlights=True)

    print("Results:", results)

    pass


if __name__ == "__main__":
    create_research(
        "Using Apple Vision Pro to code AI Agent powered Youtube Automation Tooling (LLM Proof Of Concept)"
    )
