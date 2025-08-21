import time

from tamagoshi import Tamagoshi, Dragao, Hipogrifo, Camaleao


def main():
    print("Bem-vindo ao Tamagoshi!")
    print("\nEscolha o tipo do seu bichinho:\n1 - Dragão\n2 - Hipogrifo\n3 - Camaleão\n")
    escolha = input("Insira o número do seu bichinho: ")
    nome = input("Digite o nome do seu bichinho: ")
    

    if escolha == "1":
        bicho = Dragao(nome)
    elif escolha == "2":
        bicho = Hipogrifo(nome)
    elif escolha == "3":
        bicho = Camaleao(nome)
    else:
        print("Opção inválida, criando um Tamagoshi padrão.")
        bicho = Tamagoshi(nome)

    while True:
        bicho.mostrar_status()
        print("\nO que deseja fazer?")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Dormir")
        if isinstance(bicho, Dragao):
            print("4 - Cuspir fogo")
            print("5 - Rugir")
            print("6 - Voar alto")
        elif isinstance(bicho, Hipogrifo):
            print("4 - Voar")
            print("5 - Planar")
            print("6 - Gritar")
        elif isinstance(bicho, Camaleao):
            print("4 - Camuflar")
            print("5 - Se esconder")
            print("6 - Relaxar")
        print("7 - Dormir")
        print("8 - Mostrar histórico")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            quantidade = input("Digite a quantidade de comida (0 a 100): ")
            bicho.alimentar(quantidade)
        elif opcao == "2":
            bicho.brincar()
        elif opcao == "3":
            bicho.dormir()
        elif opcao in ["4", "5", "6"]:
            if isinstance(bicho, Dragao):
                if opcao == "4":
                    bicho.cuspir_fogo()
                elif opcao == "5":
                    bicho.rugir()
                elif opcao == "6":
                    bicho.voar_alto()
            elif isinstance(bicho, Hipogrifo):
                if opcao == "4":
                    bicho.voar()
                elif opcao == "5":
                    bicho.planar()
                elif opcao == "6":
                    bicho.gritar()
            elif isinstance(bicho, Camaleao):
                if opcao == "4":
                    bicho.camuflar()
                elif opcao == "5":
                    bicho.se_esconder()
                elif opcao == "6":
                    bicho.relaxar()
        elif opcao == "7":
            bicho.mostrar_historico()
        elif opcao == "0":
            print("Saindo do jogo. Até mais!")
            break
        else:
            print("Opção inválida!")

        bicho.passar_tempo()
        time.sleep(1)

if __name__ == "__main__":
    main()
