#!/usr/bin/python3


def codepoint(x):
    return chr(int(x, 16))


copyright_sign = codepoint("a9")
pound_sign = codepoint("a3")
up_arrow = codepoint("2191")

chars = [chr(i) for i in range(33, 126)] + [copyright_sign]
chars[94 - 33] = up_arrow
chars[96 - 33] = pound_sign

print("".join(chars))
