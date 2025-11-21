import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\New volume 1\sem 3\projects\Brake Shoes\raw_data.csv")

def probability_analysis():
    # Probability of defect
    p_defect = df['defect'].mean()
    print("P(Defect) =", round(p_defect, 3))

    # PDF of temperature
    mu = df['temp'].mean()
    sigma = df['temp'].std()
    
    print("Temperature Mean:", mu)
    print("Temperature Std Dev:", sigma)

    # Plot PDF
    plt.hist(df['temp'], bins=30, density=True)
    plt.title("Temperature Distribution (PDF)")
    plt.show()

    # Bayes Rule: P(Defect | Temp > 220)
    high_temp = df[df.temp > 220]
    bayes_prob = len(high_temp[high_temp.defect == 1]) / len(high_temp)
    
    print("P(Defect | Temp > 220) =", round(bayes_prob, 3))

probability_analysis()
