import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Titanic Survival Interactive Dashboard")

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
df['age'] = df['age'].fillna(df['age'].median())
df['embarked'] = df['embarked'].fillna('Unknown')

# Sidebar filters
st.sidebar.header("Choose your view")
x = st.sidebar.selectbox("X-axis (categorical)", df.select_dtypes(include='object').columns, index=1)
y = st.sidebar.selectbox("Y-axis (numeric)", df.select_dtypes(include='number').columns, index=0)
hue = st.sidebar.selectbox("Hue (optional)", ['None'] + df.select_dtypes(include='object').columns.tolist(), index=0)

# Main plot
fig, ax = plt.subplots(figsize=(10, 6))
if hue == 'None':
    sns.barplot(x=x, y=y, data=df, ax=ax)
else:
    sns.barplot(x=x, y=y, hue=hue, data=df, ax=ax)

ax.set_title(f"{y} by {x}" + (f" (hue: {hue})" if hue != 'None' else ''))
plt.xticks(rotation=45)
st.pyplot(fig)

# Optionally: show data preview
if st.checkbox("Show raw data"):
    st.dataframe(df.head())
