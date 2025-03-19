def main():
    MAXIMUM = 10000

    fibonacci = [0, 1]
    while fibonacci[-1] < MAXIMUM:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    print(fibonacci)


if __name__ == "__main__":
    main()
