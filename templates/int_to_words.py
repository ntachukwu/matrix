

def get_amount_in_words(amount):
    stringed = str(amount)

    answer = []
    hundredth = 1
    millionth = 0
    overflown = 0

    units = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }
    tens = {
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen",
        "2": "twenty",
        "3": "thirty",
        "4": "fourty",
        "5": "fifty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety"

    }

    for num in range(len(stringed)-1, -1, -1):
        if stringed[num] == "0":
            hundredth += 1
        elif hundredth == 1 and (stringed[num] == stringed[0] or stringed[num-1] != "1"):
            if overflown != 0:
                overflown = 0
                milli = million(millionth)
                if milli:
                    answer.append(milli)
            answer.append(units[stringed[num]])
            hundredth = 2
        elif hundredth == 1 and stringed[num-1] == "1":
            hundredth = 2
        elif hundredth == 2 and stringed[num] == "1":
            if overflown != 0:
                overflown = 0
                milli = million(millionth)
                if milli:
                    answer.append(milli)
            answer.append(tens[(stringed[num]+stringed[num+1])])
            hundredth = 3
        elif hundredth == 2 and stringed[num] != "1":
            if overflown != 0:
                overflown = 0
                milli = million(millionth)
                if milli:
                    answer.append(milli)
            answer.append(tens[stringed[num]])
            hundredth = 3
        elif hundredth == 3:

            if overflown == 0:
                millionth += 1
            if overflown != 0:
                overflown = 0
                milli = million(millionth)
                if milli:
                    answer.append(milli)
            answer.append("hundred")
            answer.append(units[stringed[num]])

            if num - 1 >= 0:
                milli = million(millionth)
                if milli:
                    answer.append(milli)

            hundredth = 1

        if hundredth > 3:
            hundredth = 1
            overflown = 1
            millionth += 1

    returned_answer = " ".join(reversed(answer))

    return returned_answer


def million(millionth):
    if millionth == 1:
        return "thousand"
    elif millionth == 2:
        return "million"
    elif millionth == 3:
        return "billion"
    elif millionth == 4:
        return "trillion"
    elif millionth == 5:
        return "quardrillion"
    elif millionth == 6:
        return "qunitrillion"
    else:
        return None


nums = 30000000901

print(get_amount_in_words(nums))
