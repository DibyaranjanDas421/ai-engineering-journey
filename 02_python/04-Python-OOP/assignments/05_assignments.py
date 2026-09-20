class Vehicle:

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model




class Car(Vehicle):

    def __init__(self,engine_cc,brand,model):
        super().__init__(brand,model)
        self.engine_cc=engine_cc

class Bike(Vehicle):

      def __init__(self,seats,brand,model):
        super().__init__(brand,model)
        self.seats=seats




