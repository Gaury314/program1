#program to calculate the water bill based on numjber of units consumed
units=int(input("enter total unit consumed:"))
if units<=100:
    bill=units*5
elif units<=200:
    bill=(100*5)+(units-100)*8
else:
    bill=(100*5)+(100*8)+(units-200)*10
    print(f"total water bill for {units}units is:${bill}")        
