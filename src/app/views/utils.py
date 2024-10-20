import os
import time

def refresh():
    time.sleep(1)  # Simula um pequeno delay para transição suave
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela (Windows ou Linux/Mac)
