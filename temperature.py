def celsius_convert(ftemp):
	ctemp = (ftemp - 32) * 5/9
	return ctemp
def fahrenheit_convert(ctemp):
	ftemp = ctemp * 9/5 + 32
	return ftemp
ftemp = 72
print("{} degrees F = {} degrees C".format(ftemp, celsius_convert(ftemp)))

ctemp = 37
print("{} degrees C = {} degrees F".format(ctemp, fahrenheit_convert(ctemp)))
