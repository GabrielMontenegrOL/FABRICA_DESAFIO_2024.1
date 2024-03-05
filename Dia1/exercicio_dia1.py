#01) programa que pergunta a idade de uma pessoa e imprime na tela.
def idade(anos):
    return(anos)

def print_idade():
    anos = int(input("Digite sua idade: "))
    resultado = idade(anos)
    print("Sua idade é:", resultado)

#02) Some a média de 5 alunos e faça a média aritmética entre eles.
def media_aritmetrica(media1, media2, media3, media4, media5):
    return((media1 + media2 +  media3 +  media4 + media5) / 5)

def final_media():
    media1 = float(input("Digite a media: "))
    media2 = float(input("Digite a media: "))
    media3 = float(input("Digite a media: "))
    media4 = float(input("Digite a media: "))
    media5 = float(input("Digite a media: "))
    resultado = media_aritmetrica(media1, media2, media3, media4, media5)

    print(resultado)

#03) Programa que fale o nome de cinco times de futebol.
def cinco_times():
    times = ["Flamengo", "Bota-fogo", "Vasco da gama", "Time da fabrica", "Clube Atlético Albion"]
    print(times)

#04) Programa que calcule a maioridade de uma pessoa.
def mais18(ano_nascimento):
    return(ano_nascimento)

def mostrar_maioridade():
    ano_nascimento = int(input("Digite de ano nascimento: "))
    resultado = (2024 -ano_nascimento)
    
    if resultado >= 18:
        print("Você é de maior, tem:", resultado, "anos." )
    else:
        print("De menor, tem: ", resultado, "anos.")
    
#05) Pegunta o número e informa se é impar ou par.
def par_ou_impar(numero):
    return(numero)

def verficar_par_impar():
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")

#06) Programa para dizer se o número é primo ou não.
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def verificar_primo():
    num = int(input("Digite um número para verificar se é primo: "))
    if eh_primo(num):
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")

#Exibir painel inicial
while True:
    print("\nEscolha o serviço:")
    print("1. Programa para mostrar idade.")
    print("2. Media aritimetrica.")
    print("3. Mostrar 5 times.")
    print("4. Mostrar Maioridade.")
    print("5. Impar ou par.")
    print("6. Dizer se o número é primo ou não.")
    print("7. Sair.")

#Comando para executar o painel. 
    escolha = input("Digite o número do serviço desejado: ")
    
    if escolha == '1':
        print_idade()
    elif escolha == '2':
        final_media()
    elif escolha == '3':
        cinco_times()
    elif escolha == '4':
        mostrar_maioridade()
    elif escolha == '5':
        verficar_par_impar()
    elif escolha == '6':
        verificar_primo()
    elif escolha == '7':
        print("See you next time")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
