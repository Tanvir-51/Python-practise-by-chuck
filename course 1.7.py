largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    #cvalue = num
    try:
        ivalue = int(num)
    except:
        print("Invalid Output")
        
        
    if largest is None:
        largest = ivalue
    elif ivalue>largest:
        largest = ivalue
    elif smallest is None:
        smallest = ivalue
    elif ivalue<smallest:
        smallest = ivalue
        
    
    #print(num)

print("Maximum is ", largest)
print("Minimum is ", smallest)