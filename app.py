## Packages required for project
import streamlit as st
import streamlit.components.v1 as components
import requests
import json

st.title("Named Entity Recognition on Wikipedia")
st.subheader("Input appropriate words like for Google : search 'Google Inc' to avoid error")
raw_text = st.text_area("Your Text","Enter Text Here")
raw_text = raw_text.replace(" ", "_")
## Using the Flask api for performing NER
your_url = 'http://swapnilsrivastava.pythonanywhere.com/'+raw_text
if st.button("Submit"):
    result = requests.get(your_url).content
    html_dict = json.loads(result)
    web_page = html_dict['html_data']
    ## Using Streamlit to display the Result
    st.components.v1.html(web_page,
       height=3000,
       width=750)
