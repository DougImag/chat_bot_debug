# 🧠 Python AI Debugger (RAG + OpenRouter)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-Free-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-Compatible-blue?logo=openai)
![LangChain](https://img.shields.io/badge/LangChain-RAG-blue)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-blue)

Un **assistant de débogage Python** en ligne de commande, basé sur l’IA, utilisant **OpenRouter (accès gratuit)** et une approche **RAG (Retrieval-Augmented Generation)** pour analyser des erreurs Python, expliquer leur cause et proposer des corrections concrètes.

## 🚀 Fonctionnalités

-  Analyse de code Python et de tracebacks
-  Explications claires des erreurs
-  Propositions de corrections avec exemples de code
-  Utilisation d’un contexte local (`debug.txt`) via RAG
-  Interface CLI simple et interactive
-  Compatible OpenRouter (modèles gratuits)

## 📁 Structure du projet

- FAQ_chat_agent.py      
- debug.txt              
- requirements.txt
- README.md
- .env                   

## 🔑 Création d’une clé API OpenRouter

Le projet utilise **OpenRouter** pour accéder gratuitement à des modèles de langage.

### Étapes :

1. Aller sur 👉 https://openrouter.ai
2. Créer un compte (GitHub ou email)
3. Aller dans **Settings → API Keys**
4. Créer une nouvelle clé API
5. Copier la clé (elle commence par `sk-or-...`)
6. Mettre la clé dans le fichier .env
