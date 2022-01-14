import sys

def  descending_sequence(num_list):
    checker = None
    counter = 1
    for num in num_list:
        # print(num)
        if checker == None:
            checker = num
        else:
            if num <= checker:
                counter += 1
                checker = num
            else:
                return counter
    return counter

def  ascending_sequence(num_list):
    checker = None
    counter = 1
    for num in num_list:
        # print(num)
        if checker == None:
            checker = num
        else:
            if num >= checker:
                counter += 1
                checker = num
            else:
                return counter
    return counter

def main():
    num_list = []
    for line in sys.stdin:
        line = line.split()
        for num in line:
            num_list.append(int(num))

    # up or down check
    checker = None
    for num in num_list:
        if checker == None:
            checker = num
        if checker == num:
            continue
        else:
            if num < checker:
                hold_0 = descending_sequence(num_list)
                print(hold_0)
                break
            if num > checker:
                hold_1 = ascending_sequence(num_list)
                print(hold_1)
                break

main()

' test-sequence_len-01.stdin '