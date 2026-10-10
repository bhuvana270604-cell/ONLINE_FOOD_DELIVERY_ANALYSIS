import streamlit as st
import pandas as pd

st.set_page_config(
page_title="Online Food Delivery Analysis",
page_icon="🍔",
layout="wide"
)

st.title("🍔 Online Food Delivery Analysis")
st.write("Analysis of customer orders, delivery performance, ratings and sales.")

# Load dataset

df = pd.read_csv("online_food_delivery_cleaned.csv") 

# Dataset Overview

st.header("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Orders", len(df))
with col2:
    st.metric("Cities", df["City"].nunique())

with col3:
    st.metric("Restaurants", df["Restaurant_Name"].nunique())

# Show Data

st.subheader("📋 Food Delivery Data")
st.dataframe(df)

# Summary
st.header("📈 Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Order Value", round(df["Order_Value"].mean(), 2))

with col2:
    st.metric("Average Delivery Time", round(df["Delivery_Time_Min"].mean(), 2))

with col3:
    st.metric("Average Restaurant Rating", round(df["Restaurant_Rating"].mean(), 2))

# Orders by City
st.subheader("🏙️ Top Cities by Number of Orders")
st.bar_chart(df["City"].value_counts().head(10))