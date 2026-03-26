# UVA 10055 - 手打版
def main():
    while True:
        try:
            x, y = map(int, input().split())
            print(abs(x-y))
        except EOFError:
            break

if __name__ == "__main__":
    main()
