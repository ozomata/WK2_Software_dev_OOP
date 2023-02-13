class Circle:
 
    def __init__(self, radius):
        self.radius =float(radius)
        
    def areaOfCircle(self, radius):
        pi=3.14159
        return (pi*radius**2)
    def circumferenceOfCircle(self, radius):
        pi=3.14159
        return (2*pi*radius)

user_radius = float(input("input the radius: "))


userCircle = Circle (user_radius)
userCircle.radius=user_radius
print("The area was of your circle is : "  , userCircle.areaOfCircle(user_radius))
print("The circumference was of your circle is : "  , userCircle.circumferenceOfCircle(user_radius))
