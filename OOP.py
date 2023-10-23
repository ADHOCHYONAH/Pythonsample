class fruits:
    def __init__(self,type,price,color):
        self.type=type
        self.price=price
        self.color=color
    def onyesha(self):
        print(f"I like eating {self.type} and it costs {self.price}, color being{self.color}")
#creating an object

myobj=fruits("Apple","Ksh30","Red")
myobj2=fruits("Melon","Ksh20" ,"Green")
myobj.onyesha()
myobj2.onyesha()