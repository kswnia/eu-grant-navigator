# 🇪🇺 EU Grant Navigator — Smart, Source-Aware EU Funding Assistant

> A next-generation, AI-powered tool for navigating EU grants with natural language, grounded answers, and clickable source links.

---

## 🎯 Why This Project Exists

Finding and understanding EU funding is **needlessly complex**. Current tools like [GrantsFinder](https://www.grantsfinder.eu/) help you filter options, but:

- ❌ Require rigid input (filters, forms)
- ❌ Don’t explain *why* you’re eligible
- ❌ Don’t guide you through policies, exceptions, or logic
- ❌ Don’t show you *where* the information came from
- ❌ Can’t be extended with your own documents or data

**EU Grant Navigator** fixes that.

---

## ✅ What It Does

- 💬 Ask any question in plain language:
  - _“Can a solo developer in Estonia get EU funding for climate projects?”_
- 📚 Finds and injects relevant context from official EU sources (docs, portals)
- 🔗 Answers include **clickable citations** to exact source URLs
- 🧠 Built to support future upgrades like **graph reasoning** and **semantic search**
- 🛠️ Works offline using local LLMs (via Ollama or LM Studio)

---

---
Installation and run
```
git clone https://github.com/yourname/eu-grant-navigator.git
cd eu-grant-navigator
```
```
# Run from project root
python -m demo.app
```
for running UI 
```
streamlit run demo/app.py
```


## 🧠 How It Works (Architecture)

```mermaid
flowchart TD

A[User inputs question] --> B[Preprocess query]
B --> C[Load preprocessed JSON chunks]

C --> D{Match relevant chunks}
D -->|Keyword match| E[Select top N chunks]
D -->|Embedding future| E

E --> F[Build context block with clickable source links]
F --> G[Construct LLM prompt]
G --> H[Send to local LLM call]

H --> I[Generate grounded answer with citations]
I --> J[Display answer to user]

J --> K{User clicks source?}
K -->|Yes| L[Open original EU URL]
K -->|No| M[Done]







