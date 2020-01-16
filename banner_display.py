def seven_seg(num):
    num = str(num)
    if not num.isdigit():
        raise TypeError("Not a number")
    def switch(i):
        digit_dict = {'0': [" _ ","| |","|_|"], '1': ["   ","  |","  |"],
                      '2': [" _ "," _|","|_ "], '3': [" _ "," _|"," _|"],
                      '4': ["   ","|_|","  |"], '5': [" _ ","|_ "," _|"],
                      '6': [" _ ","|_ ","|_|"], '7': [" _ ","  |","  |"],
                      '8': [" _ ","|_|","|_|"], '9': [" _ ","|_|"," _|"]}
        return digit_dict.get(i)
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

def cust_banner(text):
    text = str(text); final = ''
    def switch(i):
        if not i.isdigit():
            char_dict = {'A': ["    "," _  ","/_\\ ","| | "], 'B': ["    ","▊▚  ","▊■  ","▊▞  "],
                         'C': ["    ","▞▀  ","▉    ","▚▄  "], 'D': ["    ","▊▚ ","▊ ■ ","▊▞ "],
                         'E': ["    ","█▀▀ ","█■■ ","█▄▄ "], 'F': ["     ","█▀▀ ","█■■ ","█   "],
                         'G': ["    ","▞▘   ","▉ ▜  ","▚▞   "], 'H': ["     ","█ █ ","█■█ ","█ █ "],
                         'I': ["    ","▜▛  "," █  ","▟▙ "], 'J': ["     ","▄▄▄ ","  ▐  ","▚▞  "],
                         'K': ["    ","▉▞  ","▉    ","▉▚  "], 'L': ["     ","█   ","█   ","█▄▄ "],
                         'M': [" __  __  ","|  \\/  | ","| |\\/| | ","|_|  |_| "],
                         'N': [" _   _  ","|  \\| | ","| |\\  | ","|_| \\_| "],
                         'O': ["     ","▞▀▚ ","▌  ▐ ","▚▄▞ "], 'P': ["     ","█▘▚ ","█▖▞ ","█    "],
                         'Q': ["    ","▞▀▚ ","▌  ▐ ","▚▞▚ "], 'R': ["     ","█▀▚  ","█▄▞  ","█▝▚ "],
                         'S': ["    ","▛▀▀ ","▙▄▄ ","▄▄▟ "], 'T': ["     ","▀█▀ "," █  "," █  "],
                         'U': ["    ","▌ ▐ ","▌ ▐ ","▙▟ "], 'V': ["     ","▌ ▐ ","▌ ▐ ","▚▞ "],
                         'W': ["__      __  ","\\ \\ /\\ / / "," \\ V  V /  ","  \\_/\\_/   "],
                         'X': ["    ","▚ ▞ "," ▞▖ ","▞ ▚ "], 'Y': [" __ __ "," \\ V /  ","  | |   ","  |_|   "],
                         'Z': [" _____  ","|_   /  ","  / /_  "," /____| "]}
            return char_dict.get(i)
    for c in range(len(text)):
        layer1 = switch(text[c])[0]
        final += layer1
    final += '\n'
    for c in range(len(text)): #Second pass
        layer2 = switch(text[c])[1]
        final += layer2
    final += '\n'
    for c in range(len(text)): #Third pass
        layer3 = switch(text[c])[2]
        final += layer3
    final += '\n'
    for c in range(len(text)): #Fourth pass
        layer4 = switch(text[c])[3]
        final += layer4
    final += '\n'
    return final

inp = str(input("Enter a word: "))
print(cust_banner(inp))
