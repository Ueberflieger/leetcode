def decodeString(s):
    ret, i = decodeString2(s)
    return ret

def decodeString2(s):
    decoded = ""
    digits = ""
    i = 0
    while i < len(s):
        c = s[i]
        if c.isalpha():
            decoded += c
        elif c.isdigit():
            digits += c
        elif c == '[':
            substr, consumed = decodeString2(s[i + 1:])
            i = i + consumed
            decoded += int(digits) * substr
            digits = ""
        elif c == ']':
            return decoded, i + 1
        i += 1
    return decoded, i

print(decodeString("3[a]2[bc]"))
print(decodeString("3[a2[c]]"))
print(decodeString("2[abc]3[cd]ef"))
print(decodeString("3[a]2[bc]"))
