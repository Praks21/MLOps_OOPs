# initiate a class
class emp:
    # special method/magic method/dunder methods - constructor

    def __init__(self):
        print("started executing the data")
        self.id=123
        self.salary=500000
        self.designation="SDE"
        print("attributed/data has een initiated")
    
    def travel(self,destination):
        print("This function was called manually")
        print("emp is travelling to",destination)


# creating an object/instance of class
sam=emp()
# printing the attribute
# print(sam.id)

# calling a method
# sam.travel("Jhansi")

print(type(sam))
