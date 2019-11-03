from abc import ABC, abstractmethod, abstractmethod, abstractproperty

class Door(ABC):
    def __init__(self):
        self._width = None
        self._height = None

    @property
    @abstractmethod
    def width(self):
        pass

    @width.setter
    @abstractmethod
    def width(self, value):
        pass

    @property
    @abstractmethod
    def height(self):
        pass

    @height.setter
    @abstractmethod
    def height(self, value):
        pass

class WoodenDoor(Door):
    def __init__(self, w, h):
        self._width = w
        self._height = h

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        return self._width
    
    def __repr__(self):
        return 'Wooden door {} x {}'.format(self._width, self._height)

class DoorFactory:
    def get_wooden_door(self, w, h):
        return WoodenDoor(w, h)

if __name__ == '__main__':
    factory = DoorFactory()
    door = factory.get_wooden_door(100, 200)
    print(door)
