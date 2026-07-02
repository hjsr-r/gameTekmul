import streamlit as st
import streamlit.components.v1 as components

# 1. Atur layout halaman Streamlit menjadi "wide" (lebar)
st.set_page_config(layout="wide")
scratch_iframe = """
<iframe src="https://scratch.mit.edu/projects/1350792459/embed" 
        allowtransparency="true" 
        width="100%" 
        height="600" 
        frameborder="0" 
        scrolling="no" 
        allowfullscreen>
</iframe>
"""

# 3. Render iframe dengan parameter scrolling=True pada komponen Streamlit-nya
components.html(scratch_iframe, height=620, scrolling=True)
