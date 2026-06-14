## ECG Analyser

Two complementary tools for working with the PhysioNet PTB-XL dataset:

ECG Report Classifier — processes the clinical text reports: classifies multilingual diagnostic statements into cardiac conditions across the whole dataset.
ECG Signal Analyser — processes the raw ECG waveform: detects heartbeats, computes heart rate, and classifies the rhythm.

Together they cover both layers of the data: the signal itself and the written interpretation of it.


# 1. ECG Report Classifier

A Python tool that analysis and classifies ECG dataset.


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



## 2. ECG Signal Analyser

A rule-based tool that reads real ECG recordings from PTB-XL, detects heartbeats (R peaks) directly from the raw waveform, computes the heart rate, classifies the rhythm.


## What it does

- Loads a single lead of a real ECG record by streaming it directly from PhysioNet (no full dataset download required).
- Detects R peaks using a transparent rule-based method: a point counts as a heartbeat if it is above a height threshold and is a local maximum, with a refractory period after each detection so a single beat is never counted twice.
- Computes heart rate from the intervals between consecutive R peaks (RR intervals).
- Classifies the rhythm as normal, bradycardia (slow), tachycardia (fast), or irregular.
- Visualises the waveform with each detected R peak marked in red.


## Usage

```bash
pip install wfdb numpy matplotlib
python ECG_analyser_visualiser.py
```
You will be prompted for a patient ID (1–21799). The program prints the number of beats, the average heart rate, and the rhythm classification, then displays the annotated ECG plot.

## Technologies

- Python 3
- wfdb — reads PhysioNet waveform records
- NumPy — signal arrays and numerical operations
- Matplotlib — plotting

  
## Limitations

The height threshold is a single global value (half the signal's maximum), so a very tall spike can raise the threshold enough that lower-amplitude real beats are missed.
The irregularity check uses the spread between the longest and shortest RR interval, which is sensitive to a single outlier beat.


## Possible improvements

- An adaptive or local threshold for R-peak detection rather than a single global one.
- A more robust irregularity metric.
- Comparison of detected heart rate against multiple patients.
