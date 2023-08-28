#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for y in range(1, 3):
        try:
            if y > a:
                raise Exception('Too far')
            else:
                result = result + (a ** b) / y
        except:
            result = b + a
            break
        finally:
            pass
    return (result)
