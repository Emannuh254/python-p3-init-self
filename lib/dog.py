class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name  # Name of the dog
        self.breed = breed  # Breed of the dog, defaulting to "Mutt"

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
