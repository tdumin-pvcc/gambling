while input("Continue?: ") == "y":

    import random

    population = ['Keyboard', 'Monitor', 'Tower', "Joker"]
    weights = [0.3, 0.2, 0.1, 0.4]

    chosen = random.choices(population, weights, k=3)

    count = chosen.count('Keyboard')
    print('count of Keyboard:', count)
    count = chosen.count('Monitor')
    print('count of Monitor:', count)
    count = chosen.count('Tower')
    print('count of Tower:', count)
    count = chosen.count('Joker')

    if chosen.count('Keyboard') > 2:
        win=True
        print("win")
    else:
        if chosen.count('Monitor') > 1:
            win=True
            print("win")
        else:
            if chosen.count('Tower') > 1:
                win=True
                print("win")
            else:
                    win=False
                    print("lose")
