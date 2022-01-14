def shape_alpha():
    list1 = [10,20]
    list2 = [50,60]
    list_return = [list1,30,40,list2]
    return list_return

def shape_bravo():
    list1 = [123,456]
    list2 = [789,1024]
    list3 = [list1,list2]
    list4 = [list2,list1]
    list_return = [list3,list4]
    return list_return

def shape_charlie(arg1):
    list1 = [arg1,arg1]
    list2 = [list1,list1]
    list_return = [list2,list1]
    return list_return

def shape_delta(arg1,arg2):
    list1 = [arg2]
    list2 = [arg1,list1]
    list3 = [arg1]
    list4 = [list2,list3]
    list_return = [arg1,arg2,list4,[17]]
    return list_return

def shape_echo(arg1,arg2,arg3):
    list1 = [arg3,None]
    list2 = [arg2,list1]
    list_return = [arg1,list2]
    list1[1] = list_return
    return list_return