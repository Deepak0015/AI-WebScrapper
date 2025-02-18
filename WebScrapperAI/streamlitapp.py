import streamlit as st 
from scrap import Scrapping 
from prompt import response


st.title("AI Web Scrapper ")

scrapper =  Scrapping()

url = st.text_input('Enter website URL')

if st.button('Scrap website'):
    if url:
        st.write("Scrapping the website...")

        dom_content = scrapper.scrap(url)

        body_content = scrapper.extract_content(dom_content)

        cleaned_content =  scrapper.clean_body(body_content)

        st.session_state.dom_content = cleaned_content 

        with st.expander('View Dom Content'):
            st.text_area('Dom Content' , cleaned_content  , height = 300)



if 'dom_content' in st.session_state:
    description  = st.text_area("Descripe What You Want To Parse")
    if st.button('Parse Content'):
        if description:
            st.write('Parsing the content....')

            dom_chunks  =   scrapper.split_dom_content(st.session_state.dom_content)

            result = response( dom_chunks , description)
            st.write(result)

