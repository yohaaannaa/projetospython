import random as r

def simular_lancamento():
    return r.randint(1, 6)

def main():
    print("Bem-vindo à simulação de lançamento de dado!")
    while True:
        input("Pressione Enter para lançar o dado...")
        resultado = simular_lancamento()
        print(f"O resultado do lançamento é: {resultado}")
        continuar = input("Deseja lançar o dado novamente? (s/n): ")
        if continuar.lower() != 's':
            print("Obrigado por usar nosso simulador!")
            break

if __name__ == "__main__":
    main()
