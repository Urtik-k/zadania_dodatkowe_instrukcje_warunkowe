

x = int(input("Podaj liczbe początkowa: "))
chain_length = 1


while x < 1 or x > 100:

        x = int(input("Podaj liczbe w poprawnym zakresie! (1-100): "))

while x != 1:


    if x % 2 == 0:
        x //= 2
        chain_length += 1
    else:
        x = x * 3 + 1
        chain_length += 1

print(f"Długość ciągu Collatza twojej liczby to : {chain_length}")

