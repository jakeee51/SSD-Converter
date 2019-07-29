def seven_seg(num):
    digit_dict = {'0': [" _ ","| |","|_|"], '1': ["   ","  |","  |"],
                  '2': [" _ "," _|","|_ "], '3': [" _ "," _|"," _|"],
                  '4': ["   ","|_|","  |"], '5': []}
    SSD = []
    layer1 = []
    layer2 = []
    layer3 = []
    for d in num:
        if d == '0':
            SSD.append(" _ \n| | \n|_| ")

    return " _  _ \n _| _|\n|_  _|\n"

print(seven_seg('0'))
