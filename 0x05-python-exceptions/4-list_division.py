#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    Nlist = []
    count = 0
    for b in range(0, list_length):
        try:
            x = my_list_1[b] / my_list_2[b]
        except TypeError:
            print("Wrong type")
            count = 1
        except ZeroDivisionError:
            print("division by 0")
            count = 1
        except IndexError:
            print("out of range")
            count = 1
        finally:
            if count:
                count = 0
                Nlist.append(0)
            else:
                Nlist.append(x)
    return Nlist
