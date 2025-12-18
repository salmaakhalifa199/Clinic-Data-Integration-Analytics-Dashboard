import pandas as pd
import random
from datetime import datetime, timedelta
import openpyxl
import numpy as np

# توليد تاريخ عشوائي
def generate_random_date():
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    date = start_date + timedelta(days=random_days)
    if random.choice([True, False]):
        return date.strftime('%d/%m/%Y')  
    else:
        return f"{date.day}/{date.strftime('%m/%Y')}"


# توليد اسم مريض عشوائي حسب الجنس
def random_name_gender():
    male_first_names = ['John', 'Mike', 'Chris', 'Tom']
    female_first_names = ['Jane', 'Anna', 'Sara', 'Laura']
    last_names = ['Smith', 'Doe', 'Johnson', 'Williams', 'Brown', 'Jones', 'Davis']

    gender = random.choices(['Male', 'Female'], weights=[45, 55])[0]
    if gender == 'Male':
        name = f"{random.choice(male_first_names)} {random.choice(last_names)}"
    else:
        name = f"{random.choice(female_first_names)} {random.choice(last_names)}"
    return name, gender

# العلاقات المنطقية بين التشخيص والعلاج والوصفة والتحاليل
diagnosis_map = {
    'Flu': {
        'weight': 30,
        'treatment': 'Medication',
        'prescription': ['Antibiotics', 'Painkillers'],
        'lab_results': ['Normal', 'Elevated'],
        'age_range': (5, 60)
    },
    'Diabetes': {
        'weight': 20,
        'treatment': 'Therapy',
        'prescription': ['Insulin'],
        'lab_results': ['Elevated', 'Critical'],
        'age_range': (30, 80)
    },
    'Hypertension': {
        'weight': 25,
        'treatment': 'Medication',
        'prescription': ['Painkillers'],
        'lab_results': ['Elevated', 'Critical'],
        'age_range': (35, 85)
    },
    'Asthma': {
        'weight': 10,
        'treatment': 'Medication',
        'prescription': ['Inhaler'],
        'lab_results': ['Normal', 'Critical'],
        'age_range': (10, 60)
    },
    'COVID-19': {
        'weight': 15,
        'treatment': 'Observation',
        'prescription': ['None', 'Antibiotics'],
        'lab_results': ['Elevated', 'Critical'],
        'age_range': (15, 75)
    }
}

diagnosis_choices = list(diagnosis_map.keys())
diagnosis_weights = [diagnosis_map[d]['weight'] for d in diagnosis_choices]

doctors = ['Dr. Smith', 'Dr. Lee', 'Dr. Patel', 'Dr. Carter']

# توليد البيانات
def generate_clinic_data(n_rows=100000):
    data = {
        "id": [],
        "date": [],
        "patient_name": [],
        "age": [],
        "gender": [],
        "diagnosis": [],
        "treatment": [],
        "doctor": [],
        "visit_cost": [],
        "lab_results": [],
        "prescription": [],
    }

    for _ in range(n_rows):
        date = generate_random_date()
        name, gender = random_name_gender()
        diagnosis = random.choices(diagnosis_choices, weights=diagnosis_weights)[0]
        details = diagnosis_map[diagnosis]
        treatment = details['treatment']
        prescription = random.choice(details['prescription'])
        lab_result = random.choice(details['lab_results'])
        age = random.randint(*details['age_range'])

        treatment_cost_map = {
            'Medication': (100, 250),
            'Therapy': (200, 400),
            'Surgery': (400, 600),
            'Observation': (50, 150),
        }
        cost_range = treatment_cost_map.get(treatment, (100, 300))
        cost = round(random.uniform(*cost_range), 2)

        data["id"].append(str(random.randint(10**9, 10**10 - 1)))
        data["date"].append(date)
        data["patient_name"].append(name)
        data["age"].append(age)
        data["gender"].append(gender)
        data["diagnosis"].append(diagnosis)
        data["treatment"].append(treatment)
        data["doctor"].append(random.choice(doctors))
        data["visit_cost"].append(cost)
        data["lab_results"].append(lab_result)
        data["prescription"].append(prescription)

    return pd.DataFrame(data)

# توليد البيانات
df = generate_clinic_data()

# تقسيم البيانات إلى 3 أجزاء
split_dfs = np.array_split(df, 3)

# حفظ كل جزء في ملف مختلف
split_dfs[0].to_csv("clinic_data22.csv", index=False)
split_dfs[1].to_csv("clinic_data33.txt", sep='\t', index=False)
split_dfs[2].to_excel("clinic_data11.xlsx", index=False)

print("✔️ تم إنشاء الملفات مقسمة:\n- clinic_data2.csv\n- clinic_data3.txt\n- clinic_data1.xlsx")
