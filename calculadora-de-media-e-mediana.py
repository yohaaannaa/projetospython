def calcular_media(lista):
    return sum(lista) / len(lista)

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)
    if tamanho % 2 == 0:
        mediana = (lista_ordenada[tamanho // 2 - 1] + lista_ordenada[tamanho // 2]) / 2
    else:
        mediana = lista_ordenada[tamanho // 2]
    return mediana

def main():
    print("Bem-vindo ao Calculador de Média e Mediana!")
    numeros = input("Digite uma lista de números separados por espaços: ").split()
    numeros = [float(num) for num in numeros]
    
    media = calcular_media(numeros)
    mediana = calcular_mediana(numeros)

    print("A média dos números é:", media)
    print("A mediana dos números é:", mediana)

if __name__ == "__main__":
    main()
