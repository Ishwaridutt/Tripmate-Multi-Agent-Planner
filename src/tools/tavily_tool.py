from tavily import TavilyClient
# import os
# from dotenv import load_dotenv
from config.config import TAVILY_API_KEY

# load_dotenv()



client = TavilyClient(
    # api_key= os.getenv("TAVILY_API_KEY")
    api_key= TAVILY_API_KEY
)


def tavily_search(query, k=5):
    '''
    uses the tavily api to fetch results againts user query and then iterate those
    to extract the required data
    '''
    response = client.search(
        query= query,
        max_results= k
    )

    results = []

    for index, result in enumerate(response["results"], 1):
        title   = result.get("title", "Unknown")
        url     = result.get("url", "")
        snippet = result.get("content", "").strip()
        # Keep only the first 300 characters to avoid wall-of-text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{index}. **{title}**\n   {url}\n   {snippet}")

    print(f'\nTavily tool query: {query} and result: ', results)

    return "\n\n".join(results)

