import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Função para calcular a Transformada de Fourier e encontrar a frequência dominante
def frequencia_dominante(arquivo_audio):
    # Carregar o arquivo de áudio
    taxa_amostragem, sinal = wav.read(arquivo_audio)
    
    # Se o áudio for estéreo, converte para mono tirando a média entre os canais
    if len(sinal.shape) > 1:
        sinal = np.mean(sinal, axis=1)
    
    # Calcular a Transformada de Fourier
    N = len(sinal)
    fft_resultado = np.fft.fft(sinal)
    
    # Calcular a magnitude do espectro (parte real e imaginária)
    magnitudes = np.abs(fft_resultado)[:N//2]
    
    # Calcular as frequências correspondentes
    frequencias = np.fft.fftfreq(N, 1/taxa_amostragem)[:N//2]
    
    # Encontrar a frequência dominante
    indice_maximo = np.argmax(magnitudes)
    frequencia_dominante = frequencias[indice_maximo]
    
    return frequencia_dominante, frequencias, magnitudes

# Exemplo de uso com um arquivo de áudio
arquivo_audio = 'seu_arquivo_audio.wav'  # Substitua pelo caminho do seu arquivo WAV
frequencia, frequencias, magnitudes = frequencia_dominante(arquivo_audio)

# Exibir a frequência dominante
print(f"A frequência dominante é: {frequencia} Hz")

# Plotar o espectro de frequências
plt.figure(figsize=(10, 6))
plt.plot(frequencias, magnitudes)
plt.title("Espectro de Frequências")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, 5000)  # Limitar o eixo x para mostrar frequências mais relevantes
plt.grid(True)
plt.show()

#pip install numpy scipy matplotlib
