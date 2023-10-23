# list are ordered

fruits=["Mangoes","Oranges","bananas","Melon"]
fruits.sort()
num=[1,3,7,0,14,4,-3,2]
num.sort()
num[3]=9
rep=num*2
len(num)


print(fruits)
fruits[2]="Apples"
print(f"I love eating {fruits[2]}")
print()
print(num)
print(rep)
print(len(num))
print(num.sort())


#Tupples    immutables value and are ordered(u cant change the values)

Cars=("Toyota","Benz","Nissan","Benz")
print(Cars[1])
tup=Cars*3
print(tup)
print(tup.count("Benz"))

#tupples take less time than list

# sets  its unordered (no index)

days={"Monday","Tuesday","Wednesday","Thursday","Friday"}
print(days)

# dictionaries   mutable   s-string %-to enable string

staff_details={"Name":"Adhoch","Age":26,"Company":"By Grace","Gender":"male","salariy":56000}
print(staff_details)
print(f"Name %s" %staff_details["Company"])




