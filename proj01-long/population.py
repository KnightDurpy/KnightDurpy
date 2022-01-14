def population_print(file_lines):
    line_split = []
    for line in file_lines:
        if line[0] == "#" or len(line) == 1:
            continue
        else:
            line = line.rstrip()
            line_split.append(line.split())
    population_list = []
    for i in line_split:
        if len(i) > 1:
            population_list.append(i[-1])

    location_list = []
    for i in line_split:
        location_list.append(i[:-1])

    for loca, popu in zip(location_list, population_list):
        print('State/Territory:', *loca, sep = ' ')
        print('Population:      '+popu)
        print()

    num_places = len(location_list)
    total_pop = 0
    for i in population_list:
        total_pop += int(i)

    print('# of States/Territories: '+str(num_places))
    print('Total Population:        '+str(total_pop))

def main():
    input_in = input('file: ')
    file_open = open(input_in, 'r')
    file_lines = file_open.readlines()
    population_print(file_lines)
    file_open.close()

main()

' test-population-01.in '