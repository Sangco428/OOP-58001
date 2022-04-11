def main():
    class TemperatureConversion:

        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):

        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):

        def conversion(self):
            return self._temp + 273.15

    class FahrenheitToCelsius(TemperatureConversion):

        def conversion(self):
            return (self._temp - 32) * 5/9

    class FahrenheitToKelvin(TemperatureConversion):

        def conversion(self):
            return (self._temp - 32) * 5/9 + 273.15

    class KelvinToCelsius(TemperatureConversion):

        def conversion(self):
            return self._temp - 273.15

    class KelvinToFahrenheit(TemperatureConversion):

        def conversion(self):
            return ((self._temp - 273.15) * 9) / 5 + 32

    tempInCelsius = float(input("Enter the temperature in Celsius: "))

    convert = CelsiusToKelvin(tempInCelsius)

    print(str(convert.conversion()) + " Kelvin")

    convert = CelsiusToFahrenheit(tempInCelsius)

    print(str(convert.conversion()) + " Fahrenheit")

    tempInKelvin = float(input("Enter the temperature in Kelvin: "))

    convert = KelvinToCelsius(tempInKelvin)

    print(str(convert.conversion()) + " Celsius")

    convert = KelvinToFahrenheit(tempInKelvin)

    print(str(convert.conversion()) + " Fahrenheit")


    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    convert = FahrenheitToCelsius(tempInFahrenheit)

    print(str(convert.conversion()) + " Celsius")

    convert = FahrenheitToKelvin(tempInFahrenheit)

    print(str(convert.conversion()) + " Kelvin")
main()