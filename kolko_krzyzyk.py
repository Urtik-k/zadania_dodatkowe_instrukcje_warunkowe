

#wersja na milionie ifów bez list

box1 = box2 = box3 = box4 = box5 = box6 = box7 = box8 = box9 = "-"


print("witaj w programie kółko i krzyżyk! /// aka milion ifów ")


#numeracja pól dla gracza

print(" 1  2  3 ")
print(" 4  5  6 ")
print(" 7  8  9 ")


while True:

    print("Ruch CPU!")

    #sprawdzanie czy jest opcja wygranej

    #159

    if box5 == "X" and box9 == "X" and box1 == "-" :
        box1 = "X"
    elif box5 == "X" and box1 == "X" and box9 == "-" :
        box9 = "X"

    #456

    elif box5 == "X" and box4 == "X" and box6 == "-" :
        box6 = "X"
    elif box5 == "X" and box6 == "X" and box4 == "-" :
        box4 = "X"

    #753

    elif box5 == "X" and box7 == "X" and box3 == "-" :
        box3 = "X"
    elif box5 == "X" and box3 == "X" and box7 == "-" :
        box7 = "X"

    #258

    elif box5 == "X" and box2 == "X" and box8 == "-" :
        box8 = "X"
    elif box5 == "X" and box8 == "X" and box2 == "-" :
        box2 = "X"


    #blokowanie gracza przed wygrana
    else :

        # 123

        if box1 == box2 == "O" and box3 == "-":
            box3 = "X"
        elif box2 == box3 == "O" and box1 == "-":
            box1 = "X"
        elif box1 == box3 == "O" and box2 == "-":
            box2 = "X"

        # 789

        elif box7 == box8 == "O" and box9 == "-":
            box9 = "X"
        elif box8 == box9 == "O" and box7 == "-":
            box7 = "X"
        elif box7 == box9 == "O" and box8 == "-":
            box8 = "X"

        # 147

        elif box1 == box4 == "O" and box7 == "-":
            box7 = "X"
        elif box4 == box7 == "O" and box1 == "-":
            box1 = "X"
        elif box1 == box7 == "O" and box4 == "-":
            box4 = "X"

        # 369

        elif box3 == box6 == "O" and box9 == "-":
            box9 = "X"
        elif box6 == box9 == "O" and box3 == "-":
            box3 = "X"
        elif box3 == box9 == "O" and box6 == "-":
            box6 = "X"


        # jeśli nie trzeba blokować  wykonaj ruch
        else:

            if box5 == "-":
                box5 = "X"
            elif box1 == "-":
                box1 = "X"
            elif box3 == "-":
                box3 = "X"
            elif box7 == "-":
                box7 = "X"
            elif box9 == "-":
                box9 = "X"
            elif box2 == "-":
                box2 = "X"
            elif box4 == "-":
                box4 = "X"
            elif box6 == "-":
                box6 = "X"
            elif box8 == "-":
                box8 = "X"

    # drukowanie planszy i sprawdzenie stanu gry

    print(box1 + " " + box2 + " " + box3 + " ")
    print(box4 + " " + box5 + " " + box6 + " ")
    print(box7 + " " + box8 + " " + box9 + " ")

    if box5 == box1 == box9 == "X" or box5 == box4 == box6 == "X" or box5 == box7 == box3 == "X" or box5 == box8 == box2 == "X":
        print("Przegrana!")
        break
    elif box1 != "-" and box2 != "-" and box3 != "-" and box4 != "-" and box5 != "-" and box6 != "-" and box7 != "-" and box8 != "-" and box9 != "-":
        print("Remis!")
        break

    # ruch gracza

    move_valid = 0
    while move_valid == 0:
        player_input = int(input("wpisz numer pola do postawienia kółka:  "))

        if player_input == 1 and box1 == "-" :
            box1 = "O"
            move_valid = 1
        elif player_input == 2 and box2 == "-" :
            box2 = "O"
            move_valid = 1
        elif player_input == 3 and box3 == "-" :
            box3 = "O"
            move_valid = 1
        elif player_input == 4 and box4 == "-" :
            box4 = "O"
            move_valid = 1
        elif player_input == 5 and box5 == "-" :
            box5 = "O"
            move_valid = 1
        elif player_input == 6 and box6 == "-" :
            box6 = "O"
            move_valid = 1
        elif player_input == 7 and box7 == "-" :
            box7 = "O"
            move_valid = 1
        elif player_input == 8 and box8 == "-" :
            box8 = "O"
            move_valid = 1
        elif player_input == 9 and box9 == "-" :
            box9 = "O"
            move_valid = 1
        else:
            print("Błąd! wpisz poprawne pole!")

    print(box1 + " " + box2 + " " + box3 + " ")
    print(box4 + " " + box5 + " " + box6 + " ")
    print(box7 + " " + box8 + " " + box9 + " ")
    print()


    # sprawdzenie stanu gry

    if box5 == box1 == box9 == "X" or box5 == box4 == box6 == "X" or box5 == box7 == box3 == "X" or box5 == box8 == box2 == "X":
        print("Wygrało CPU!")
        break
    elif box1 != "-" and box2 != "-" and box3 != "-" and box4 != "-" and box5 != "-" and box6 != "-" and box7 != "-" and box8 != "-" and box9 != "-":
        print("Remis!")
        break

