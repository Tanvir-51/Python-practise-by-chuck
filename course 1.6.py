		def computepay(h,r):
		    
		if h>40:
			np = h * r
	        op = (h-40) * (r * 0.5)
	        gp = np + op
	    else:
	        gp = h * r
	        
	    return gp

		hrs = input("Enter Hours:")
		rte = input("Enter Rate:")
		h = float(hrs)
		r = float(rte)
		p = computepay(h,r)
		print("Pay",p)