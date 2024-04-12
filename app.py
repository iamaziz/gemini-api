import streamlit as st

from gemini import Gemini, MODELS

st.set_page_config(layout="wide")

st.sidebar.title("Gemini Chat")
selected_model = st.sidebar.selectbox("Choose a model", MODELS)


@st.cache_resource(show_spinner=False)
def init_chat(model):
    gemini = Gemini(model_name=model)
    return gemini.model.start_chat(history=[]), gemini


def upload_file():
    uploaded_file = st.sidebar.file_uploader("Upload text file", type=["txt", "py", "json", "md"])
    return uploaded_file.read().decode("utf-8") if uploaded_file else None


def st_chat_message(text, role="user"):
    with st.chat_message(name=role): st.write(text)


def print_conversation_history(chat):
    for message in chat.history:
        role = "user" if message.role == "user" else "ai"
        st_chat_message(message.parts[0].text, role)


def main():
    prompt = st.chat_input("Ask me anything!")
    gemini_chat, gemini = init_chat(selected_model)

    uploaded_text = upload_file()

    print_conversation_history(gemini_chat)

    # -- prompt with text from the uploaded file
    if uploaded_text and prompt:
        context_prompt = f"{prompt}\n\n{uploaded_text}"
        st_chat_message(prompt, role="human")
        answer = gemini_chat.send_message(context_prompt).text
        st_chat_message(answer, role="ai")

    # -- regular chatbot
    elif prompt:
        st_chat_message(prompt, role="human")
        answer = gemini_chat.send_message(prompt).text
        st_chat_message(answer, role="ai")

    


if __name__ == "__main__":
    main()
