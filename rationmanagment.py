a="02002C759AC1"
b="02002C75164D"




print"Ration service||shop no:-32"

for j in range( 25):
    print "-",
print""

print"sugar price:- Rs.35/kg"
print"wheat price:- Rs.10/kg"
print"dal:- Rs.50/kg"

for j in range( 25):
    print "-",
print""
 
i=raw_input("enter the card no.:-")

for j in range( 25):
    print "-",
print""

if(a==i):
    print"name- manish kumar"
    print"father name:- sumit kumar"
    print "dist. - jodhpur"
    print "contact:- ++91847321345 "
    
elif(b==i):
    print"name- sharwan kumar"
    print"father name:- sumit kumar"
    print "dist. - jaipur"
    print "contact:- ++91847321345 "

else:
    print " unknown person"

def price(x,y,z):
    print "sugar amount-",x,"sugar cost :- Rs.",35*x
    print"wheat  amount-", y,"wheat cost  :- Rs.",10*y
    print"dal  amount-", z,"dal cost  :- Rs.",50*z
    print "Total Amount :- Rs",(35*x)+(10*y)+(50*z)
    

print "enter the quantity one by one"
for j in range( 25):
    print "-",
print""
x=int(raw_input("enter the quantity of sugar :-"))
y=int(raw_input( "enter the quantity of wheat:-"))
z=int(raw_input( "enter the quantity of dal:-"))

for j in range( 25):
    print "-",
print""

price(x,y,z)
    
