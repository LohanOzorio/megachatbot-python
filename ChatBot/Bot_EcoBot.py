nome = input("Olá, ecoguardiã(o)! Qual seu nome? ")
print(f"Bem-vindo(a), {nome}! 🌱 Vamos conversar sobre sustentabilidade?")

tema = input("Você quer dicas sobre:\n1 - Reciclagem\n2 - Energia limpa\n3 - Consumo consciente\nDigite o número: ")
if tema == "1":
    print("Separe o lixo seco do úmido, e leve recicláveis a cooperativas locais!")
elif tema == "2":
    print("Que tal instalar painéis solares ou usar lâmpadas LED?")
elif tema == "3":
    print("Evite compras por impulso. Reflita antes de consumir. 😉")
else:
    print("Tema não reconhecido, tente novamente.")