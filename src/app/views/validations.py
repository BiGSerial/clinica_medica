import re
from datetime import datetime

def validar_inteiro(mensagem, nome_campo, tamanho=None):
    while True:
        valor = input(mensagem)
        try:
            inteiro = int(valor)
            if tamanho and len(valor) != tamanho:
                print(f"Entrada inválida: {nome_campo} deve ter {tamanho} dígitos.")
            else:
                return inteiro
        except ValueError:
            print(f"Entrada inválida: {nome_campo} deve ser um número inteiro.")

from datetime import datetime

def validar_data(mensagem):
    while True:
        data_str = input(mensagem)
        formatos_aceitos = ['%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d']
        
        for formato in formatos_aceitos:
            try:
                data = datetime.strptime(data_str, formato)
                # Convertendo a data para o formato YYYY-MM-DD
                return data.strftime('%Y-%m-%d')
            except ValueError:
                continue  # Tenta o próximo formato
        
        print("Data inválida. Use um dos seguintes formatos: DD/MM/YYYY, MM/DD/YYYY, YYYY-MM-DD.")


def validar_email(mensagem):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        email = input(mensagem)
        if re.match(regex, email):
            return email
        else:
            print("Email inválido.")
