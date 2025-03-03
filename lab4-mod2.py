class Animal:
    """Базовый класс для описания общих характеристик животных."""

    def __init__(self, name: str, age: int) -> None:
        """ Конструктор класса Animal. :param name: Имя животного. :param age: Возраст животного. """
        self._name = name  # Непубличный атрибут, чтобы предотвратить прямое изменение имени извне
        self.age = age     # Публичный атрибут возраста

    @property
    def name(self) -> str:
        """Геттер для получения имени животного."""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """ Сеттер для изменения имени животного. :param new_name: Новое имя животного. """
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть строкой.")
        self._name = new_name

    def eat(self) -> None:
        """Метод, описывающий процесс питания животного."""
        print(f"{self.name} ест.")

    def sleep(self) -> None:
        """Метод, описывающий процесс сна животного."""
        print(f"{self.name} спит.")

    def make_sound(self) -> None:
        """Абстрактный метод для создания звука животным."""
        pass

    def __str__(self) -> str:
        """Магический метод для преобразования объекта в строку."""
        return f"Животное {self.name}, возраст {self.age}"

    def __repr__(self) -> str:
        """Магический метод для представления объекта в консоли."""
        return f"Animal(name='{self.name}', age={self.age})"
        from typing import List

class Cat(Animal):
    """Класс для описания кошек, наследуется от класса Animal."""

    def __init__(self, name: str, age: int, favorite_toys: list[str]) -> None:
        """ Конструктор класса Cat. :param name: Имя кошки. :param age: Возраст кошки. :param favorite_toys: Список любимых игрушек кошки. """
        super().__init__(name, age)
        self.favorite_toys = favorite_toys  # Любимые игрушки кошки

    def play_with_toy(self, toy: str) -> None:
        """ Метод, описывающий игру кошки с игрушкой. :param toy: Название игрушки. """
        if toy in self.favorite_toys:
            print(f"{self.name} играет с любимой игрушкой {toy}.")
        else:
            print(f"{self.name} неохотно играет с {toy}. Это не её любимая игрушка.")

    def make_sound(self) -> None:
        """Метод, описывающий звук, издаваемый кошкой."""
        print(f"{self.name} мяукает.")

    def __str__(self) -> str:
        """Переопределенный магический метод для преобразования объекта в строку."""
        return f"Кошка {self.name}, возраст {self.age}, любимые игрушки: {', '.join(self.favorite_toys)}"

    def __repr__(self) -> str:
        """Переопределенный магический метод для представления объекта в консоли."""
        return f"Cat(name='{self.name}', age={self.age}, favorite_toys={self.favorite_toys})"

class Dog(Animal):
    """Класс для описания собак, наследуется от класса Animal."""

    def __init__(self, name: str, age: int, breed: str) -> None:
        """ Конструктор класса Dog. :param name: Имя собаки. :param age: Возраст собаки. :param breed: Порода собаки. """
        super().__init__(name, age)
        self.breed = breed  # Порода собаки

    def bark(self) -> None:
        """ Метод, описывающий лай собаки. :return: None """
        print(f"{self.name} лает.")

    def make_sound(self) -> None:
        """Метод, описывающий звук, издаваемый собакой."""
        self.bark()

    def __str__(self) -> str:
        """Переопределенный магический метод для преобразования объекта в строку."""
        return f"Собака {self.name}, возраст {self.age}, порода {self.breed}"

    def __repr__(self) -> str:
        """Переопределенный магический метод для представления объекта в консоли."""
        return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"

if __name__ == "__main__":
    dog = Dog(name = "Барбос", age = 5, breed = "Алабай")
    cat = Cat("Марти", 4, ["фантик","бубенчик"])

    print(cat)      # Кошка Марти, возраст 4, любимые игрушки: бубенчик
    print(dog)      # Собака Барбос, возраст 5, порода Алабай

    cat.eat()       #Марти ест.
    dog.sleep()     # Барбос спит.

    cat.make_sound()   # Марти мяукает.
    dog.make_sound()   # Барбос лает.

    cat.play_with_toy("бубенчик")  # Марти играет с любимой игрушкой.
    