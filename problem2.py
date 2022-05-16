a = int(input('1 chislo= '))
b = int(input('2 chislo= '))
c = int(input('3 chislo= ')) 
if a > b and a > c or a < b and a < c:
    print(a, '1' )
if b > a and b > c or b < a and b < c:
    print(b, '2' )
if c > a and c > b or c < a and c < b:
    print(c, '3' )
