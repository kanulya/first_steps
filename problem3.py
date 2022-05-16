a = 17391
b = 546
c = 934
if a % 17 < b % 17 and a % 17 < c % 17:
	print( a , '-ostatok menwe vsego v A')
elif b % 17 < a % 17 and b % 17 < c % 17:
	print(b , '-ostatok menwe vsego v B')
elif c % 17 < a % 17 and c % 17 < b % 17:
	print(c ,'ostatok menwe vsego v C')
