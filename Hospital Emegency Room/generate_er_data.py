import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Generate 9,216 patient records (matching your dashboard)
n = 9216

# Age groups with realistic distribution
age_groups = ['<20', '20-30', '30-40', '40-50', '50-60', '60+']
age_weights = [0.01, 0.02, 0.05, 0.10, 0.15, 0.67]  # Matches your 60+ = 33%

# Race distribution (matches your dashboard)
races = ['White', 'Black', 'Other']
race_weights = [0.92, 0.08, 0.00]

# Gender (matches your 36/64 split)
genders = ['Male', 'Female']
gender_weights = [0.36, 0.64]

data = {
    'patient_id': range(1, n+1),
    'age_group': np.random.choice(age_groups, n, p=age_weights),
    'race': np.random.choice(races, n, p=race_weights),
    'gender': np.random.choice(genders, n, p=gender_weights),
    'wait_time_minutes': np.random.exponential(30, n) + 5,  # Avg ~35 min
    'satisfaction_score': np.random.normal(4.5, 1.2, n).clip(1, 5),
    'bed_occupied': np.random.choice([0, 1], n, p=[0.6, 0.4]),  # 38% occupancy
    'arrival_date': [datetime.today() - timedelta(days=np.random.randint(0, 90)) for _ in range(n)]
}

df = pd.DataFrame(data)
df['wait_time_minutes'] = df['wait_time_minutes'].round(1)
df['satisfaction_score'] = df['satisfaction_score'].round(1)

df.to_csv('er_data.csv', index=False)
print("✅ er_data.csv created with 9,216 records!")
