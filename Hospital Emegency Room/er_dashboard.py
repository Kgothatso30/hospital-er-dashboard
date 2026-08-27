import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Hospital ER Dashboard", layout="wide")
st.title("🏥 Hospital Emergency Room Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('er_data.csv')

df = load_data()

# --- KPI CARDS (Top Row) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Patient Flow", f"{len(df):,}")

with col2:
    avg_wait = df['wait_time_minutes'].mean()
    st.metric("⏱️ Avg Wait Time", f"{avg_wait:.1f} min")

with col3:
    avg_satisfaction = df['satisfaction_score'].mean()
    st.metric("⭐ Satisfaction Score", f"{avg_satisfaction:.2f}")

with col4:
    bed_occupancy = df['bed_occupied'].mean() * 100
    st.metric("🛏️ Beds Occupied", f"{bed_occupancy:.0f}%")

st.divider()

# --- CHARTS (Two Columns) ---
col1, col2 = st.columns(2)

with col1:
    # Gender Distribution (Pie Chart)
    gender_counts = df['gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    fig_gender = px.pie(
        gender_counts, 
        values='Count', 
        names='Gender',
        title='Gender Distribution',
        color_discrete_sequence=['#1f77b4', '#ff7f0e']
    )
    fig_gender.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_gender, use_container_width=True)

with col2:
    # Age Group Distribution (Bar Chart)
    age_counts = df['age_group'].value_counts().reindex(
        ['<20', '20-30', '30-40', '40-50', '50-60', '60+']
    ).reset_index()
    age_counts.columns = ['Age Group', 'Count']
    fig_age = px.bar(
        age_counts, 
        x='Age Group', 
        y='Count',
        title='Age Group Distribution',
        color='Age Group',
        color_discrete_sequence=px.colors.sequential.Blues_r
    )
    st.plotly_chart(fig_age, use_container_width=True)

# --- RACE DISTRIBUTION (Full Width) ---
race_counts = df['race'].value_counts().reset_index()
race_counts.columns = ['Race', 'Count']
fig_race = px.bar(
    race_counts,
    x='Race',
    y='Count',
    title='Race Distribution',
    color='Race',
    color_discrete_sequence=['#2ca02c', '#d62728', '#9467bd']
)
st.plotly_chart(fig_race, use_container_width=True)

# --- RAW DATA (Expandable) ---
with st.expander("📊 View Raw Data"):
    st.dataframe(df.head(100))