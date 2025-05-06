import Bot_Conselheiro
import Bot_Treinador
import Bot_Dialogo_Passado
import Bot_Mentor
import Bot_Quebrada
import Bot_EcoBot

def exibir_menu():
  print("\n🤖 Bem-vindo ao Centro de Chatbots!")
  print("Qual bot você deseja acessar?")
  print("1 - Conselheiro de Bairro")
  print("2 - Treinador de Fim de Semana")
  print("3 - Diálogo com o Passado")
  print("4 - Mentor para Iniciantes")
  print("5 - Bot da Quebrada")
  print("6 - EcoBot")
  print("0 - Sair")

def main():
  while True:
    exibir_menu()
    escolha = input("Digite o número do bot: ")
    if escolha == "1":
      Bot_Conselheiro.iniciar()
    elif escolha == "2":
      Bot_Treinador.iniciar()
    elif escolha == "3":
      Bot_Dialogo_Passado.iniciar()
    elif escolha == "4":
      Bot_Mentor.iniciar()
    elif escolha == "5":
      Bot_Quebrada.iniciar()
    elif escolha == "6":
      Bot_EcoBot.iniciar()
    elif escolha == "0":
      print("Encerrando... 👋")
      break
    else:
      print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()







    