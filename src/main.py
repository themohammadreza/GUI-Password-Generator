from password_generator import RandomPasswordGenerator, MemorablePasswordGenerator, PinGenerator
import streamlit as st


st.title("Password Generator")

password_type = st.selectbox("Select password type:", ["Random", "Memorable", "PIN"])

if password_type == "Random":
    length = st.slider("Select password length:", 8, 32, 16)
    include_uppercase = st.checkbox("Include uppercase letters?")
    include_numbers = st.checkbox("Include numbers?")
    include_symbols = st.checkbox("Include symbols?")
    generator = RandomPasswordGenerator(length, include_uppercase, include_numbers, include_symbols)
elif password_type == "Memorable":
    number_of_words = st.slider("Select number of words:", 2, 8, 4)
    capitalize = st.checkbox("Capitalize words?")
    generator = MemorablePasswordGenerator(number_of_words, capitalize)
elif password_type == "PIN":
    length = st.slider("Select PIN length:", 4, 16, 6)
    generator = PinGenerator(length)

if st.button("Generate Password"):
    password = generator.generate()
    st.success(fr"Generated Password: ```{password}```")
