HP = 15
AP = 15
WP = 15

HO = 15
AO = 15
WO = 15

kolv = 0

money = 0
b = 10
c = 20
b = 40
chis = 1
chiss = 5
br = 1
while br == 1:
    vopr = input("fight, rounds, shop, money, exit, player: ") 

    if kolv == 2:
        HO+=chiss
        AO+=chiss
        WO+=chiss
    if vopr == "fight":
        if HP >= HO and AP >= AO and WP >= WO: 
            print("win")
            money+=b
            kolv+=chis
        else:
            print("lose")
            kolv+=chis    
    elif vopr == "exit":
        br = 0
    elif vopr == "shop":
        print("\n(a1)Armor+10 = 20₽\n(h1)heatlh+10 = 20₽\n(w1)weapon+10 = 20₽\n(a2)Armor+20 = 40₽\n(h2)heatlh+20 = 40₽\n(w2)weapon+20 = 40₽\n")
        varik = input("Choose update: ")
        if varik == "a1" and money == 20:
            AP+=b
            money-=c
            print("All ok.")
        elif varik == "h1" and money == 20:
            HP+=b
            money-=c
            print("All ok.")
        elif varik == "w1" and money == 20:
            WP+=b
            money-=c
            print("All ok.")
        elif varik == "a2" and money == 40:
            AP+=c
            money-=b
            print("All ok.")
        elif varik == "р2" and money == 40:
            HP+=c
            money-=b
            print("All ok.")
        elif varik == "w2" and money == 40:
            WP+=c
            money-=b
            print("Not enough money.")
        elif varik == "a1" and money <= 20:
            print("Not enough money.")
        elif varik == "h1" and money <= 20:
            print("Not enough money.")
        elif varik == "w1" and money <= 20:
            print("Not enough money.")
        elif varik == "a2" and money <= 40:
            print("Not enough money.")
        elif varik == "р2" and money <= 40:
            print("Not enough money.")
        elif varik == "w2" and money <= 40:
            print("Not enough money.")  
        else:
            print("i`m don`t understand")
    elif vopr == "money":
        print(money)
    elif vopr == "player":
        print('\n'+"Heatlh = "+str(HP)+'\n'+"Armor = "+str(AP)+'\n'+"Weapon = "+str(WP)+'\n')
    elif vopr == "rounds":
        print(kolv) 
    else:
        print("i`m don`t understand. ")
    