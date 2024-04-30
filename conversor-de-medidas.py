# Função para converter metros para centímetros
def metros_para_centimetros(metros):
    return metros * 100

# Função para converter centímetros para metros
def centimetros_para_metros(centimetros):
    return centimetros / 100

# Função principal do programa
def main():
    print("Bem-vindo ao Conversor de Medidas!")
    print("Escolha a conversão que deseja fazer:")
    print("1. Converter metros para centímetros")
    print("2. Converter centímetros para metros")

    # Loop para garantir uma escolha válida
    while True:
        escolha = input("Digite 1 ou 2: ")
        if escolha in ['1', '2']:
            break
        else:
            print("Escolha inválida. Por favor, digite 1 ou 2.")

    # Conversão de metros para centímetros
    if escolha == '1':
        metros = float(input("Digite a medida em metros: "))
        centimetros = metros_para_centimetros(metros)
        print(f"{metros} metros equivalem a {centimetros} centímetros.")

    # Conversão de centímetros para metros
    elif escolha == '2':
        centimetros = float(input("Digite a medida em centímetros: "))
        metros = centimetros_para_metros(centimetros)
        print(f"{centimetros} centímetros equivalem a {metros} metros.")

if __name__ == "__main__":
    main()
