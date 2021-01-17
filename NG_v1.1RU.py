HP = 15
AP = 15
WP = 15

HO = 15
AO = 15
WO = 15

kolv = 0

money = 0
ten = 10
dwad = 20
sorok = 40

one = 1
five = 5
br = 1
while br == 1:
    vopr = input("бой, раунды, магазин, счёт, выйти, игрок: ") 

    if kolv == 2:
        HO+=five
        AO+=five
        WO+=five
    if vopr == "бой":
        if HP >= HO and AP >= AO and WP >= WO: 
            print("вы выиграли.")
            money+=ten
            kolv+=one 
        else:
            print("вы проиграли.")    
    elif vopr == "выйти":
        br = 0
    elif vopr == "магазин":
        print("\n(a1)Броня+10 = 20₽\n(h1)Здоровье+10 = 20₽\n(w1)Оружие+10 = 20₽\n(a2)Броня+20 = 40₽\n(h2)Здоровье+20 = 40₽\n(w2)Оружие+20 = 40₽\n")
        varik = input("Выберите улучшение: ")
        if varik == "a1" and money == 20:
            AP+=ten
            money-=dwad
            print("Успешно.")
        elif varik == "h1" and money == 20:
            HP+=ten
            money-=dwad
            print("Успешно.")
        elif varik == "w1" and money == 20:
            WP+=ten
            money-=dwad
            print("Успешно.")
        elif varik == "a2" and money == 40:
            AP+=dwad
            money-=sorok
            print("Успешно.")
        elif varik == "р2" and money == 40:
            HP+=dwad
            money-=sorok
            print("Успешно.")
        elif varik == "w2" and money == 40:
            WP+=dwad
            money-=sorok
            print("Не достаточно денег.")
        elif varik == "a1" and money <= 20:
            print("Не достаточно денег.")
        elif varik == "h1" and money <= 20:
            print("Не достаточно денег.")
        elif varik == "w1" and money <= 20:
            print("Не достаточно денег.")
        elif varik == "a2" and money <= 40:
            print("Не достаточно денег.")
        elif varik == "р2" and money <= 40:
            print("Не достаточно денег.")
        elif varik == "w2" and money <= 40:
            print("Не достаточно денег.")  
        else:
            print("Я не понимаю. Повоторите запрос.")
    elif vopr == "счёт":
        print(money)
    elif vopr == "игрок":
        print('\n'+"Здоровье = "+str(HP)+'\n'+"Броня = "+str(AP)+'\n'+"Оружие = "+str(WP)+'\n')
    elif vopr == "раунды":
        print(kolv) 
    else:
        print("Я не понимаю. Повоторите запрос.")
    