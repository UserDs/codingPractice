p, s, t, h, x = map(int, input().split())
if s - t > x:
	print(x * p)
else:
	hiked_price_for = x - s + t
	print(hiked_price_for * h + (s - t) * p)
