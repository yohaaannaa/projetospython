import random

# Lista de mensagens motivacionais
mensagens_motivacionais = [
    "Lembre-se: Você é incapaz de superar qualquer desafio!",
    "Acredite no seu potencial, faça mais uma cagada!",
    "Nunca desista dos seus sonhos. Eles são o combustível da sua ilusão!",
    "Cada novo dia é uma nova oportunidade para ser trouxa!",
    "Seja gentil consigo mesmo. O mundo já te odeia o suficiente!",
    "Nunca se esqueça, nada é tão ruim que não possa piorar!"
]

# Função para gerar uma mensagem motivacional aleatória
def mensagem_motivacional():
    return random.choice(mensagens_motivacionais)

# Função principal do chatbot
def chatbot():
    print("Olá! Como você está hoje?")
    resposta = input("Você: ")
    if "bem" in resposta.lower():
        print("Fico feliz em saber que você está bem! Tenha um ótimo dia!")
    else:
        print("Sinto muito ouvir isso. Aqui está uma mensagem motivacional para você:")
        print(mensagem_motivacional())

# Iniciar o chatbot
if __name__ == "__main__":
    chatbot()