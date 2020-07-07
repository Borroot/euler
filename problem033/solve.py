from fractions import Fraction

result = Fraction(1, 1)
for numerator in range(11, 99):
    for denominator in range(numerator + 1, 100):
        fraction = Fraction(numerator, denominator)
        for i1 in range(0, 2):
            for i2 in range(0, 2):
                new1 = int(str(numerator)[abs(i1-1)])
                new2 = int(str(denominator)[abs(i2-1)])
                if str(numerator)[i1] == str(denominator)[i2] != '0' and new2 != 0 \
                   and fraction == Fraction(new1, new2):
                    print(f'{numerator}/{denominator} = {new1}/{new2}')
                    result *= Fraction(new1, new2)

print(result.denominator)
