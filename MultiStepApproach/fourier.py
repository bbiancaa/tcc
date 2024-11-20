import numpy as np
import matplotlib.pyplot as plt
import librosa

# Carregar o arquivo de áudio
audio_path = 'utils/audio.wav'
y, sr = librosa.load(audio_path, sr=None)

# Aplicar FFT
n = len(y)
frequencies = np.fft.fftfreq(n, 1/sr)
fft_values = np.fft.fft(y)

# Obter as magnitudes da FFT (somente as frequências positivas)
fft_magnitude = np.abs(fft_values[:n//2])
frequencies = frequencies[:n//2]

# Identificar a frequência dominante
dominant_frequency = frequencies[np.argmax(fft_magnitude)]
print(f'Frequência dominante: {dominant_frequency} Hz')

# Plotar o gráfico da FFT
plt.figure(figsize=(10, 6))
plt.plot(frequencies, fft_magnitude)
plt.title('Transformada de Fourier - Análise de Frequência')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()
