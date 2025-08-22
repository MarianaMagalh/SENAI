import time

from tamagoshi import Tamagoshi
from filhos import Dragao, Hipogrifo, Camaleao

def main():
    print("""
   __   __   ____  ____  __  _  _    ____  __ _   ___   __   __ _  ____  __   ____   __  
 _(  ) / _\ (  _ \(    \(  )( \/ )  (  __)(  ( \ / __) / _\ (  ( \(_  _)/ _\ (    \ /  \ 
/ \) \/    \ )   / ) D ( )( / \/ \   ) _) /    /( (__ /    \/    /  )( /    \ ) D ((  O )
\____/\_/\_/(__\_)(____/(__)\_)(_/  (____)\_)__) \___)\_/\_/\_)__) (__)\_/\_/(____/ \__/           
""")
    
    print("Bem-vinde ao Jardim Encantado!!")
    print("Escolha o tipo no seu novo filho:\n[ 1 ] - Dragão\n[ 2 ] - Hipogrifo\n[ 3 ] - Camaleão")
    print("OBS: Caso vc não escolha nada, o seu filho será um Tamagoshi normal")
    
    escolha = input("Insira o número do seu novo filho: ")
    nome = input("Digite o nome do seu filho: ")
    
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
        bicho.mostraHistorico()
        
        print("""
  __      __   _  _  ____     __   _  _  ____  ____    ____  __   ____  ____  ____  ___  \n
 /  \    /  \ / )( \(  __)   /  \ / )( \(  __)(  _ \  (  __)/ _\ (__  )(  __)(  _ \(__ \ \n
(  O )  (  O )) \/ ( ) _)   (  O )) \/ ( ) _)  )   /   ) _)/    \ / _/  ) _)  )   / (__/ \n
 \__/    \__\)\____/(____)   \__\)\____/(____)(__\_)  (__) \_/\_/(____)(____)(__\_) (_)  \n
                             """)    
        
        print("[ 1 ] - Alimentar")
        print("[ 2 ] - Brincar")
        print("[ 3 ] - Dormir")
        if isinstance(bicho, Dragao):
            print("[ 4 ] - Cuspir Fogo")
            print("[ 5 ] - Rugir")
            print("[ 6 ] - Voar Alto")
        elif isinstance(bicho, Hipogrifo):
            print("[ 4 ] - Voar")
            print("[ 5 ] - Planar")
            print("[ 6 ] - Cumprimentar")
        elif isinstance(bicho, Camaleao):
            print("[ 4 ] - Camuflar")
            print("[ 5 ] - Pegar Inseto")
            print("[ 6 ] - Esconder")
        print("[ 7 ] - Mostrar Historico")
        print("[ 0 ] - Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            quantidade = input(f"Insira a quantidade de comida que vc quer dar a {nome}")
            bicho.alimentar(quantidade)
        elif opcao == "2":
            bicho.brincar()
        elif opcao == "3":
            bicho.dormir()
        elif opcao in ["4", "5", "6"]:
            if isinstance(bicho, Dragao):
                if opcao == "4":
                    bicho.cuspirFogo()
                elif opcao == "5":
                    bicho.rugir()
                elif opcao == "6":
                    bicho.voarAlto()
            elif isinstance(bicho, Hipogrifo):
                if opcao == "4":
                    bicho.voar()
                elif opcao == "5":
                    bicho.planar()
                elif opcao == "6":
                    bicho.cumprimentar()
            elif isinstance(bicho, Camaleao):
                if opcao == "4":
                    bicho.camuflar()
                elif opcao == "5":
                    bicho.pegarInseto
                elif opcao == "6":
                    bicho.esconder()
        elif opcao == "7":
            bicho.mostraHistorico()
        elif opcao == "0":
            print("Você está saindo...")
            print("""
                     ____  ___  _  _   __   _  _ \n
                    (_  _)/ __)/ )( \ / _\ / )( \\n
                      )( ( (__ ) __ (/    \) \/ (\n
                     (__) \___)\_)(_/\_/\_/\____/\n
                  """)
        else:
            print("Opção inválida!")
        
        bicho.passarTempo()
        time.sleep(1)
        
        
if __name__ == "__main__":
    main()
        