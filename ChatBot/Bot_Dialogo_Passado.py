nome = input("Qual seu nome, visitante do tempo? ")
print(f"{nome}, vamos embarcar numa viagem com o passado... prepare-se!")

resposta = input("Você deseja saber sobre a história de Recife? (s/n): ")
if resposta.lower() == "s":
    print("Recife é uma das mais antigas cidades do Brasil, cheia de cultura e resistência!")
else:
    print("Tudo bem! O passado sempre estará por aqui, esperando por você.")