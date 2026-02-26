import streamlit as st

st.title("📚 AI Study Buddy")

topic = st.text_input("Enter a topic to study:")

if st.button("Generate"):
    if topic:
        st.subheader("📖 Explanation")
        st.write(f"{topic} is an important concept. This is a simple explanation for beginners.")

        st.subheader("📝 Summary")
        st.write(f"In short, {topic} helps us understand key ideas in an easy way.")

        st.subheader("❓ Quiz")
        st.write(f"1. What is {topic}?")
        st.write(f"2. Why is {topic} important?")
    else:
        st.warning("Please enter a topic!")