#logical operators

print(not True)
print(not False)  #prints the opposite of returned boolean value 

print("--------------------------------------------------------------")
a=10
b=5

print(not (a<b)) #return TRUE
print(not (a>b)) #return FALSE

print(a<b) #return FALSE
print(a>b) #return TRUE

print("--------------------------------------------------------------")

V1=False
V2=True

print("AND operator=",V1 and V2)
print("OR operator=",V1 or V2)

print("--------------------------------------------------------------")

print("AND operator=",(a>b) and (a<b)) #False
print("OR operator=",(a==b) or (a*b!=0)) #True