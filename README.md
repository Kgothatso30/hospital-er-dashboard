# 🏥 Hospital Emergency Room Dashboard

## Project Overview
An interactive data dashboard for analyzing emergency room operations, patient flow, and service efficiency. This tool enables healthcare administrators to make data-driven decisions to improve patient experience and optimize ER performance.

## 📊 Key Metrics
- **Patient Flow:** 9,216 patients analyzed
- **Average Wait Time:** 35.3 minutes
- **Satisfaction Score:** 4.99 / 5.0
- **Bed Occupancy:** 38%

## 📈 Dashboard Features
- **Gender Distribution** - 36% Male / 64% Female
- **Age Group Analysis** - 60+ accounts for 33% of visits
- **Race Distribution** - 92% White, 8% Black
- **Interactive Charts** - Hover for detailed values
- **Raw Data Access** - Expandable data table

## 🛠️ Technologies Used
- **Python** - Data processing and analysis
- **Streamlit** - Interactive dashboard framework
- **Pandas** - Data manipulation
- **Plotly** - Interactive visualizations

## 🚀 How to Run the Dashboard

### Prerequisites
- Python 3.7+
- pip package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/24052292W/hospital-er-dashboard.git

# Navigate to project folder
cd hospital-er-dashboard

# Install required packages
pip install streamlit pandas numpy plotly

# Generate the data
python generate_er_data.py

# Run the dashboard
streamlit run er_dashboard.py
