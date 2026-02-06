from agent import LANGUAGE_MODEL, MODEL, ROLE

def generate_response(retriev, user_input, docs):
    retriev.similarity_search(user_input)
    context = "\n\n".join(d.page_content for d in docs)
    response = MODEL.chat.completions.create(
        model=LANGUAGE_MODEL,
        messages=[
            {"role": "system", "content": ROLE},
            {"role": "user", "content": f"CONTEXTE:\n{context}\n\nQUESTION:\n{user_input}"}
        ]
    )
    return response.choices[0].message.content
