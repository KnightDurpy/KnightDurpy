from short1_thing import *

line_in = input()
hold_1 = foo(line_in)
print(hold_1)

line_in_2 = input()
line_in_3 = input()
hold_2 = bar(line_in, line_in_2, line_in_3)
print(hold_2)

print(baz(hold_1, hold_2))