import re
from datetime import datetime

def validar_inteiro(nome_campo, tamanho=None):
    while True:
        valor = input(f"Digite o valor para {nome_campo}: ")
        # Verifica se o valor é numérico antes de tentar converter para int
        if not valor.isdigit():
            print(f"Entrada inválida: {nome_campo} deve ser um número inteiro.")
            continue

        if tamanho and len(valor) != tamanho:
            print(f"Entrada inválida: {nome_campo} deve ter {tamanho} dígitos.")
            continue
        
        return int(valor)
    
def validar_texto(nome_campo, tamanho_min=None, tamanho_max=None):
    while True:
        texto = input(f"Digite o valor para {nome_campo}: ")
        
        if tamanho_min and len(texto) < tamanho_min:
            print(f"Entrada inválida: {nome_campo} deve ter pelo menos {tamanho_min} caracteres.")
            continue
        
        if tamanho_max and len(texto) > tamanho_max:
            print(f"Entrada inválida: {nome_campo} deve ter no máximo {tamanho_max} caracteres.")
            continue
        
        return str(texto)

def validar_data(mensagem):
    formatos_aceitos = ['%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d']
    
    while True:
        data_str = input(mensagem)
        
        for formato in formatos_aceitos:
            try:
                data = datetime.strptime(data_str, formato)
                # Retornando a data como um objeto datetime.date
                return data.date()
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
            print("Email inválido. Tente novamente.")
