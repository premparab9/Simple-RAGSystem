import os
from openai import OpenAI

def get_qa_chain(retriever):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL")
    )

    model = os.getenv("OPENAI_MODEL")

    def ask(query: str):
        docs = retriever.invoke(query)
        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
Use the context to answer the question.

Context:
{context}

Question:
{query}
"""

        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )

        return resp.choices[0].message.content

    return ask