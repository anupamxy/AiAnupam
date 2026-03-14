class Chai:
    def __init__(self, temperature, strength, origin):
        self.temperature=temperature
        self.strength=strength
        self.origin=origin
class GingerClass(Chai):
    def __init__(self, temperature, strength, origin, flavour):
        super().__init__(temperature, strength, origin)
        # we avoid code duplication by calling the __init__ method of the parent class using super().__init__(temperature, strength, origin). This allows us to initialize the inherited attributes (temperature, strength, origin) in the parent class, and then we can add the new attribute flavour specific to the GingerClass without repeating the code for initializing the inherited attributes.
        self.flavour=flavour
        # i have just added flavour attribute to the GingerClass which is not present in the Chai class. This allows us to create a new class that is a specialized version of the Chai class, without having to duplicate the code in the Chai class.