class Superhero:
    """Base class for all superheroes"""
    
    def __init__(self, name, secret_identity, powers, weakness, base_of_operations):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # List of powers
        self.weakness = weakness
        self.base_of_operations = base_of_operations
        self.energy_level = 100
        self.is_in_costume = False
    
    def transform(self):
        """Put on superhero costume"""
        self.is_in_costume = True
        print(f"{self.name} has transformed! Ready for action!")
    
    def use_power(self, power_index, intensity="medium"):
        """Use a specific power with given intensity"""
        if not self.is_in_costume:
            print("Cannot use powers without costume! Transform first.")
            return False
        
        if power_index >= len(self.powers):
            print("Power not available!")
            return False
        
        energy_cost = {"low": 5, "medium": 15, "high": 30}
        cost = energy_cost.get(intensity, 15)
        
        if self.energy_level >= cost:
            self.energy_level -= cost
            power = self.powers[power_index]
            print(f"{self.name} uses {power} at {intensity} intensity!")
            return True
        else:
            print("Not enough energy! Rest needed.")
            return False
    
    def rest(self):
        """Recover energy"""
        self.energy_level = min(100, self.energy_level + 25)
        print(f"{self.name} is resting. Energy level: {self.energy_level}%")
    
    def get_status(self):
        """Return current status"""
        status = "in costume" if self.is_in_costume else "in civilian form"
        return f"{self.name} ({status}) - Energy: {self.energy_level}%"
    
    def __str__(self):
        return f"Superhero: {self.name} | Identity: {self.secret_identity}"


class ElementalHero(Superhero):
    """Heroes who control natural elements"""
    
    def __init__(self, name, secret_identity, element, powers, weakness, base_of_operations):
        super().__init__(name, secret_identity, powers, weakness, base_of_operations)
        self.element = element
        self.element_charge = 100
    
    def charge_element(self):
        """Recharge elemental energy"""
        self.element_charge = 100
        print(f"{self.name}'s {self.element} powers are fully charged!")
    
    def use_power(self, power_index, intensity="medium"):
        """Override to include elemental charge"""
        if self.element_charge <= 0:
            print(f"{self.element} energy depleted! Need to recharge.")
            return False
        
        success = super().use_power(power_index, intensity)
        if success:
            charge_cost = {"low": 10, "medium": 25, "high": 50}
            self.element_charge -= charge_cost.get(intensity, 25)
        
        return success
    
    def get_status(self):
        """Override to show elemental charge"""
        base_status = super().get_status()
        return f"{base_status} | {self.element.capitalize()} Charge: {self.element_charge}%"


class TechHero(Superhero):
    """Heroes who rely on technology and gadgets"""
    
    def __init__(self, name, secret_identity, powers, weakness, base_of_operations, gadgets):
        super().__init__(name, secret_identity, powers, weakness, base_of_operations)
        self.gadgets = gadgets  # Dictionary: {gadget_name: uses_remaining}
        self.tech_level = 100
    
    def use_gadget(self, gadget_name):
        """Use a specific gadget"""
        if gadget_name not in self.gadgets:
            print("Gadget not available!")
            return False
        
        if self.gadgets[gadget_name] <= 0:
            print(f"{gadget_name} is out of charges!")
            return False
        
        self.gadgets[gadget_name] -= 1
        print(f"{self.name} uses {gadget_name}! Charges remaining: {self.gadgets[gadget_name]}")
        return True
    
    def repair_tech(self):
        """Repair and recharge all technology"""
        self.tech_level = 100
        for gadget in self.gadgets:
            self.gadgets[gadget] = 5  # Reset all gadgets to 5 charges
        print(f"{self.name}'s technology has been repaired and recharged!")


# Example usage and demonstration
if __name__ == "__main__":
    # Create different types of heroes
    print("=== SUPERHERO UNIVERSE ===")
    
    # Elemental Hero
    pyro = ElementalHero(
        "Pyro Knight",
        "Alex Chen",
        "fire",
        ["Fire Blast", "Flame Shield", "Meteor Strike"],
        "water",
        "Volcano Lair"
    )
    
    # Tech Hero
    gadgeteer = TechHero(
        "Gadget Master",
        "Maya Rodriguez",
        ["Hacking", "Gadget Deployment", "Tech Analysis"],
        "EMP pulses",
        "Underground Bunker",
        {"Grappling Hook": 5, "Smoke Bombs": 3, "EMP Device": 2, "Drone": 4}
    )
    
    # Regular Superhero
    captain_strong = Superhero(
        "Captain Strong",
        "John Smith",
        ["Super Strength", "Flight", "Invulnerability"],
        "Magic",
        "Sky Fortress"
    )
    
    # Demonstrate polymorphism
    heroes = [pyro, gadgeteer, captain_strong]
    
    for hero in heroes:
        print(f"\n--- Testing {hero.name} ---")
        hero.transform()
        
        # Each hero uses their powers differently
        if isinstance(hero, ElementalHero):
            hero.use_power(0, "high")
            print(hero.get_status())
            hero.charge_element()
        
        elif isinstance(hero, TechHero):
            hero.use_power(1)
            hero.use_gadget("Grappling Hook")
            print(hero.get_status())
            hero.repair_tech()
        
        else:
            hero.use_power(2, "low")
            print(hero.get_status())
            hero.rest()
    
    # Show inheritance hierarchy
    print(f"\n=== INHERITANCE DEMONSTRATION ===")
    print(f"Pyro Knight is a Superhero: {isinstance(pyro, Superhero)}")
    print(f"Pyro Knight is an ElementalHero: {isinstance(pyro, ElementalHero)}")
    print(f"Gadget Master is a TechHero: {isinstance(gadgeteer, TechHero)}")
    
    # Method overriding demonstration
    print(f"\n=== METHOD OVERRIDING ===")
    pyro.transform()
    pyro.use_power(0, "high")
    print(pyro.get_status())  # Shows elemental charge (overridden method)
    
    captain_strong.transform()
    captain_strong.use_power(0)
    print(captain_strong.get_status())  # Regular status (base method)
This implementation demonstrates:
