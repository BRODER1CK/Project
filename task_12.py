class Dessert:
    def __init__(self, name=None, calories=0):
        self._name = name
        self._calories = int(calories)
    def is_healthy(self):
        return True if self._calories < 200 else False
    def is_delicious(self):
        return True
    @property
    def name(self):
        return self._name
    @property
    def calories(self):
        return self._calories
    @name.setter
    def name(self, name):
        self._name = name
    @calories.setter
    def calories(self, calories):
        self._calories = int(calories)
class JellyBean(Dessert):
    def __init__(self, name=None, calories=0, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor
    def is_healthy(self):
        return super().is_healthy()
    def is_delicious(self):
        return super().is_delicious() if self._flavor != 'black licorice' else False
    @property
    def name(self):
        return super().name
    @property
    def calories(self):
        return super().calories
    @property
    def flavor(self):
        return self._flavor
    @name.setter
    def name(self, name):
        super().name(name)
    @calories.setter
    def calories(self, calories):
        super().calories(calories)
    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor