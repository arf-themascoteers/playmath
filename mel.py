import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("dataset_min.csv").to_numpy()
plt.plot(data[0])
plt.plot(data[1])
plt.show()

sr = 4200

mel_spectrogram = librosa.feature.melspectrogram(y=data[0], sr=sr)
mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)

librosa.display.specshow(mel_spectrogram_db, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.show()

mel_spectrogram = librosa.feature.melspectrogram(y=data[1], sr=sr)
mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)

librosa.display.specshow(mel_spectrogram_db, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.show()
