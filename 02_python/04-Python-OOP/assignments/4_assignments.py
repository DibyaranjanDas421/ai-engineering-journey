class Shape:

    def area(self):
        print("area")




class Circle(Shape):
    PI=3.141
    def calc_area(self,radius):
      self.area=2*self.PI*radius*radius
      return self.area

class  Rectangle(Shape):
    
    def area(self,length,width):
        self.area=(length*width)
        return self.area



c1=Circle()

print(c1.calc_area(4))


r1=Rectangle()

print(r1.area(3,4))



