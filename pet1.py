class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.fun = 0

    def eat(self):
        if self.is_alive:
            print(self.name + " goes 'Nom Nom Nom...'")
        else:
            print("Dis boi ded.")

    def sleep(self):
        if self.is_alive:
            print(self.name + " goes 'zzzzzzzzzzzzzz...'")
        else:
            print("Dis boi ded.")

    def play(self):
        if self.is_alive:
            print(self.name + " goes 'Yippee!'")
            self.fun += 1
            print(self.name + "'s fun is now " + self.fun)
        else:
            print("Dis boi ded.")

    def play_together(self, other):
        if self.is_alive:
            print(self.name + " plays with " + other.name)
            self.fun += 1
            print(self.name + "'s fun is now " + str(self.fun))
            other.fun += 1
            print(other.name + "'s fun is now " + str(other.fun))
        else:
            print("Dis boi ded.")

    def rotate_right(self):
        if self.is_alive:
            self.direction += 1

            if self.direction == 4:
                self.direction = 0
        else:
            print("Dis boi ded.")

    def rotate_left(self):
        if self.is_alive:
            self.direction -= 1

            if self.direction == -1:
                self.direction = 3
        else:
            print("Dis boi ded.")

    def move(self):
        if self.is_alive:
            if self.direction == 0:
                self.y += 1
            elif self.direction == 1:
                self.x += 1
            elif self.direction == 2:
                self.y -= 1
            elif self.direction == 3:
                self.x -= 1
        else:
            print("Dis boi ded.")

    def kill(self, other):
        print(self.name + " kills " + other.name + "!")
        other.is_alive = False

    def resurect(self, other):
        print(self.name + " resurects " + other.name + "!")
        other.is_alive = True
  
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
    
pet1 = Pet("Eric Foreman")
pet2 = Pet("Edgy")
pet3 = Pet("Mikey")

