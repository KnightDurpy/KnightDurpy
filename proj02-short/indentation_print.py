def space_counter(line):
    counter = 0
    for space in range(0, len(line)):
        if line[space] == ' ':
            counter += 1
        if line[space].isalpha():
            break
    return counter

input_holder = []
while True:
    temp_holder = []
    line_in = input()
    temp_holder.append(line_in)
    if 'quit' in temp_holder[-1]:
        break
    input_holder.append(line_in)


for line in input_holder:
    print(space_counter(line))