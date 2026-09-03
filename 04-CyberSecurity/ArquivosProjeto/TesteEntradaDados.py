import random

def jogar():
    print("=" * 40)
    print("  BEM-VINDO AO JOGO DA ADIVINHAÇÃO!  ")
    print("=" * 40)
    print("Tente adivinhar o número secreto entre 1 e 100.\n")

    # 1. O computador escolhe o número secreto
    numero_secreto = random.randint(1, 100)
    
    tentativas = 0
    acertou = False

    # 2. Laço principal do jogo
    while not acertou:
        # Pega o palpite do jogador
        entrada = input("Digite o seu palpite (ou 'sair' para encerrar): ")

        # Permite ao jogador desistir
        if entrada.lower() == 'sair':
            print(f"\nJogo encerrado. O número secreto era {numero_secreto}.")
            break

        # Valida se a entrada é um número
        if not entrada.isdigit():
            print("Por favor, digite um número inteiro válido!\n")
            continue

        palpite = int(entrada)
        tentativas += 1

        # 3. Verificação do palpite
        if palpite == numero_secreto:
            acertou = True
            print("\n" + "*" * 40)
            print(f" PARABÉNS! Você acertou em {tentativas} tentativa(s)!")
            print("*" * 40)
        elif palpite < numero_secreto:
            print(" Dica: O número secreto é MAIOR. Tente novamente!\n")
        else:
            print(" Dica: O número secreto é MENOR. Tente novamente!\n")

# Executa o jogo
if __name__ == "__main__":
    jogar()

