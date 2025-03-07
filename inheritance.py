# # simple inheritance

# ## Base Class
# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print(self.name," makes a sound.")

# class dog(Animal):
#     # this is contructor overrideing
#     #def __init__(self):
#     #    self.behaviour="friendly"
        
#     def speak(self):
#         print(self.behaviour,"Barks")


# #animal=Animal("generic animal")
# #animal.speak()

# # Dog=dog()
# # Dog.speak()


# super keyword

class Animal:
     def __init__(self):
         self.name="Buddy"

     def speak(self):
        print(self.name," makes a sound.")

class dog(Animal):
     
    def __init__(self,breed):
        super().__init__()
        self.breed=breed
        
    def speak(self):
       super().speak()
       print(self.name,"Barks",self.breed)


Dog=dog("labra")
Dog.speak()


