class Dessert:
    def __init__(self, name=None, calories=0):
        self._name = name
        self._calories = int(calories)
    def is_healthy(self):
        if isinstance(self._calories, int):
            return True if self._calories < 200 else False
        else:
            return True
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
        if isinstance(calories, str):
            self._calories = int(calories) if calories.isdigit() else calories
        else:
            self._calories = calories