import random

# computador escolhe um número aleatório entre 0 e 100
numero_secreto = random.randint(0, 100)

tentativa = None

while tentativa != numero_secreto:
    tentativa = int(input("Tente adivinhar o número (0 a 100): "))

    if tentativa < numero_secreto:
        print("O número é maior!")
    elif tentativa > numero_secreto:
        print("O número é menor!")
    else:
        print("Parabéns! Você acertou 🎉")
    