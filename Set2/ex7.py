# 7. ASCII divizibilitate
def ascii_filter(x=1, *strings, flag=True):
    results = []
    for s in strings:
        if flag:
            results.append([c for c in s if ord(c) % x == 0])
        else:
            results.append([c for c in s if ord(c) % x != 0])
    return tuple(results)