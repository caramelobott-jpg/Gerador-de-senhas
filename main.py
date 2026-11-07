import random
senhas = []
def gerar_senha(tamanho):
    operação = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    senha = ""
    for i in range(tamanho):  
        print("Gerando senha...")
        senha += random.choice(operação)
    senhas.append(senha)
    print("Senhas geradas:", senhas)


gerar_senha(12)