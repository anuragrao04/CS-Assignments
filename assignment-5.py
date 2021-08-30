### Write a Python Program to convert decimal numbers to octal numbers using
### user- defined function Convert(), function takes two arguments decimal number
### and base. If base is missing function should convert decimal number to binary.






def Convert(given_num, base = 2):
    octal_num = [0]
    num_of_octal_char = 0
    while (given_num != 0):
        octal_num.append(given_num % base)
        given_num = int(given_num / base)
        num_of_octal_char += 1



    for i in range(num_of_octal_char, 0, -1):
        list_of_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        if octal_num[i] >= 10: octal_num[i] = list_of_alphabets[octal_num[i]-10]        
        print(octal_num[i], end = "")

    print()



given_num = int(input("Enter Decimal Number To Convert: "))
base = input("Enter Base To Convert To (Default = 2): ")
if base == '': 
    Convert(given_num)

else:
    base = int(base)
    Convert(given_num, base)








