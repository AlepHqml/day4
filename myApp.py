import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data
@st.cache_data
def load_data():
    df = pd.read_csv("banking.csv")  # Ensure 'banking.csv' is in the app's directory
    return df

# Function for data visualization
def data_visualization_page(df):
    st.title("📊 Data Visualization")
    st.markdown("## Interactive Visualizations")

    st.write("### Dataset Preview")
    st.dataframe(df)

    # Dynamically list column names
    available_columns = df.columns.tolist()

    # Dropdowns for choosing columns for Chart 1
    st.markdown("### Chart 1 Options")
    col_x = st.selectbox("Select X-Axis", options=available_columns, key="chart1_x")
    col_color1 = st.selectbox("Select Color/Grouping", options=available_columns, key="chart1_color")

    # Dropdowns for choosing columns for Chart 2
    st.markdown("### Chart 2 Options")
    col_y = st.selectbox("Select Y-Axis", options=available_columns, key="chart2_y")
    col_color2 = st.selectbox("Select Color/Grouping", options=available_columns, key="chart2_color")

    # Dropdown for filtering the dataset
    st.markdown("### Data Filtering Options")
    filter_col = st.selectbox("Select Column to Filter By", options=available_columns, key="filter_col")
    filter_values = st.multiselect(
        f"Select values in {filter_col}", options=df[filter_col].unique(), default=df[filter_col].unique()
    )

    # Apply the filter
    filtered_df = df[df[filter_col].isin(filter_values)]

    # Two-column layout for displaying charts
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Chart 1: Interactive Histogram")
        fig1 = px.histogram(
            filtered_df,
            x=col_x,
            color=col_color1,
            title=f"{col_x} Distribution by {col_color1}",
            template="plotly_dark",
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.markdown("### Chart 2: Interactive Boxplot")
        fig2 = px.box(
            filtered_df,
            y=col_y,
            x=col_color2,
            color=col_color2,
            points="all",
            title=f"{col_y} Distribution by {col_color2}",
            template="plotly_white",
        )
        st.plotly_chart(fig2, use_container_width=True)

# Define Main Function for Multipage Support
def main():
    st.sidebar.title("📂 Navigation")
    menu = ["Home", "Data Visualization"]
    choice = st.sidebar.radio("Go to", menu)

    # Load data
    df = load_data()

    # Page Navigation
    if choice == "Home":
        st.title("🏡 Welcome to the Banking Data App")
        st.markdown(
            """
            This application is designed to analyze and visualize **banking data**. 
            Use the sidebar to navigate through the app.
            """
        )
    elif choice == "Data Visualization":
        data_visualization_page(df)

# Run the app
if __name__ == "__main__":
    main()
    