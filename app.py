import streamlit as st

st.title("Hello World !!!")

st.header("This is a header") 
st.subheader("This is a subheader")

st.text("Hello GeeksForGeeks!!!")

st.markdown("### This is a markdown ised for medium sized headings")
st.markdown("# This is a header")
st.markdown("This is **bold** text and this is *italic* text")
st.markdown("- Item 1\n- Item 2\n- Item 3")
st.markdown("[Click Here](https://streamlit.io) to visit Streamlit Website.")

st.write("Hello, **World**")
st.write([1, 2, 3])
st.write({"name": "Streamlit"})
st.text("Hello, **World**")

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

from PIL import Image
img = Image.open("Streamlit.png")
st.image(img, width=200)
st.image(img, width=400)

if st.checkbox("Show/Hide"):
    st.text("Showing the widget")

status = st.radio("Select Gender:", ['Male', 'Female'])
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is:", hobby)

hobbies = st.multiselect("Select Your Hobbies:", ['Dancing', 'Reading', 'Sports'])
st.write("You selected", len(hobbies), "hobbies")


st.button("Click Me")
if st.button("About"):
    st.text("Welcome to GeeksForGeeks!")

name = st.text_input("Enter your name",)
if st.button("Submit"):
    result = name.title()
    st.success(result)

level = st.slider("Choose a level", min_value=1, max_value=5)
st.write(f"Selected level: {level}")    