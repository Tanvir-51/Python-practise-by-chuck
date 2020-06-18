hrs = input("Enter Hours:")
h = float(hrs)
hp = input("Enter rate per hour:")
p = float(hp)

if(h>40):
	Eh = (h-40)*(p*1.5) // Eh = (h-40)*(p*0.5)
	Nh = (40*p)			// Nh = (h*p)

	gp = Eh+Nh

//else:
	gp = h*p// 

print(gp)