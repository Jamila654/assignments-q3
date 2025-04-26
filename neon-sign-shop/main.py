class NeonSignShop:
    _voltage = 120 # Protected attribute (single underscore, accessible but meant for internal/subclass use)
    __gas_type = "Neon" # Private attribute (double underscore, name-mangled for restricted access)
    
    def __init__(self, message, color):
        self.message = message
        self.color = color
        
    # Public method to access private attribute
    def get_gas_type(self):
        return f"Gas type: {self.__gas_type}"
    
    def _adjust_brightness(self, level):
        return f"{self.message} glows at {level}% brightness with {self._voltage}V"
    
    def __ignite_gas(self):
        return f"{self.__gas_type} gas ignited for {self.message} in {self.color}!"
    
    def light_up(self):
        return self.__ignite_gas()
    
class CustomSignShop(NeonSignShop):
    def __init__(self, message, color, font_style):
        super().__init__(message, color)
        self.font_style = font_style
    
    def display(self):
        brightness = self._adjust_brightness(80)
        return f"Custom {self.font_style} sign: {brightness}"
    
    def get_info(self):
        gas = self.get_gas_type()
        return f"Sign: {self.message}, Color: {self.color}, Gas: {gas}, Voltage: {self._voltage}V"
def main():
    print("\033[95m🌀 UV Neon Sign Shop Demo 🌀\033[0m")
    print("-" * 40)
    
    basic_sign = NeonSignShop("OPEN", "Pink")
    print("\033[91m💡 Basic Neon Sign:\033[0m")
    print(basic_sign.light_up())
    print(basic_sign.get_gas_type())
    print("-" * 40)
    
    custom_sign = CustomSignShop("WELCOME", "Purple", "Cursive")
    print("\033[94m🌟 Custom Neon Sign:\033[0m")
    print(custom_sign.display())
    print(custom_sign.get_info())
    print("-" * 40)
    
    print("\033[96m🔍 Access Demo:\033[0m")
    print(f"Protected _voltage (accessible): {custom_sign._voltage}V")
    try:
        print(f"Private __gas_type (inaccessible): {custom_sign.__gas_type}")
    except AttributeError:
        print("❌ Cannot access private __gas_type directly!")
        print(f"Access via public method: {custom_sign.get_gas_type()}")

    print("\033[95m🌌 Demo Complete! Private vs Protected clearly shown.\033[0m")


if __name__ == "__main__":
    main()
