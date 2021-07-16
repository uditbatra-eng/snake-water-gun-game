from random import choice
n = 1
l1 = ["snake", "water", "gun"]
cp = 0
p1 = 0
chance = 10
while n < 11:
    a = choice(l1)
    b = input("enter your choice ")
    if a == "snake":
        if b == "snake" or b == "SNAKE":
            print(f"In {a} vs {b}  no one wins")
            print("tie")
            n += 1
        
        elif b == "water" or b == "WATER":
            print(f"In {a} vs {b}  {a} wins ")
            cp += 1
            print(f"computer score {cp} your score {p1}")
            n += 1
        else:
            print(f"In {a} vs {b}  {b} wins")
            p1 += 1
            print(f"computer score {cp} your score {p1}")
            n += 1
    if a == "water":
        if b == "snake" or b == "SNAKE":
             print(f"In {a} vs {b}  {b} wins ")
             p1 += 1
             print(f"computer score {cp} your score {p1}")
             n += 1
        elif b == "water" or b == "WATER":
            print(f"In {a} vs {b} no one wins")
            print("tie")
            n += 1
            
        else:
            print(f"In {a} vs {b}  {a} wins")
            cp += 1
            print(f"computer score {cp} your score {p1}")
            n += 1
    if a == "gun":
        if b == "snake" or b == "SNAKE":
             print(f"In {a} vs {b}  {a} wins ")
             cp += 1
             print(f"computer score {cp} your score {p1}")
             n += 1
        elif b == "water" or b == "WATER":
            print(f"In {a} vs {b}  {b} wins")
            p1 += 1
            print(f"computer score {cp} your score {p1}")
            n += 1
        else:
            print(f"In {a} vs {b} no one wins")
            n += 1
    chance -= 1
    print(f"Number of chances left {chance}")

print(f"your score {p1} and computer score {cp}")
