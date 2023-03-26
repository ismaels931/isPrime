def isPrime(number : int) -> bool:
    if number <= 1:
        return False

    counter = 2

    while counter ** 2 <= number:
        if number % counter == 0:
            return False

        counter += 1

    return True

if __name__ == '__main__':
    numbers = int(input('Enter a number => '))

    for number in range(1, numbers + 1):
        if isPrime(number):
            print(number)
