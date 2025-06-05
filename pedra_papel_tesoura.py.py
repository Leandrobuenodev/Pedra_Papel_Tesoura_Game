import random

user_points = 0 
computer_points = 0
options = ["r", "t", "p"]

while user_points < 2 and computer_points < 2:
    user = input("Escolha: | R(Pedra) | T(Tesoura) | P(Papel): ").lower()
    if user not in options:
        print("Inválido. Tente novamente.")
        continue

    pc = random.choice(options)
    print("Computador escolheu:", pc.upper())

    if user == pc:
        print("Empate!")
    elif (user == "r" and pc == "t") or (user == "t" and pc == "p") or (user == "p" and pc == "r"):
        print("Você venceu a rodada!")
        user_points += 1
    else:
        print("Computador venceu a rodada!")
        computer_points += 1

print("\nPlacar final - Você:", user_points, "| Computador:", computer_points)
print("Vitória!" if user_points > computer_points else "Derrota!")