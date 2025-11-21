import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
from scipy.signal import welch

df = pd.read_csv(r"D:\New volume 1\sem 3\projects\Brake Shoes\raw_data.csv")

def random_process_analysis():
    temp = df['temp']

    # Autocorrelation
    autocorr = acf(temp, nlags=20)
    print("Autocorrelation:", autocorr)

    plt.plot(autocorr)
    plt.title("Autocorrelation of Temperature")
    plt.show()

    # Power Spectral Density (machine vibration)
    vib = df['vibration']
    freqs, psd = welch(vib)
    plt.plot(freqs, psd)
    plt.title("PSD of Vibration Signal")
    plt.show()

random_process_analysis()
