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
    st.metric(
        "Average Order Value",
        round(df["Order_Value"].mean(), 2)
    )

with col2:
    st.metric(
        "Average Delivery Time",
        round(df["Delivery_Time_Min"].mean(), 2)
    )

with col3:
    st.metric(
        "Average Restaurant Rating",
        round(df["Restaurant_Rating"].mean(), 2)
    )

# Orders by City
st.subheader("🏙️ Top Cities by Number of Orders")

city_orders = df["City"].value_counts().head(10)

st.bar_chart(city_orders)

# Cuisine Analysis
st.subheader("🍕 Cuisine Type Analysis")

cuisine_orders = df["Cuisine_Type"].value_counts().head(10)

st.bar_chart(cuisine_orders)

# Payment Mode
st.subheader("💳 Payment Mode Analysis")

payment_orders = df["Payment_Mode"].value_counts()

st.bar_chart(payment_orders)

# Order Status
st.subheader("📦 Order Status")

status_orders = df["Order_Status"].value_counts()

st.bar_chart(status_orders)

# Delivery Performance
st.subheader("🚚 Delivery Performance")

performance = df["Delivery_Performance"].value_counts()

st.bar_chart(performance)

# Highest Order Value
st.subheader("💰 Highest Order Value")

max_order = df.loc[df["Final_Amount"].idxmax()]

st.write("Order ID:", max_order["Order_ID"])
st.write("City:", max_order["City"])
st.write("Restaurant:", max_order["Restaurant_Name"])
st.write("Final Amount:", max_order["Final_Amount"])

# Ratings
st.subheader("⭐ Ratings Analysis")

col1, col2 = st.columns(2)

with col1:
    st.write("Restaurant Rating")
    st.bar_chart(df["Restaurant_Rating"].value_counts().sort_index())

with col2:
    st.write("Delivery Rating")
    st.bar_chart(df["Delivery_Rating"].value_counts().sort_index())

st.success("Food Delivery Analysis completed successfully!")