def main():
    str_input = input('input string: ')
    print(len(str_input))
    print(str_input[1])
    print(str_input[:10])
    print(str_input[-5:])
    print(str_input.upper())

    if (str_input[0].upper() in 'QWERTY'):
        print('QWERTY')
    elif (str_input[0] in 'uiop'):  
        print('UIOP')
    elif (str_input[0].isalpha()):
        print('LETTER')
    elif (str_input[0] in '1234567890'):
        print('DIGIT')
    else:
        print('OTHER')

    int_0 = input()
    int_1 = input()
    print(int(int_0) * int(int_1))

main()

' test-strings_and_input-01.stdin '