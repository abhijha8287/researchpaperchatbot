# 📚 Research Paper Chatbot

A smart and interactive **research summarization tool** that explains famous machine learning research papers in various styles and depths — powered by OpenAI's GPT-4 and built with Streamlit.

🔗 **Live App**: [https://researchpaperchatbotbyabhishek.streamlit.app](https://researchpaperchatbotbyabhishek.streamlit.app)

> ⚠️ **Note**: If the app is asleep (Streamlit Community Cloud does this when inactive), click **“Wake App”** and wait a few seconds before interacting.

---

## 🤖 What It Does

This chatbot takes a famous research paper (like BERT or GPT-3) and explains it to you in a personalized way. You choose:

- 📄 The paper name
- 🎓 The explanation style: Beginner-friendly, Technical, Code-Oriented, or Mathematical
- 📏 The explanation length: Short, Medium, or Long

Then, it generates a custom explanation using **GPT-4**, tailored to your inputs.

---

## 🎯 Use Cases

- 🧑‍🎓 Students trying to understand cutting-edge research
- 🧪 Researchers summarizing papers for different audiences
- 🧑‍💻 Developers looking for code-level insights
- 🧠 Anyone curious about how modern ML models work

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [LangChain](https://www.langchain.com/) + [OpenAI GPT-4](https://platform.openai.com/)
- **Prompting**: Uses `PromptTemplate` for dynamic prompt generation
- **Secrets Handling**: `.env` + `st.secrets` for secure API key usage

---

## 🚀 How It Works

1. User selects:
   - A research paper
   - Explanation style (e.g., Beginner-Friendly)
   - Desired length (e.g., Medium)
2. The app dynamically fills a prompt template with the selected inputs.
3. The prompt is sent to GPT-4 via LangChain.
4. The result is displayed in the Streamlit UI.

---

## 🧾 Example Prompt Template

```txt
Please generate a {length_input} explanation of {paper_input} in {style_input} style.
