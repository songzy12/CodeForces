number = int(input())
table1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
          'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
          'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen',
          'eighteen', 'nineteen']
table2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
          'eighty','ninety']
if number < 20:
    print(table1[number])
else:
    print(table2[number//10 - 2] +
          ('-'+table1[number % 10]) if number % 10 else '')
