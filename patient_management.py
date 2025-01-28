def search_patients_by_disease(patients, disease):
    """Return a list of patient names with a specific disease."""
    return [patient["Name"] for patient in patients if patient["Disease"] == disease]


# Example usage
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
print("Patients with Flu:", search_patients_by_disease(patients, "Flu"))
