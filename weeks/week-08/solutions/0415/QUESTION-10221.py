# 10221 Satellites
# 中文註解：三角函數計算弧長與弦長
import math

R = 6440
while True:
    try:
        s, a, unit = input().split()
        s = float(s)
        a = float(a)
        r = R + s
        if unit == 'min':
            a = a / 60
        rad = math.radians(a)
        if rad > math.pi:
            rad = 2*math.pi - rad
        arc = r * rad
        chord = 2 * r * math.sin(rad/2)
        print(f"{arc:.6f} {chord:.6f}")
    except EOFError:
        break
