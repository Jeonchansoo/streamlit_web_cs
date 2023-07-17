import streamlit as st
import pandas as pd

st.write('# Youtube view')
st.write('## raw')
view = [100,150,30]
view

st.write('## barchart')
st.bar_chart(view)

sview = pd.Series(view)
sview