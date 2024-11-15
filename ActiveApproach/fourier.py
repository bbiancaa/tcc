#pip install numpy scipy matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Função para carregar o arquivo de áudio e realizar a transformada de Fourier
def analisar_audio(filtro_arquivo):
    # Carregar o arquivo de áudio (.wav)
    taxa_amostragem, sinal = wavfile.read(filtro_arquivo)
    
    # Caso o sinal tenha mais de um canal (estéreo), usar apenas um canal (mono)
    if len(sinal.shape) > 1:
        sinal = sinal[:, 0]  # Usando apenas o primeiro canal
    
    # Normalizar o sinal para o intervalo [-1, 1]
    sinal_normalizado = sinal / np.max(np.abs(sinal))
    
    # Aplicar a Transformada de Fourier
    sinal_fft = np.fft.fft(sinal_normalizado)
    
    # Obter as frequências correspondentes aos valores do FFT
    n = len(sinal_normalizado)
    frequencias = np.fft.fftfreq(n, d=1/taxa_amostragem)
    
    # Obter as magnitudes das frequências
    magnitudes = np.abs(sinal_fft)
    
    # Remover a parte negativa das frequências
    idx_positivas = np.where(frequencias >= 0)
    frequencias_positivas = frequencias[idx_positivas]
    magnitudes_positivas = magnitudes[idx_positivas]
    
    # Identificar a frequência dominante (maior pico de magnitude)
    freq_dominante = frequencias_positivas[np.argmax(magnitudes_positivas)]
    
    # Exibir o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(frequencias_positivas, magnitudes_positivas)
    plt.title("Espectro de Frequências do Áudio")
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.show()
    
    print(f"A frequência dominante é: {freq_dominante:.2f} Hz")

# Caminho para o arquivo de áudio
arquivo_audio = "seu_arquivo_audio.wav"

# Analisar o áudio e mostrar a frequência dominante
analisar_audio(arquivo_audio)
