from random import randint


class Node:
    # Инициализация ноды заданными значениями
    def __init__(self, value):
        self.value = value # Хранимое значение
        self.next = None   # Ссылка на следующую ноду


class Stack:
    """
    Класс Стек, состоит из объектов класса Node

    """
    # Инициализация стека пустой головой
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # Текущий размер стека
    def get_size(self):
        return self.size

    # Проверка, является ли стек пустым
    def is_empty(self):
        return self.size == 0

    # Получить последний элемент стека
    def get_top(self):

        # Если стек пуст, ничего не делать
        if self.is_empty():
            return None

        return self.head.next.value

    # Добавить значение в стек
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # Возвращает последнее значение из стека и удаляет его
    def pop(self):
        if self.is_empty():
            raise Exception("Стек пуст")
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.value


stack = Stack()
print("Пуст: " + str(stack.is_empty()))

print("Push:", end=" ")
for i in range(10):
    val = randint(1,10)
    print(val, end=" ")
    stack.push(val)

print("\n\nПуст: " + str(stack.is_empty()))


print("\nPop:", end=" ")

for i in range(stack.get_size()):
    print(stack.pop(), end=" ")
print("\n\nПуст: " + str(stack.is_empty()))
