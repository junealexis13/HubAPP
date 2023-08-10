import pandas as pd
import glob, os
import streamlit as st

from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title('HubAPP')

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("pages/home.py", "Home", "🏠"),
        Page("pages/dtr.py", "DTR", ":books:"),
    ]
)


st