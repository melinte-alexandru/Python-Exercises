# 3. Drepte unice ax + by + c = 0
def get_unique_lines(points):
    from math import gcd
    lines = set()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            a = y1 - y2
            b = x2 - x1
            c = x1 * y2 - x2 * y1
            common = gcd(gcd(a, b), c)
            lines.add((a//common, b//common, c//common))
    return list(lines)