import sys
""" This is a test.
This is only a test.
 """

lines = []
for line in sys.stdin:
    line = line.split()
    lines.append(line)

line_1 = lines[0]
line_2 = lines[1]
print('The first line was: '+str(line_1))
print('The second line was: '+str(line_2))

line_1_and_2 = line_1 + line_2
print()
print('The combination of both lines had '+str(len(line_1_and_2))+' words.')
print('The combined set of words was: '+str(line_1_and_2))

print()
print('After sorting, the words were: '+str(sorted(line_1_and_2)))
print()

print('Pairs:')
walker = 0
for list_1, list_2 in zip(line_1, line_2):
    print(str(walker)+': '+str(list_1)+', '+str(list_2))
    walker += 1

' two_lines_of_words-02.stdin '