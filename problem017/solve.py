ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['teen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
specials = {10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 15 : 'fifteen', 18 : 'eighteen'}

count = 11  # one thousand

def underhundred(n):
    global count
    if 0 < n < 10:
        count += len(ones[n - 1])
    elif n in specials:
        count += len(specials[n])
    elif n > 13:
        count += len(tens[n // 10 - 1])
        if n % 10 != 0:
            count += len(ones[n % 10 - 1])

def abovehundred(n):
    global count
    count += len(ones[n // 100 - 1]) + len('hundred')
    if n % 100 > 0:
        count += len('and')

for i in range(1, 1000):
    if i >= 100:
        abovehundred(i)
    underhundred(i % 100)

print(count)
