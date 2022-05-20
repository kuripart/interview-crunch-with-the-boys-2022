from dataclasses import dataclass
from nis import cat
import string
from enum import Enum


class EmptyException(Exception):
    pass


class AnimalType(Enum):
    CAT = 1
    DOG = 2


@dataclass
class Animal:
    name: string
    index: int
    type: AnimalType

    def __init__(self, name, index, type) -> None:
        self.name = name
        self.index = index
        self.type = type


@dataclass
class Cat: Animal


@dataclass
class Dog: Animal


@dataclass
class Queue:
    data: list
    start_index: int

    def is_empty(self):
        return self.start_index == len(self.data)

    def top(self):
        if self.is_empty():
            raise EmptyException("oops queue empty")
        return self.data[self.start_index]
    
    def pop(self):
        if self.is_empty():
            raise EmptyException("oops queue empty")
        top_val = self.top()
        self.start_index += 1
        return top_val
        
    def push(self, val):
        self.data.append(val)
    
    def get_queue_len(self):
        return len(self.data)

    def __init__(self):
        self.data = []
        self.start_index = 0


@dataclass
class AnimalQueue:
    dog_queue: Queue
    cat_queue: Queue
    index_counter: int

    def is_empty(self):
        return self.dog_queue.is_empty() and self.cat_queue.is_empty()

    def top(self):
        dog_top = None
        cat_top = None

        if not self.dog_queue.is_empty():
            dog_top = self.dog_queue.top()
        if not self.cat_queue.is_empty():
            cat_top = self.cat_queue.top()
        
        if dog_top == None and cat_top != None:
            return cat_top
        if dog_top != None and cat_top == None:
            return dog_top

        if dog_top.index > cat_top.index:
            return cat_top
        else:
            return dog_top

    def dequeue_cat(self):
        return self.cat_queue.pop();

    def dequeue_dog(self):
        return self.dog_queue.pop();

    def dequeue_any(self):
        dog_top = None
        cat_top = None

        if not self.dog_queue.is_empty():
            dog_top = self.dog_queue.top()
        if not self.cat_queue.is_empty():
            cat_top = self.cat_queue.top()
        
        if dog_top == None and cat_top != None:
            return self.cat_queue.pop()
        if dog_top != None and cat_top == None:
            return self.dog_queue.pop()
        
        if dog_top.index > cat_top.index:
            return self.cat_queue.pop()
        else:
            return self.dog_queue.pop()


    def push(self, name, type):
        if type == AnimalType.CAT:
            self.cat_queue.push(Animal(name, self.index_counter, type))
        else:
            self.dog_queue.push(Animal(name, self.index_counter, type))
        self.index_counter += 1

    def __init__(self) -> None:
        self.dog_queue = Queue()
        self.cat_queue = Queue()
        self.index_counter = 0


animal_q = AnimalQueue()
animal_q.push("C1", AnimalType.CAT)
animal_q.push("D1", AnimalType.DOG)
animal_q.push("C2", AnimalType.CAT)
animal_q.push("D2", AnimalType.DOG)
animal_q.push("D3", AnimalType.DOG)
animal_q.push("D4", AnimalType.DOG)
animal_q.push("C3", AnimalType.CAT)
animal_q.push("C4", AnimalType.CAT)
animal_q.push("D5", AnimalType.DOG)
animal_q.push("C5", AnimalType.CAT)

print(animal_q.top())
print(animal_q.dequeue_any())
print(animal_q.dequeue_any())
print(animal_q.dequeue_dog())
print(animal_q.dequeue_cat())
print(animal_q.dequeue_any())

