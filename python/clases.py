class Vehicle:
    kind = 'car'

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model_name = model

    @property
    def name(self):
        return "%s %s" % (self.manufacturer, self.model_name)

    def __repr__(self):
        return "<%s>" % self.name

car = Vehicle('Toyota', 'Corolla')
print(car, car.kind)