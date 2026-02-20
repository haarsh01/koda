# Koda — A Simple, Explainable RAG System

Koda is a **Retrieval-Augmented Generation (RAG)** application , think of it as a focused version of ChatGPT that **answers questions using only your documents**, not the internet or hallucinations.

Instead of guessing answers, Koda:

1. **Searches your documents**
2. **Finds the most relevant parts**
3. **Uses an LLM to answer based only on that information**

This repo is built to be **simple, transparent, and educational** — no heavy frameworks, no hidden magic.

## ✨ Why Koda?

Most RAG tutorials jump straight into complex frameworks and abstractions.

Koda is different:

- ✅ Step-by-step, readable code
- ✅ Minimal dependencies
- ✅ Easy to debug and extend
- ✅ Designed to actually _understand_ RAG, not just run it

---

## 🧩 How Koda Works (High Level)

When you ask a question, Koda follows this flow:
