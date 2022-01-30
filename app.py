from streamlit_sketch_rnn_labeling_tool import st_sketch_tool
import streamlit as st
import numpy as np
import pandas as pd

@st.cache
def process_data(raw_data):
    np_data = np.asarray(raw_data, dtype=np.int32)[:-1]
    df = pd.DataFrame(np_data, columns=["x", "y", "p1", "p2", "p3"])
    csv_data = df.to_csv().encode('utf-8')
    return df, csv_data

st.title("Sketch Labeling Tool")

data = st_sketch_tool(width=640, height=480, key="a")

df, csv_data = process_data(data)

st.write("check out the [GitHub repository](https://github.com/wingedrasengan927/streamlit-sketch-rnn-labelling-tool) for more details")


col1, col2 = st.columns(2)

with col1:
    file_name = st.text_input('Please Enter File Name', 'sketch_data')
    st.caption("Please click the finish button before downloading")
    st.download_button(
        label="Download data as CSV",
        data=csv_data,
        file_name=file_name + ".csv",
        mime='text/csv',
    )

with col2:
    st.caption("data")
    st.dataframe(df)

