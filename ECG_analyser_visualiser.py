
import wfdb
import numpy as np
 
def load_ecg(record_name, pn_dir, lead=1):
    record = wfdb.rdrecord(record_name, pn_dir=pn_dir)
    signal = record.p_signal[:, lead]
    return signal, record.fs

def detect_r_peaks(signal, fs):
    threshold = 0.5 * np.max(signal)
    refractory_period = int(0.3 * fs)         
 
    peaks = []
    i = 1
    while i < len(signal) - 1:
        taller = signal[i] > threshold
        higher = signal[i] > signal[i - 1] and signal[i] >= signal[i + 1]
        if taller and higher:
            peaks.append(i)
            i += refractory_period
        else:
            i += 1
    return np.array(peaks)
 

def analyse_ecg(signal, fs):
    result = {}
    peaks = detect_r_peaks(signal, fs)

    if len(peaks) < 2:
        return {"n_beats": len(peaks), "avg_bpm": None,
                "rhythm": "not enough beats detected"}
 
    rr_seconds = np.diff(peaks) / fs 
    bpm = 60 / rr_seconds               
    avg_bpm = float(np.mean(bpm))       
 
    spread = float(np.max(rr_seconds) - np.min(rr_seconds))
    if spread > 0.15:
        rhythm = "irregular rhythm"
    elif avg_bpm < 60:
        rhythm = "bradycardia (slow)"
    elif avg_bpm > 100:
        rhythm = "tachycardia (fast)"
    else:
        rhythm = "normal rhythm"
    result = {"n_beats": len(peaks), "avg_bpm": round(avg_bpm, 1), "rhythm": rhythm}
    print("Beats detected:   ", result["n_beats"])
    print("Average heart rate:", result["avg_bpm"], "bpm")
    print("Classification:   ", result["rhythm"])
    return result

def visualise_ecg(signal, fs, peaks=None):
    import matplotlib.pyplot as plt
    time = np.arange(len(signal)) / fs
    plt.figure(figsize=(12, 4))
    plt.plot(time, signal, label="ECG Signal")
    if peaks is not None:
        plt.plot(peaks / fs, signal[peaks], 'ro', label="R-peaks")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("ECG Signal")
    plt.legend()
    plt.grid()
    plt.show()

def analyse_patient(patient_id):
    folder = f"{(patient_id//1000)* 1000:05d}"
    record = f"{patient_id:05d}_hr"
    signal, fs = load_ecg(record, pn_dir=f"ptb-xl/1.0.3/records500/{folder}")
    visualise_ecg(signal, fs, peaks=detect_r_peaks(signal, fs))
    final_result = analyse_ecg(signal, fs)
    return final_result

if __name__ == "__main__":
    raw = input("Enter patient ID: ")
    try:
        x = int(raw)
    except ValueError:
        print(f"'{raw}' is not a number. Please enter a patient ID like 5 or 19000.")
    else:
        if 0 < x <= 21799:
            analyse_patient(x)
        else:
            print(f"'{x}' is not a valid patient ID. Please enter a patient ID between 1 and 21799.")
