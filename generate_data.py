import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_PATIENTS = 100000

# ── Lookup tables ─────────────────────────────────────────
INSURANCE_PROVIDERS = [
    "Blue Cross Blue Shield", "Aetna", "UnitedHealth", "Cigna",
    "Humana", "Medicare", "Medicaid", "Kaiser Permanente",
    "Anthem", "Centene"
]

CHIEF_COMPLAINTS = [
    "Chest pain and shortness of breath",
    "Severe headache and dizziness",
    "Abdominal pain and nausea",
    "Fever and persistent cough",
    "Lower back pain radiating to left leg",
    "Fatigue and unexplained weight loss",
    "Palpitations and lightheadedness",
    "Swelling in lower extremities",
    "Confusion and memory lapses",
    "Allergic reaction with hives",
    "Knee pain following fall",
    "Urinary frequency and burning sensation",
    "Blurred vision and eye pain",
    "Rash spreading across torso",
    "Anxiety and panic attacks"
]

MEDICATIONS = [
    "Lisinopril 10mg daily, Metformin 500mg twice daily",
    "Atorvastatin 20mg daily, Aspirin 81mg daily",
    "Levothyroxine 50mcg daily",
    "Omeprazole 20mg daily, Amlodipine 5mg daily",
    "None reported",
    "Metoprolol 25mg twice daily, Furosemide 20mg daily",
    "Sertraline 50mg daily, Alprazolam 0.5mg as needed",
    "Insulin glargine 20 units nightly, Jardiance 10mg daily",
    "Prednisone 10mg daily, Hydroxychloroquine 200mg twice daily",
    "Ibuprofen 400mg as needed, Cetirizine 10mg daily"
]

ALLERGIES = [
    "Penicillin — rash and hives",
    "Sulfa drugs — anaphylaxis",
    "No known drug allergies",
    "Aspirin — GI bleeding",
    "Latex — contact dermatitis",
    "Codeine — nausea and vomiting",
    "Contrast dye — hives",
    "No known allergies",
    "Shellfish — anaphylaxis",
    "ACE inhibitors — angioedema"
]

MEDICAL_HISTORY = [
    "Hypertension, Type 2 Diabetes Mellitus",
    "Coronary Artery Disease, Hyperlipidemia",
    "Hypothyroidism",
    "GERD, Hypertension",
    "No significant medical history",
    "Congestive Heart Failure, Atrial Fibrillation",
    "Major Depressive Disorder, Generalized Anxiety Disorder",
    "Type 1 Diabetes Mellitus, Diabetic Neuropathy",
    "Systemic Lupus Erythematosus, Rheumatoid Arthritis",
    "Asthma, Seasonal Allergies"
]

SURGICAL_HISTORY = [
    "Appendectomy 2015, Cholecystectomy 2018",
    "CABG 2019",
    "None",
    "Cesarean section 2016, Tubal ligation 2020",
    "Knee replacement right 2021",
    "Tonsillectomy 2005",
    "Hysterectomy 2017",
    "None reported",
    "Spinal fusion L4-L5 2020",
    "Cataract surgery bilateral 2022"
]

FAMILY_HISTORY = [
    "Father — hypertension, mother — type 2 diabetes",
    "Father — myocardial infarction age 58, brother — hyperlipidemia",
    "No significant family history",
    "Mother — breast cancer, maternal aunt — ovarian cancer",
    "Father — COPD, mother — hypothyroidism",
    "Paternal grandfather — colon cancer, father — hypertension",
    "Mother — depression, sister — anxiety disorder",
    "Both parents — type 2 diabetes, sibling — obesity",
    "Mother — lupus, maternal grandmother — rheumatoid arthritis",
    "Father — asthma, mother — allergic rhinitis"
]

CARE_TEAMS = [
    "Dr. Sarah Chen, Internal Medicine",
    "Dr. Marcus Williams, Family Medicine",
    "Dr. Priya Patel, Cardiology",
    "Dr. James O'Brien, Emergency Medicine",
    "Dr. Lisa Nguyen, Hospitalist",
    "Dr. Robert Martinez, Pulmonology",
    "Dr. Amanda Foster, Neurology",
    "Dr. David Kim, Endocrinology",
    "Dr. Rachel Thompson, Oncology",
    "Dr. Michael Santos, Orthopedics"
]

LANGUAGES = [
    "English", "English", "English", "English", "English",
    "Spanish", "Spanish", "Mandarin", "Vietnamese", "Haitian Creole"
]

OPEN_FINDINGS = [
    "Pending cardiology consult for abnormal EKG findings",
    "Insurance pre-authorization required for MRI",
    "Social work consult needed for discharge planning",
    "Nutrition consult ordered for diabetic meal planning",
    "Physical therapy evaluation pending",
    "None",
    "None",
    "Infectious disease consult pending for fever workup",
    "Psychiatry consult ordered for mood assessment",
    "Follow up labs required within 48 hours"
]

REFERRAL_SOURCES = [
    "Primary Care Physician", "Emergency Department",
    "Specialist Referral", "Self-referral", "Urgent Care",
    "Transfer from outside facility", "Walk-in"
]

print("Generating patient IDs and base data...")
patient_ids = [f"P{str(i).zfill(6)}" for i in range(1, NUM_PATIENTS + 1)]

# ── File 1: Patient Demographics ──────────────────────────
print("Building PatientDemographics.xlsx...")

demographics = []
for pid in patient_ids:
    dob = fake.date_of_birth(minimum_age=18, maximum_age=95)
    age = (datetime.now().date() - dob).days // 365
    lang = random.choice(LANGUAGES)
    demographics.append({
        "PatientID":             pid,
        "FirstName":             fake.first_name(),
        "LastName":              fake.last_name(),
        "DateOfBirth":           dob.strftime("%m/%d/%Y"),
        "Age":                   age,
        "Gender":                random.choice(["Male", "Female", "Non-binary"]),
        "Address":               fake.address().replace("\n", ", "),
        "Phone":                 fake.phone_number(),
        "EmergencyContactName":  fake.name(),
        "EmergencyContactPhone": fake.phone_number(),
        "InsuranceProvider":     random.choice(INSURANCE_PROVIDERS),
        "InsurancePolicyNumber": fake.bothify(text="??#######"),
        "PrimaryCarePhysician":  f"Dr. {fake.last_name()}, {random.choice(['MD', 'DO'])}",
        "ReferralSource":        random.choice(REFERRAL_SOURCES),
        "AdmissionDate":         fake.date_between(start_date="-30d", end_date="today").strftime("%m/%d/%Y"),
        "LanguagePreference":    lang,
    })

df1 = pd.DataFrame(demographics)
df1.to_excel("PatientDemographics.xlsx", index=False)
print(f"  PatientDemographics.xlsx — {len(df1):,} rows written")

# ── File 2: Clinical Intake ───────────────────────────────
print("Building ClinicalIntake.xlsx...")

clinical = []
for pid in patient_ids:
    systolic  = random.randint(90, 180)
    diastolic = random.randint(60, 110)
    hr        = random.randint(55, 120)
    temp      = round(random.uniform(97.0, 103.0), 1)
    o2        = random.randint(88, 100)
    pain      = random.randint(0, 10)
    clinical.append({
        "PatientID":          pid,
        "ChiefComplaint":     random.choice(CHIEF_COMPLAINTS),
        "BloodPressure":      f"{systolic}/{diastolic} mmHg",
        "HeartRate":          f"{hr} bpm",
        "Temperature":        f"{temp} F",
        "OxygenSaturation":   f"{o2}%",
        "CurrentMedications": random.choice(MEDICATIONS),
        "KnownAllergies":     random.choice(ALLERGIES),
        "MedicalHistory":     random.choice(MEDICAL_HISTORY),
        "SurgicalHistory":    random.choice(SURGICAL_HISTORY),
        "FamilyHistory":      random.choice(FAMILY_HISTORY),
        "SmokingStatus":      random.choice(["Never", "Former", "Current — 10 pack years", "Current — 20 pack years"]),
        "AlcoholUse":         random.choice(["None", "Occasional", "Moderate", "Heavy"]),
        "PainScale":          f"{pain}/10",
        "FunctionalStatus":   random.choice(["Independent", "Requires minimal assistance", "Requires moderate assistance", "Dependent"])
    })

df2 = pd.DataFrame(clinical)
df2.to_excel("ClinicalIntake.xlsx", index=False)
print(f"  ClinicalIntake.xlsx — {len(df2):,} rows written")

# ── File 3: Administrative Flags ──────────────────────────
print("Building AdministrativeFlags.xlsx...")

admin = []
for i, pid in enumerate(patient_ids):
    fall_score   = random.randint(0, 15)
    fall_level   = "High" if fall_score >= 10 else ("Medium" if fall_score >= 5 else "Low")
    priority     = random.choice(["Critical", "High", "Medium", "Low"])
    lang         = demographics[i]["LanguagePreference"]
    interpreter  = "Yes" if lang != "English" else "No"
    admin.append({
        "PatientID":                  pid,
        "InsuranceVerificationStatus": random.choice(["Verified", "Pending", "Denied", "Partial"]),
        "ConsentFormsSigned":          random.choice(["Yes", "No", "Partial"]),
        "AdvanceDirectiveOnFile":      random.choice(["Yes", "No", "In progress"]),
        "SpecialAccommodationsNeeded": random.choice(["None", "Wheelchair access", "Hearing assistance", "Vision assistance", "Bariatric equipment"]),
        "LanguagePreference":          lang,
        "InterpreterRequired":         interpreter,
        "FallRiskScore":               fall_score,
        "FallRiskLevel":               fall_level,
        "PriorityLevel":               priority,
        "AssignedCareTeam":            random.choice(CARE_TEAMS),
        "OpenFindings":                random.choice(OPEN_FINDINGS),
        "IntakeCompletionStatus":      random.choice(["Complete", "In progress", "Pending review"]),
        "NotesForCareTeam":            random.choice([
            "Patient anxious about procedures. Requires additional reassurance.",
            "Family present and involved in care decisions.",
            "Patient prefers minimal intervention approach.",
            "Follow up with PCP required within one week of discharge.",
            "No additional notes.",
            "Patient has history of non-compliance with medication regimen.",
            "Interpreter services confirmed for all interactions.",
            "Patient is a healthcare worker — aware of diagnosis and prognosis.",
            "Advance directive reviewed with patient and family.",
            "Social determinants screening completed — no immediate concerns identified."
        ])
    })

df3 = pd.DataFrame(admin)
df3.to_excel("AdministrativeFlags.xlsx", index=False)
print(f"  AdministrativeFlags.xlsx — {len(df3):,} rows written")

print("\nAll three files generated successfully.")
print(f"Location: {__import__('os').path.abspath('.')}")
print("\nNext step: Upload these files to OneDrive.")