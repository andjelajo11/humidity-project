import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import periodogram





def compute_periodogram(time_series, sampling_rate):
    """
    Computes the periodogram for the specified time series.

    Parameters:
    time_series (array-like): The time series data.
    sampling_rate (float): The sampling rate of the time series.

    Returns:
    tuple: A tuple containing frequencies, power density, dominant frequency, and its magnitude.
    """
    if time_series.isnull().all() or len(time_series) == 0:
        print("Empty or all NaN time series")
        return np.array([]), np.array([]), None, None

    # Compute the periodogram
    frequencies, power_density = periodogram(time_series, fs=sampling_rate)

    if len(power_density) <= 1:
        print("Insufficient data in power density")
        return frequencies, power_density, None, None

    # Find the index of the dominant frequency
    dominant_frequency_index = np.argmax(power_density[1:]) + 1  # ignore the zero-frequency component
    dominant_frequency = frequencies[dominant_frequency_index]
    dominant_power = power_density[dominant_frequency_index]

    return frequencies, power_density, dominant_frequency, dominant_power




# Compute the periodogram for each moisture column



        
        
def plot_periodogram(column, periodograms):
    """
    Plots the periodogram for the specified column and marks the dominant frequency.

    Parameters:
    column (str): The name of the column to plot.
    periodograms (dict): A dictionary containing periodogram data with 'frequencies' and 'power_density'.
    """
    data = periodograms.get(column, None)
    if data is None:
        print(f"No data available for {column}")
        return

    frequencies = data.get('frequencies')
    power_density = data.get('power_density')
    dominant_frequency = data.get('dominant_frequency')
    dominant_power = data.get('dominant_power')

    if frequencies is None or power_density is None:
        print(f"No frequencies or power density data available for {column}")
        return

    if dominant_frequency is None or dominant_power is None:
        print(f"No dominant frequency or power data available for {column}")
        return

    plt.figure(figsize=(10, 6))
    plt.semilogy(frequencies, power_density, label='Power Density')
    plt.scatter(dominant_frequency, dominant_power, color='red', label=f'Dominant frequency: {dominant_frequency:.2f} Hz')
    plt.title(f'Periodogram of {column}')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Density')
    plt.legend()
    plt.show()


