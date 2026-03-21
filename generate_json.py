import json
import pandas as pd
import numpy as np

demo = pd.read_excel('PatientDemographics.xlsx').head(50)
clinical = pd.read_excel('ClinicalIntake.xlsx').head(50)
admin = pd.read_excel('AdministrativeFlags.xlsx').head(50)

# Drop LanguagePreference from admin before merging to avoid duplicate columns
admin = admin.drop(columns=['LanguagePreference'])

# Merge all three on PatientID
merged = demo.merge(clinical, on='PatientID').merge(admin, on='PatientID')

# Replace NaN with empty string
merged = merged.replace({np.nan: ''})

# Convert to list of dicts
patients = merged.to_dict(orient='records')

# Write to JSON
with open('patients.json', 'w') as f:
    json.dump(patients, f, indent=2, default=str)

print(f"Generated {len(patients)} patients in patients.json")
print(f"File size: {__import__('os').path.getsize('patients.json') / 1024:.1f} KB")