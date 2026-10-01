import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Netflix Data Analysis", layout="wide")

st.title("🎬 Netflix Data Analysis Interactive Dashboard")
st.markdown("Explore the Netflix dataset with Power BI-like interactive visualizations.")

@st.cache_data
def load_data():
    df = pd.read_csv('mymoviedb.csv', lineterminator='\n')
    df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')
    df['Year'] = df['Release_Date'].dt.year
    df.drop(['Overview', 'Original_Language', 'Poster_Url'], axis=1, inplace=True, errors='ignore')
    return df

try:
    df = load_data()

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Movies", f"{df.shape[0]:,}")
    col2.metric("Average Rating", round(df['Vote_Average'].mean(), 2))
    col3.metric("Total Votes", f"{df['Vote_Count'].sum():,}")
    col4.metric("Years Spanned", f"{int(df['Year'].min())} - {int(df['Year'].max())}")
    
    st.markdown("---")

    # Filters
    st.sidebar.header("Dashboard Filters")
    min_year = int(df['Year'].min()) if not pd.isna(df['Year'].min()) else 1900
    max_year = int(df['Year'].max()) if not pd.isna(df['Year'].max()) else 2025
    selected_year = st.sidebar.slider("Select Release Year Range", min_value=min_year, max_value=max_year, value=(min_year, max_year))
    
    genre_options = sorted(list(set(', '.join(df['Genre'].dropna()).split(', '))))
    selected_genres = st.sidebar.multiselect("Select Genres", options=genre_options, default=genre_options[:5])
    
    # Apply Filters
    filtered_df = df[(df['Year'] >= selected_year[0]) & (df['Year'] <= selected_year[1])]
    if selected_genres:
        # Regex to match any of the selected genres
        pattern = '|'.join(selected_genres)
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(pattern, na=False, regex=True)]

    st.subheader(f"Filtered Data: {filtered_df.shape[0]} Movies")
    
    # Row 1 of Charts
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Top 10 Most Popular Movies**")
        top_popular = filtered_df.nlargest(10, 'Popularity')
        fig1 = px.bar(top_popular, x='Popularity', y='Title', orientation='h', color='Popularity', color_continuous_scale='Viridis')
        fig1.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig1, use_container_width=True)

    with c2:
        st.markdown("**Top 10 Highest Rated Movies** (min. 1000 votes)")
        top_rated = filtered_df[filtered_df['Vote_Count'] >= 1000].nlargest(10, 'Vote_Average')
        fig2 = px.bar(top_rated, x='Vote_Average', y='Title', orientation='h', color='Vote_Average', color_continuous_scale='Magma')
        fig2.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig2, use_container_width=True)

    # Row 2 of Charts
    c3, c4 = st.columns(2)
    with c3:
        st.markdown("**Movies Released Over Time**")
        movies_per_year = filtered_df.groupby('Year').size().reset_index(name='Count')
        fig3 = px.line(movies_per_year, x='Year', y='Count', markers=True)
        st.plotly_chart(fig3, use_container_width=True)
        
    with c4:
        st.markdown("**Popularity vs Rating Scatter Plot**")
        fig4 = px.scatter(filtered_df.sample(min(1000, len(filtered_df)), random_state=42), 
                          x='Vote_Average', y='Popularity', color='Vote_Average', hover_name='Title')
        st.plotly_chart(fig4, use_container_width=True)
        
    st.markdown("---")
    st.subheader("Dataset Details")
    st.dataframe(filtered_df)

except FileNotFoundError:
    st.error("Dataset 'mymoviedb.csv' not found. Please ensure it is in the same directory.")
