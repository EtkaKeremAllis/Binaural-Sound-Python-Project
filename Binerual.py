import numpy as np
import sounddevice as sd
import tkinter as tk

pencere = tk.Tk()
pencere.title("Stereo Sound Player")
pencere.geometry("400x300")  # Daha kompakt

fs = 44100

# --- SÜRE ---
frame1 = tk.Frame(pencere)
frame1.pack(pady=10)
label1 = tk.Label(frame1, text="Time (seconds):")
label1.pack(side="left", padx=5)
entry1 = tk.Entry(frame1, width=10)
entry1.pack(side="left")

# --- SOL FREKANSLAR ---
frame2 = tk.Frame(pencere)
frame2.pack(pady=10)
label2 = tk.Label(frame2, text="Left Frequence(Hz):")
label2.pack(side="left", padx=5)
entry2 = tk.Entry(frame2, width=10)
entry2.pack(side="left")

# --- SAĞ FREKANSLAR ---
frame3 = tk.Frame(pencere)
frame3.pack(pady=10)
label3 = tk.Label(frame3, text="Right Frequence (Hz):")
label3.pack(side="left", padx=5)
entry3 = tk.Entry(frame3, width=10)
entry3.pack(side="left")

# --- Sonuç / Hata Label ---
result_label = tk.Label(pencere, text="", fg="red")
result_label.pack(pady=10)

# --- Fonksiyonlar ---
def frekans1():
    try:
        return float(entry2.get())
    except ValueError:
        result_label.config(text="Please insert left frequence ")
        return None

def frekans2():
    try:
        return float(entry3.get())
    except ValueError:
        result_label.config(text="Please insert right frequence")
        return None

def süreyi_hesapla():
    try:
        return float(entry1.get())
    except ValueError:
        result_label.config(text="Please insert numbers")
        return None

def buton_komut():
    f1 = frekans1()
    f2 = frekans2()
    s = süreyi_hesapla()
    if f1 is not None and f2 is not None and s is not None:
        t = np.linspace(0, s, int(fs*s), endpoint=False)
        sol_ses = 0.6 * np.sin(2*np.pi*f1*t)
        sag_ses = 0.6 * np.sin(2*np.pi*f2*t)
        wave_stereo = np.column_stack((sol_ses, sag_ses))
        sd.play(wave_stereo, samplerate=fs)
        sd.wait()

# --- Buton ---
button = tk.Button(pencere, text="Play", command=buton_komut, width=15)
button.pack(pady=15)

pencere.mainloop()