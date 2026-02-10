from database.database import get_driver
from repository.friend import add_friend


def main():
    with get_driver() as driver:
        x = input("Digite 'x' para entrar ou 'sair' para encerrar: ")

        while x.lower() != "sair":
            print("Digite o nome de uma pessoa:")
            pessoa1 = input()

            print("Digite o nome do amigo dessa pessoa:")
            pessoa2 = input()

            add_friend(driver, pessoa1, pessoa2)
            print("Amizade cadastrada com sucesso!\n")

            x = input("Digite 'sair' para encerrar ou ENTER para continuar: ")


if __name__ == "__main__":
    main()
