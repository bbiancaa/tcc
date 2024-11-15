#pip install numpy scipy matplotlib librosa
import numpy as np
import librosa
import matplotlib.pyplot as plt

# Função para realizar a FFT e extrair frequências dominantes
def analisar_audio(audio_path):
    # Carregar o áudio
    y, sr = librosa.load(audio_path, sr=None)  # sr=None mantém a taxa de amostragem original

    # Realizar a Transformada de Fourier (FFT)
    fft_result = np.fft.fft(y)
    
    # Obter o espectro de magnitudes
    fft_magnitude = np.abs(fft_result)
    
    # Obter as frequências correspondentes a cada ponto da FFT
    frequencies = np.fft.fftfreq(len(y), 1/sr)
    
    # Considerar apenas as frequências positivas
    positive_freqs = frequencies[:len(frequencies)//2]
    positive_magnitude = fft_magnitude[:len(fft_magnitude)//2]

    # Identificar as 5 frequências dominantes (maiores magnitudes)
    top_frequencies_idx = np.argsort(positive_magnitude)[-5:][::-1]
    top_frequencies = positive_freqs[top_frequencies_idx]
    top_magnitudes = positive_magnitude[top_frequencies_idx]

    # Exibir as 5 frequências dominantes
    print("Frequências dominantes (Hz):")
    for i, (freq, mag) in enumerate(zip(top_frequencies, top_magnitudes)):
        print(f"{i + 1}. {freq:.2f} Hz com magnitude {mag:.2f}")
    
    # Plotar o espectro de frequências
    plt.figure(figsize=(10, 6))
    plt.plot(positive_freqs, positive_magnitude)
    plt.title("Espectro de Frequências")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.show()

# Caminho do arquivo de áudio (substitua pelo seu arquivo de áudio)
audio_path = 'seu_arquivo_de_audio.wav'

# Analisar o áudio
analisar_audio(audio_path)
