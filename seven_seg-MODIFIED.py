def switch(i):
    digit_dict = {'0': [" _ ",
                        "| |",
                        "|_|"],
                  '1': ["   ",
                        "  |",
                        "  |"],
                  '2': [" _ ",
                        " _|",
                        "|_ "],
                  '3': [" _ ",
                        " _|",
                        " _|"],
                  '4': ["   ",
                        "|_|",
                        "  |"],
                  '5': [" _ ",
                        "|_ ",
                        " _|"],
                  '6': [" _ ",
                        "|_ ",
                        "|_|"],
                  '7': [" _ ",
                        "  |",
                        "  |"],
                  '8': [" _ ",
                        "|_|",
                        "|_|"],
                  '9': [" _ ",
                        "|_|",
                        " _|"]}
    return digit_dict.get(i)

def seven_seg(num):
    num = str(num)
    if not num.isdigit():
        raise TypeError("Not a number")

    SSD = ""
    for d in range(len(num)): #First pass
        layer1 = switch(num[d])[0]
        SSD += layer1
    SSD += '\n'
    for d in range(len(num)): #Second pass
        layer2 = switch(num[d])[1]
        SSD += layer2
    SSD += '\n'
    for d in range(len(num)): #Third pass
        layer3 = switch(num[d])[2]
        SSD += layer3
    SSD += '\n'
    return SSD

print(seven_seg("152"))
