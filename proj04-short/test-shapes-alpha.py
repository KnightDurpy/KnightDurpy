#! /usr/bin/python3

import shapes



# The tests will use this set to detect unexpected aliasing.  Some aliasing is
# expected and required, of course - but spurious aliasing is always an error!

ids = set()



def test_alpha():
    print("Testing shape_alpha()")

    val = shapes.shape_alpha()

    print(f"shape_alpha() returned: {val}")

    if len(val) != 4:
        print("ERROR: Invalid contents")
        return

    if val[0] != [10,20]:
        print("ERROR: Invalid contents")
        return

    if val[1] != 30:
        print("ERROR: Invalid contents")
        return

    if val[2] != 40:
        print("ERROR: Invalid contents")
        return

    if val[3] != [50,60]:
        print("ERROR: Invalid contents")
        return

    print("OK - the shape appears to be correct")




data = [10, None, 20, ["foo", None, "baz"], None ]
data[1] = "asdf"
data[4] = data[3]
data[3][1] = [1,2,3]


print(data)
print()
all = [10, None]
tail = all
# DRAW HERE
for i in range(4):
    tail[1] = [ i*10+20, None ]
    tail = tail[1]
    # DRAW HERE
print(all)
