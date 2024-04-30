import matplotlib.pyplot as plt

def gerar_grafico():
    # Dados de exemplo
    categorias = ['A', 'B', 'C', 'D', 'E']
    valores = [23, 45, 56, 78, 33]

    # Gerar o gráfico de barras
    plt.bar(categorias, valores, color='skyblue')
    plt.xlabel('Categorias')
    plt.ylabel('Valores')
    plt.title('Gráfico de Barras')
    plt.show()

if __name__ == "__main__":
    gerar_grafico()
