class PostoSaude:
    def __init__(self, nome, endereco, absorventes_disponiveis):
        self.nome = nome
        self.endereco = endereco
        self.absorventes_disponiveis = absorventes_disponiveis

    def fazer_doacao(self, quantidade):
        self.absorventes_disponiveis += quantidade
        print(f"Você doou {quantidade} absorventes para o posto de saúde {self.nome}. Obrigado por sua generosidade!")

# Lista de postos de saúde em Curitiba
postos_saude_curitiba = [
    PostoSaude("Posto de Saúde X", "Endereço X", 100),
    PostoSaude("Posto de Saúde Y", "Endereço Y", 50),
    PostoSaude("Posto de Saúde Z", "Endereço Z", 75)
]

def menu_principal():
    print("Bem-vindo ao programa de doações de absorventes em postos de saúde de Curitiba!")
    print("Selecione uma opção:")
    print("1. Ver postos de saúde próximos")
    print("2. Fazer uma doação")
    print("3. Sair")

def listar_postos_saude():
    print("Postos de saúde em Curitiba:")
    for i, posto in enumerate(postos_saude_curitiba, 1):
        print(f"{i}. {posto.nome} - {posto.endereco} - Absorventes disponíveis: {posto.absorventes_disponiveis}")

def fazer_doacao():
    listar_postos_saude()
    escolha_posto = int(input("Escolha o posto de saúde para fazer a doação: "))
    quantidade_doacao = int(input("Digite a quantidade de absorventes que deseja doar: "))
    posto_escolhido = postos_saude_curitiba[escolha_posto - 1]
    posto_escolhido.fazer_doacao(quantidade_doacao)

def main():
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            listar_postos_saude()
        elif opcao == '2':
            fazer_doacao()
        elif opcao == '3':
            print("Obrigado por usar o programa de doações. Volte sempre!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
