import streamlit as st

st.set_page_config(page_title="Data Analyst Internship Portfolio", layout="wide")

st.title("📊 Data Analyst Internship Portfolio")
st.subheader("ApexPlanet Software Pvt. Ltd. Internship")

st.write("""
Welcome to my Data Analyst Internship Portfolio.
This portfolio showcases all projects completed during the internship.
""")

st.header("🚀 Projects Completed")

st.markdown("""
### Task 1 – Data Cleaning & EDA
- Data Cleaning
- Missing Value Handling
- Exploratory Data Analysis

### Task 2 – Business Insights & Visualization
- KPI Analysis
- Sales & Profit Analysis
- Data Storytelling

### Task 3 – Interactive Dashboard
- Dashboard Development
- Business Reporting
- Interactive Visualizations

### Task 4 – Time Series Forecasting
- Forecasting Models
- Trend Analysis
- Model Evaluation
""")

st.header("🛠 Skills Demonstrated")

skills = [
    "Python",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Scikit-learn",
    "Statsmodels",
    "Git",
    "GitHub"
]

for skill in skills:
    st.write("✅", skill)

st.header("📚 Key Learnings")

st.write("""
- Data Cleaning & Preparation
- Exploratory Data Analysis
- Dashboard Development
- Business Intelligence
- Forecasting & Predictive Analytics
- Version Control with Git & GitHub
""")

st.header("🎯 Internship Outcome")

st.success(
    "Successfully completed an end-to-end Data Analytics workflow "
    "from data preparation to forecasting and business storytelling."
)

st.header("🔗 GitHub Project Links")

st.write("Task 1 Repository:https://github.com/HasiniLavanga/Data-Wrangling-ApexPlanet")
st.write("Task 2 Repository:https://github.com/HasiniLavanga/EDA-Business-Intelligence-ApexPlanet")
st.write("Task 3 Repository:https://github.com/HasiniLavanga/superstore-sales-dashboard-analysis")
st.write("Task 4 Repository:https://github.com/HasiniLavanga/house-price-simple-app")