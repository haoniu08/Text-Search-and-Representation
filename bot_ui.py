import streamlit as st
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
from sklearn.neighbors import KDTree
import numpy as np
import shelve
import time

# Load or train Word2Vec model
def load_or_train_model():
    corpus = [
        "hello how are you",
        "good morning",
        "hi there",
        "I'm fine, thanks",
        "how can I help you",
    ]

    sentences = [simple_preprocess(sentence) for sentence in corpus]
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

    responses = [
        "hello how are you",
        "good morning",
        "hi there",
        "I'm fine, thanks",
        "how can I help you"
    ]

    response_vectors = [np.mean([model.wv[word] for word in response.split() if word in model.wv], axis=0) for response in responses]
    response_vectors = np.array(response_vectors)

    tree = KDTree(response_vectors)
    return model, tree, responses

model, tree, responses = load_or_train_model()

def get_best_response(user_input):
    user_vector = np.mean([model.wv[word] for word in user_input.lower().split() if word in model.wv], axis=0)
    if user_vector is None:
        return "Sorry, I didn't understand that."

    dist, ind = tree.query([user_vector], k=1)
    nearest_response_index = ind[0][0]

    return responses[nearest_response_index]

st.title("Artificial without Intelligence")
st.header("🤖 The bot you wish you never met")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

# Ensure messages are initialized in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize session state for user message count
if 'user_message_count' not in st.session_state:
    st.session_state.user_message_count = 0

# Load chat history from shelve file
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages

# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])

# Custom CSS for chat layout
st.markdown("""
    <style>
    .user-message {
        text-align: right;
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
        display: inline-block;
        max-width: 70%;
    }
    .bot-message {
        text-align: left;
        background-color: #F1F0F0;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
        display: inline-block;
        max-width: 70%;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    </style>
    """, unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    message_class = "user-message" if message["role"] == "user" else "bot-message"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(f'<div class="{message_class}">{message["content"]}</div>', unsafe_allow_html=True)

# Main chat interface
if prompt := st.chat_input("How can I help?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.user_message_count += 1

    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

    # Introduce delay before bot's response
    time.sleep(0.5)

    if st.session_state.user_message_count == 3:
        response = "ARE you done bro???"
        st.session_state.user_message_count = 0
        response = get_best_response(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        st.markdown(f'<div class="bot-message">{response}</div>', unsafe_allow_html=True)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Save chat history after each interaction
save_chat_history(st.session_state.messages)