# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def order_weight(weights):
	weights = weights.split(' ')
	d = [(weight, sum(int(x) for x in weight)) for weight in weights]
	return " ".join(x[0] for x in sorted(d, key=lambda y: (y[1], str(y[0]))))
