
class Dog():
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
        
  
  

    def speak(self):
        return self.breed
        
dog1 = Dog("Lab", "John", 8)
dog2 = Dog("Pug", "Crums", 12)



print(dog1.speak())
print(dog2.speak())


