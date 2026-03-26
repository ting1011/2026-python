# UVA 10056 - 手打版
def main():
    while True:
        try:
            n, p, i = map(float, input().split())
            if p == 0:
                print("0.0000")
                continue
            ans = (1-p)**(i-1) * p / (1-(1-p)**n)
            print(f"{ans:.4f}")
        except EOFError:
            break

if __name__ == "__main__":
    main()
