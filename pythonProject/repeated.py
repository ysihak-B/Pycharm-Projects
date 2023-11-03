# import numpy as np
def repeated_character(s):
    count = [0 for i in range(256)]
    for c in s:
        char = c
        c = ord(c)
        if count[c] == 0:
            count[c] += 1
        else:
            print("the first repeated character is", char)
            return True
    return False


def power(p, i):
    if i == 0:
        return 1
    elif i == 1:
        return p
    else:
        return p * power(p, i-1)


def hash_function(s):
    string = s.lower()
    p = 31
    m = 7
    total = 0
    alphabets = "abcdefghijklmnopqrstuvwxyz "
    for i in range(len(string)):
        for j in range(27):
            if string[i] == alphabets[j]:
                pos = j + 1
                # print(pos)
                # print(power(p, i))
                total += pos * power(p, i)
                # print("the total value is", total)
            j += 1
        i += 1
    # print(total)
    return total % m


def main():
    if repeated_character("shakily") is False:
        print("there is no repeated character")
        print(ord(" "))
        print(chr(10))
        print("ysihak"),print("ysihak")
    print(hash_function("ysi hak"))
    print(hash_function("alemu"))
    print(hash_function("haile"))
    print(hash_function("kibret"))
    print(hash_function("bamlaku"))
    print(hash_function("abrham"))


main()
