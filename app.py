import streamlit as st
import Llama2

def main():
    st.title("🦙 Documents search and queries")
    st.write("Enter your queries and chat with your document")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter your prompt or summarize about..."):
        with st.chat_message("human"):
            st.markdown(f"User: {prompt}")
        st.session_state.messages.append(
            {"role": "user", "content": f"User:  {prompt}"}
        )

        response = Llama2.get_response(prompt)

        with st.chat_message("ai"):
            st.markdown(f"Llama: {response}")
        st.session_state.messages.append(
            {"role": "assistant", "content": f"Llama:  {response}"}
        )


if __name__ == "__main__":
    main()
