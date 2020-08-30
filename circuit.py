
class circuitElement :
    def __init__(self) :
        pass
    def __repr__(self) :
        return "A base class for a circuit element"

class battery(circuitElement) :
    def __init__(self,voltage) :
        self.voltage = voltage
    def __repr__(self) :
        return f"{self.voltage}V battery"

class resistor(circuitElement) :
    def __init__(self,resistance) :
        self.resistance = resistance
    def __repr__(self):
        return f"{self.resistance} ohm resistor"

class capacitor(circuitElement) :
    def __init__(self,capacitance) :
        self.capacitance = capacitance
    def __repr__(self):
        return f"Capacitor of capacitance : {self.capacitance}"

class branch :
    def __init__(self,structure=[]) :
        self.structure = structure


class circuit :
    def __init__(self,structure=[]) :
        self.structure = structure
        try :
            self.startVlotage = structure[0].voltage
        except :
            raise TypeError("first element is not a battery")
    def __repr__(self) :
        return f"Elements in this circuit are {self.structure}"

    def startFlow(self) :
        pass

    
if __name__ == "__main__":
    
    circuit1 = circuit([battery(9),resistor(10)])
    print()
    print(
        circuit1.startFlow()
    )
    print()