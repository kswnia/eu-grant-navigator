def clean_chunks(chunks):
    cleaned = []
    for chunk in chunks:
        if len(chunk["content"].strip()) > 50:
            cleaned.append(chunk)
    return cleaned
