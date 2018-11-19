# Tiana Tsang Started : 12/11/2018 Last Modified: 15/11/2018
# Halving the interval method of approximating roots 
# Task: Create a program which is able to approximate the root of a given polynomial, given a range which the root lies within and the number of approximations 

def Main():
	polyformatted = []
	
	resultlow = 0
	resulthigh = 0
	applied = 0
	i = 0
	
	polynomial = input("Enter the polynomial: ")
	range = input("Enter the root range: ")
	iterations = int(input("Enter the number of times to apply the halving the interval method: "))
	
	limits = range.split(",")
	lowerlim = float(limits[0])
	upperlim = float(limits[1])
	
	polyformatted = GetPolynomial(polynomial,polyformatted)
	resultlow, resulthigh = TestLimits(polyformatted, lowerlim, upperlim,resultlow, resulthigh)
	
	while i < iterations:  
		lowerlim, upperlim, resulthigh, resultlow = HalveInt(polyformatted, resultlow, resulthigh, lowerlim, upperlim)
		i = i + 1 
		
def TestLimits(polyformatted, lowerlim, upperlim, resultlow, resulthigh): # Tests that a root lies within given limits
	
	for a in polyformatted: 
		if a[2] != 0:
			resultlow = resultlow + a[2]
			resulthigh = resulthigh + a[2]
			
		else:
			resultlow = resultlow + ((lowerlim ** a[0]) * a[1])
			resulthigh = resulthigh + (upperlim ** a[0] * a[1])
	
	if (resultlow >= 0 and resulthigh < 0) or (resulthigh >= 0 and resultlow < 0):
		limitsvalid = 1
	else: 
		limitsvalid = 0
	
	if limitsvalid == 0: 
		print("polynomial or range is not valid, please try again.")
		Main()
	
	return resultlow, resulthigh

def HalveInt(polyformatted, resultlow, resulthigh, lowerlim, upperlim): # Halves interal and returns new limits
	halvedint = (lowerlim + upperlim) / 2
	print("Estimated root: " + str(halvedint))
	newresult = 0
	
	for a in polyformatted:
	
		if a[2] != 0:
			newresult = newresult + a[2]
		else:
			newresult = newresult + ((halvedint ** a[0]) * a[1])
			
	print("ll: " + str(lowerlim) + " ul: " + str(upperlim))		
	
	if newresult <  0:
	
		if (resultlow > resulthigh): # if lowerlim result + & upperlim result - 
			upperlim = halvedint
			resulthigh = newresult
		else: 
			lowerlim = halvedint
			resultlow = newresult
			
	else:
	
		if (resultlow > resulthigh): 
			lowerlim = halvedint
			resultlow = newresult
		else: 
			upperlim = halvedint
			resulthigh = newresult
	
	return lowerlim, upperlim, resulthigh, resultlow 
			
def GetPolynomial(polynomial, polyformatted): # Takes polynomial string and places required operands into polyformatted list
	
	polynomial = polynomial.replace("- ", "+ -").split(" + ")
	
	for p in polynomial:
		print(p)
		tarray = []
		
		multiplier = ""
		exponent = ""
		constant = 0
		xfound = 0
		
		if "^" in p:
			
			for char in p:
			
				if (char != "x" and xfound == 0):
					multiplier = multiplier + char
					
				if (char != "^" and xfound == 1):                                      
					exponent = exponent + char	
					
				if char == "x":
					xfound = 1
				
		else:
		
			exponent = 1
			if "x" in p:
				
				if p == "x":
					multiplier = 1
					
				else:	
					multiplier = p.strip("x")
					
			else:
				constant = int(p)
		
		if len(str(multiplier)) == 0:
			multiplier = 1 
			
		tarray.append(int(exponent))
		tarray.append(int(multiplier)) 
		tarray.append(constant)
		polyformatted.append(tarray)
		
	return polyformatted

if __name__ == "__main__":  
	Main()
