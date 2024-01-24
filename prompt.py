import streamlit as st

from dotenv import load_dotenv
import openai
from openai import OpenAI

import docx
import os
import time

def configure():
    load_dotenv()

# Function to extract text from a Word document
def read_word_file(doc_file):
    doc = docx.Document(doc_file)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to communicate with OpenAI assistant
def get_openai_response(text,prompt):
    configure()

    # Assuming you have set up OpenAI API key in your environment variables
  
    client = OpenAI(

    api_key= os.getenv("APIKEY")
 
    ) 

    

    response = client.chat.completions.create(
        model="gpt-4",  # or the model you're using
        
        messages=[{"role": "system", "content": f"in this document {prompt}"},
                  {"role": "user", "content": text}]
    )
    return response.choices[0].message.content 

# Streamlit interface
st.title("Word Document Reader with OpenAI Assistant by Ahmad Dalain")

pw=st.text_input("insert password")

if pw == "TME=fast":


    st.markdown("In your contrcat draft word document or offer or any word document, get the assitant advise")

    uploaded_file = st.file_uploader("Upload a Word document, no more than 7000 words", type="docx")


    if uploaded_file is not None:
        text = read_word_file(uploaded_file)
        # st.write("Document Text:")
        # st.write(text)
        prompt = st.text_input("clarify your query here in details --->     Example(find me clauses related to payment and provide me professional legal advice for each one )")

        if st.button('Get Assistant Response'):
            if not prompt:
                st.warning("fill your query in the above prompt first to get Assistant answer")
       

            else:
                with st.spinner('Wait for it...'):
        
                    response = get_openai_response(text,prompt)
               
                    time.sleep(1)
                    st.success('Done!')
                    st.write("Assistant Response:")
                    st.write(response)
   
