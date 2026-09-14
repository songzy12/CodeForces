# https://codeforces.com/contest/535/problem/A

TABLE1 = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen'
]
TABLE2 = [
    'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
]


def convert(number):
    if number < 20:
        return TABLE1[number]
    else:
        return TABLE2[number // 10 -
                      2] + ('-' + TABLE1[number % 10]) if number % 10 else ''


if __name__ == "__main__":
    number = int(input())
    print(convert(number))
