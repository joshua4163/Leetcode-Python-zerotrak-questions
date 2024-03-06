class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        l = []
        F = (9/5 * celsius) + 32
        Kelvin = celsius + 273.15
        l.append(Kelvin)
        l.append(F)
        return l