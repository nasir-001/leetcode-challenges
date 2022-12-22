def look_say(number: int) -> int:
    num = str(number)

    result = ""
    i = 0

    while i < len(num):
        count = 1
        while (i + 1 < len(num)) and (num[i] == num[i+1]):
            i += 1
            count += 1
        result += (str(count) + num[i])
        i += 1

    return int(result)