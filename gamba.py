import random
start=(input("Press enter to start"))
points=100
while(points>6):

    points=points-10
    population = ['Keyboard', 'Monitor', 'Tower', "Joker"]
    weights = [0.2, 0.2, .05, 0.55]

    chosen = random.choices(population, weights, k=3)

    count = chosen.count('Keyboard')
    print('count of Keyboard:', count)
    count = chosen.count('Monitor')
    print('count of Monitor:', count)
    count = chosen.count('Tower')
    print('count of Tower:', count)
    count = chosen.count('Joker')
    print('count of Joker:', count)

    if chosen.count('Keyboard') == 2:
        print("Win. Would you like to play again? y/n")
        points=points+25
        print(points)
    elif chosen.count('Monitor') == 2:
        print("Win. Would you like to play again? y/n")
        points=points+40
        print(points)
    elif chosen.count('Tower') == 2:
        print("Win. Would you like to play again? y/n")
        points=points+60
        print(points)
    elif chosen.count('Keyboard') > 2:
        print("Win. Would you like to play again? y/n")
        points=points+100
        print(points)
    elif chosen.count('Monitor') > 2:
        print("Win. Would you like to play again? y/n")
        points=points+160
        print(points)
    elif chosen.count('Tower') > 2:
        print("Win. Would you like to play again? y/n")
        points=points+240
        print(points)

    else:
        print("Lose. Would you like to play again? y/n")
        print(points)
    ans=input()
    if ans == 'y':
        print('Good. Your win comes soon.')
     
        print(points)
    elif ans == 'n':
        print("90% of gamblers quit before their big win.")
        print(points)
        break
    else:
        print('Good. Your win comes soon.') and ans =='y'
       
