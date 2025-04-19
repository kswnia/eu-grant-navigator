import json
import os


def build_prompt(query, json_path, limit=5):
    # Make JSON path absolute
    abs_path = os.path.join(os.path.dirname(__file__), '..', json_path)

    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"Missing JSON file: {abs_path}")

    with open(abs_path, 'r', encoding='utf-8') as f:
        chunks = json.load(f)

    # Filter relevant chunks (basic match — upgrade to vector search later)
    query_lower = query.lower()
    query_words = query_lower.split()
    relevant = [
        c for c in chunks
        if any(word in c.get('content', '').lower() or word in c.get('section', '').lower() for word in query_words)
    ]

    # Limit top-N results
    context_blocks = relevant[:limit]
    print(f"[DEBUG] Found {len(context_blocks)} relevant chunks for query: '{query}'")

    # Build Markdown-style context with real URL links
    context = "\n\n".join(
        f"**{c.get('section', 'No Section')}** "
        f"([🔗 source]({c.get('source', '#')})):\n"
        f"{c.get('content', 'No content')}"
        for c in context_blocks
    )
    if not context_blocks:
        return f"""No relevant information found in the source documents for your question: {query}"""

    # Full prompt to send to the LLM
    return f"""You are an expert advisor on EU grants.

    Use ONLY the following CONTEXT to answer the QUESTION. For each part of your answer, cite the specific [source link] when relevant.

    ### CONTEXT:
    {context}

    ### QUESTION:
    {query}

    ### ANSWER (include sources inline, like [source](URL)):
    """


# Example usage
if __name__ == "__main__":
    query = input("Ask your question about EU grants: ")
    prompt = build_prompt(query, "data/processed_chunks/your_file.json")
    print("\n--- Prompt to LLM ---\n")
    print(prompt)
    print(f"[DEBUG] Query words: {query_words}")
    print(f"[DEBUG] Matched chunks: {len(relevant)}")

