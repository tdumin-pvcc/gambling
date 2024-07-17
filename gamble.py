import random
while True:
    population = ['Keyboard', 'Monitor', 'Tower', "Joker"]
    weights = [0.3, 0.2, 0.01, 0.4]

    chosen = random.choices(population, weights, k=3)

    count = chosen.count('Keyboard')
    print('count of Keyboard:', count)
    count = chosen.count('Monitor')
    print('count of Monitor:', count)
    count = chosen.count('Tower')
    print('count of Tower:', count)
    count = chosen.count('Joker')
    print('count of Joker:', count)

    if chosen.count('Keyboard') > 1:
        print("win")
    else:
        if chosen.count('Monitor') > 1:
            print("win")
        else:
            if chosen.count('Tower') > 1:
                print("win")
            else:
               print("Lose. Would you like to play again? y/n")
    ans=input()
    if ans != 'y':
        break
