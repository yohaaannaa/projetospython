import random

def jogar_jogo(usuario_escolha):
    opcoes = ['pedra', 'papel', 'tesoura']
    ia_escolha = random.choice(opcoes)

    print(f"Você escolheu: {usuario_escolha}")
    print(f"O adversário escolheu: {ia_escolha}")

    if usuario_escolha == ia_escolha:
        print("Empate!")
    elif (usuario_escolha == 'pedra' and ia_escolha == 'tesoura') or \
         (usuario_escolha == 'papel' and ia_escolha == 'pedra') or \
         (usuario_escolha == 'tesoura' and ia_escolha == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

def main():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    print("Digite sua escolha (pedra, papel ou tesoura) ou 'sair' para encerrar o jogo.")

    while True:
        escolha = input("Escolha: ").lower()

        if escolha == 'sair':
            print("Obrigado por jogar!")
            break
        elif escolha in ['pedra', 'papel', 'tesoura']:
            jogar_jogo(escolha)
        else:
            print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")

if __name__ == "__main__":
    main()

