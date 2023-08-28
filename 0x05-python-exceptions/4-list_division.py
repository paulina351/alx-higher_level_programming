#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    Nlist = []
    count = 0
    for b in range(list_length):
        try:
            count = my_list_1[b] / my_list_2[b]
        except(ValueError, TypeError):
            print("Wrong type")
            count = 0
        except ZeroDivisionError:
            print("division by 0")
            count = 0
        except IndexError:
            print("out of range")
            count = 0
        finally:
            Nlist.append(count)
    return Nlist
