import streamlit as st


#Title

st.title("Ask a question")

#header

st.header("Upload an image")

#upload file

file = st.file_uploader("", type = ["jpeg", "png", "jpg"])

if file:

    #image display
    st.image(file, use_column_width = True)

    #Text input
    user_question = st.text_input('Ask a question about your image')



    #Write agent repsonse
    if user_question and user_question != "":
        st.write('wrong')