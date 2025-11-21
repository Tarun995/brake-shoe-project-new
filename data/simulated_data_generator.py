import numpy as np
import pandas as pd

def generate_data(n=1000):
    # Simulate production parameters
    temp = np.random.normal(200, 20, n)          # Temperature
    pressure = np.random.normal(100, 15, n)      # Pressure
    cycle_time = np.random.normal(40, 5, n)      # Cycle time
    vibration = np.random.normal(5, 1.5, n)      # Vibration
    humidity = np.random.normal(50, 10, n)       # Humidity

    # Defect depends on extreme values
    defect = (
        (temp > 230).astype(int) +
        (pressure > 120).astype(int) +
        (cycle_time > 48).astype(int) +
        (vibration > 7).astype(int)
    )

    # convert to 0 or 1
    defect = (defect > 1).astype(int)

    df = pd.DataFrame({
        'temp': temp,
        'pressure': pressure,
        'cycle_time': cycle_time,
        'vibration': vibration,
        'humidity': humidity,
        'defect': defect
    })

    df.to_csv("raw_data.csv", index=False)
    print("Dataset created → raw_data.csv")

generate_data()
