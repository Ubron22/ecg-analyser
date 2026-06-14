# ecg-analyser

A Python tool that reads and analyzes real ECG data to detect abnormal heart rhythms and generate clinical summaries.


## Description

This project analyzes real electrocardiogram (ECG) data from the PhysioNet PTB-XL database, which contains 21,799 clinical records from real patients. It classifies multilingual reports written in German, Swedish, and English into 7 cardiac conditions including myocardial infarction, atrial fibrillation, bradycardia, and tachycardia, and flags unclassified records. The program generates a statistical summary showing the count and percentage of each condition across the entire dataset.


## Features

- Reads and classifies multilingual ECG reports
- Identifies 7 cardiac conditions and flags unclassified records
- Generates percentage breakdown across all patients


## Data Source

This project uses the [PTB-XL ECG Database](https://physionet.org/content/ptb-xl/1.0.3/) from PhysioNet.


## Technologies

- Python 3
- CSV module


## What's Next

- Visualization of ECG signal
- Detection of specific arrhythmia patterns
- Comparison across multiple patients
