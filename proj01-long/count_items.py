def data(line_holder):
    line_split = []
    for item in line_holder:
        line_split.append(item.split())

    line_dict = {}
    for i in line_split:
        key = i[0]
        value = int(i[-1])
        if key in line_dict.keys():
            line_dict[key] += value
        else:
            line_dict[key] = value

    key_sorted = []
    for key in sorted(line_dict.keys()):
        key_sorted.append(key)

    hold = [(v, k) for k, v in line_dict.items()]
    sort_hold = sorted(hold)

    step_1(key_sorted, line_dict)
    step_2(line_dict)
    step_3(sort_hold)
    step_4(sort_hold)

def step_1(key_sorted, line_dict):
    print('STEP 1: THE ORIGINAL DICTIONARY')
    for key in key_sorted:
        if key in line_dict:
            print('  Key: '+key,'Value: '+str(line_dict[key]))
    print()

def step_2(line_dict):
    holder = []
    print('STEP 2: A LIST OF VALUE->KEY TUPLES')
    for key in sorted(line_dict):
        holder.append((line_dict[key], key))
    print(holder)
    print()

def step_3(sort_hold):
    print('STEP 3: AFTER SORTING')
    print(sort_hold)
    print()

def step_4(sort_hold):
    print('STEP 4: THE ACTUAL OUTPUT')
    for pair in sort_hold:
        print(pair[1], pair[0])

def main():
    file_in = input('File to scan: ')
    file_open = open(file_in, 'r')
    file_lines = file_open.readlines()
    line_holder = []
    for line in file_lines:
        line = line.rstrip()
        if line == '':
            continue
        else:
            line_holder.append(line)
    data(line_holder)
    file_open.close()

main()

" test-count_items-01.in "