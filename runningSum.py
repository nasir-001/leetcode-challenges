def main():
    nums = [3,1,2,10,1]
    sumNumbers = []
    x = 0
    for i in nums:
        x = x + i
        sumNumbers.append(x)

    print(sumNumbers)

if __name__ == '__main__':
    main()