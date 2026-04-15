# 10222 Decode the Mad man
# 中文註解：QWERTY鍵盤左移3位解碼

keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
while True:
    try:
        line = input()
        ans = ''
        for ch in line:
            if ch == ' ':
                ans += ' '
            else:
                idx = keyboard.find(ch.lower())
                if idx >= 3:
                    ans += keyboard[idx-3]
                else:
                    ans += ch
        print(ans)
    except EOFError:
        break
