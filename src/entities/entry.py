from random import randrange

class Entry:

    def __init__(self):
        pass

    def generate_key(self, title:str):
        return f"{title.split(' ')[0]}{randrange(999999999)}"