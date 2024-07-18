import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("redbus_data.csv")

# Clean 'bus_type' column
df["bus_type"] = df["bus_type"].str.split("\n").str[-1]
df.dropna(subset=["bus_type"], inplace=True)

df.dropna(subset=["price"], inplace=True)


def convert_duration_to_minutes(duration):
    if pd.isna(duration):
        return np.nan
    parts = duration.split(" ")
    hours = int(parts[0].replace("h", ""))
    minutes = int(parts[1].replace("m", ""))
    return hours * 60 + minutes


df["duration_minutes"] = df["duration"].apply(convert_duration_to_minutes)
df.dropna(subset=["duration_minutes"], inplace=True)


# Streamlit app
st.set_page_config(page_title="Redbus", page_icon=":bus:", layout="wide")
st.title(" :bus: REDBUS DASHBOARD")
st.markdown(
    "<style>div.block-container{padding-top:2rem;}</style", unsafe_allow_html=True
)

# Display raw data
st.header("Scrapped Data")
st.write(df)

# Display summary statistics
st.header("Summary Statistics")
st.write(df.describe())

# sidebar
st.sidebar.header("Choose your filter: ")

# Filter by Route
route = st.sidebar.multiselect("Pick your Route", df["route_name"].unique())
if not route:
    df2 = df.copy()
else:
    df2 = df[df["route_name"].isin(route)]

# Filter by Bus
bus = st.sidebar.multiselect("Pick the Bus", df2["bus_name"].unique())
if not bus:
    df3 = df2.copy()
else:
    df3 = df2[df2["bus_name"].isin(bus)]

# Filter by Bus Type
bus_type = st.sidebar.multiselect("Pick the Bus Type", df3["bus_type"].unique())
if not bus_type:
    df4 = df3.copy()
else:
    df4 = df3[df3["bus_type"].isin(bus_type)]

# Filter by Price Range
if df4["price"].nunique() == 1:
    price_min, price_max = df4["price"].min(), df4["price"].max() + 1
else:
    price_min, price_max = int(df4["price"].min()), int(df4["price"].max())
price_range = st.sidebar.slider(
    "Pick your price range",
    min_value=price_min,
    max_value=price_max,
    value=(price_min, price_max),
)

# Filter by Duration Range
duration_min, duration_max = int(df4["duration_minutes"].min()), int(
    df4["duration_minutes"].max()
)
duration_range = st.sidebar.slider(
    "Pick your duration range (minutes)",
    min_value=duration_min,
    max_value=duration_max+1,
    value=(duration_min, duration_max+1),
)

# Filter the data based on selected options
filtered_df = df4[(df4["price"] >= price_range[0]) & (df4["price"] <= price_range[1])]
filtered_df = filtered_df[
    (filtered_df["duration_minutes"] >= duration_range[0])
    & (filtered_df["duration_minutes"] <= duration_range[1])
]

# Display charts
st.header("Charts")
st.subheader("Seat availability")
st.bar_chart(filtered_df["seats_available"].value_counts())

st.subheader("Price Distribution")
price_counts, bin_edges = np.histogram(filtered_df["price"], bins=10)
histogram_data = pd.DataFrame({"Price Range": bin_edges[:-1], "Count": price_counts})
st.bar_chart(histogram_data.set_index("Price Range"))

# Additional charts
st.subheader("Bus Type Distribution")
st.bar_chart(filtered_df["bus_type"].value_counts())

st.subheader("Departure Times")
st.line_chart(filtered_df["depart_time"].value_counts().sort_index())

st.subheader("Arrival Times")
st.line_chart(filtered_df["arrival_time"].value_counts().sort_index())

st.subheader("Trip Duration Distribution (In Minutes)")
duration_counts, duration_bin_edges = np.histogram(
    filtered_df["duration_minutes"].dropna(), bins=10
)
duration_histogram_data = pd.DataFrame(
    {"Duration Range": duration_bin_edges[:-1], "Count": duration_counts}
)
st.bar_chart(duration_histogram_data.set_index("Duration Range"))

# Add footer
st.write("Data sourced from RedBus website")
