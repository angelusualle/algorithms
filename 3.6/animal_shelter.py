import datetime
class Animal():
    def __init__(self, name, type_animal):
        self.name = name
        self.type = type_animal
        self.date_entered = datetime.datetime.now()
class Animal_Shelter():
    def __init__(self):
        self.dog_head = {}
        self.cat_head = {}
    def enqueue(self, animal):
        if animal.type == 'cat':
            head = self.cat_head
        else:
            head = self.dog_head
        if 'animal' not in head:
            head['animal'] = animal
        else:
            next_one = head
            while 'next' in next_one:
                next_one = next_one['next']
            next_one['next'] = {}
            next_one['next']['animal'] = animal

    def deque_any(self):
        if 'animal' not in self.cat_head and 'animal' not in self.dog_head:
            return None
        elif 'animal' not in self.cat_head:
            return self.deque_dog()
        elif 'animal' not in self.dog_head:
            return self.deque_cat()
        else:
            if self.cat_head['animal'].date_entered < self.dog_head['animal'].date_entered:
                return self.deque_cat()
            else:
                return self.deque_dog()
    def deque_cat(self):
        animal = self.cat_head['animal']
        if 'next' in self.cat_head:
            self.cat_head = self.cat_head['next'] 
        else:
            del self.cat_head['animal']
        return animal
    def deque_dog(self):
        animal = self.dog_head['animal']
        if 'next' in self.dog_head:
            self.dog_head = self.dog_head['next']
        else:
            del self.dog_head['animal']
        return animal