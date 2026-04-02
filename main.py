

def classify_report(report):
    translations = {
        "vorhofflimmern": "Atrial Fibrillation",
        "sinusbradykardie": "Bradycardia",
        "tachy": "Tachycardia",
        "infarkt": "Myocardial Infarction",
        "myokardschaden": "Myocardial Damage",
        "sinusrhythmus": "Normal",
        "abnormal":  "Abnormal",
        "förmaksflimmer": "Atrial Fibrillation",
        "sinusbradykardi": "Bradycardia",
        "takykardi": "Tachycardia",
        "infarkt": "Myocardial Infarction",
        "myokardskada": "Myocardial Damage",
        "normal": "Normal",
        "avvikande": "Abnormal",
        "ischaemia": "Ischaemia"}
    report = report.lower()
    for keyword in translations:
        if keyword in report:
            c = translations[keyword]
            return c
    return "Unclassified"
    
def analyse_dataset():
    dataset = {}
    dataset["Total patients analysed"] = ""
    dataset["Normal"] = 0
    dataset["Bradycardia"] = 0
    dataset["Tachycardia"] = 0
    dataset["Atrial Fibrillation"] = 0
    dataset["Myocardial Infarction"] = 0
    dataset["Myocardial Damage"] = 0
    dataset["Abnormal"] = 0
    dataset["Unclassified"] = 0       
    with open("ptbxl_database.csv") as new_file:
        dataset["Total patients analysed"] = len(new_file.readlines()) - 1
    with open("ptbxl_database.csv") as new_file:    
        for line in new_file:
            line = line.split(',')
            if line[10] == "report":
                continue
            if classify_report(line[10]) in dataset:
                dataset[classify_report(line[10])] += 1
            else:
                dataset["Unclassified"] += 1

    print("(=== ECG DATASET ANALYSIS ===)")
    for key in dataset:
        if key == "Total patients analysed":
            print(f"{key}: {dataset[key]}")
        else:
            print(f"{key}: {dataset[key]} ({dataset[key]/dataset['Total patients analysed']*100:.2f}%)")
    
    
if __name__ == "__main__":
    analyse_dataset()
