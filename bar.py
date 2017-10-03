import random

lengths = {1.0: 'w', 0.5: 'h', 0.25: 'q', 0.125: 'e', 0.0625: 's'}

class Bar:
    def __init__(self, range):
        self.note_tree = NoteNode(1.0, range)
    
    def getNotes(self):
        return self.note_tree.getNotes()
    
    def sumPitch(self):
        return self.note_tree.sumPitch()
    
    def numNotes(self):
        return self.note_tree.numNotes()
    
    def sumVolume(self):
        return self.note_tree.sumVolume()
    
    def mutate(self, rate):
        self.note_tree.mutate(rate)
    
    def __str__(self):
        return str(self.note_tree)

class NoteNode:
    def __init__(self, length, range):
        if length <= 0.125:
            self.left = Note(length/2, range)
            self.right = Note(length/2, range)
        else:
            self.left = random.choice((NoteNode, Note))(length/2, range)
            self.right = random.choice((NoteNode, Note))(length/2, range)
    
    def getNotes(self):
        return self.left.getNotes() + self.right.getNotes()
    
    def sumPitch(self):
        return self.left.sumPitch() + self.right.sumPitch()
    
    def numNotes(self):
        return self.left.numNotes() + self.right.numNotes()
    
    def sumVolume(self):
        return self.left.sumVolume() + self.right.sumVolume()
    
    def mutate(self, rate):
        self.left.mutate(rate)
        self.right.mutate(rate)
    
    def __str__(self):
        return str(self.left) + str(self.right)

class Note:
    def __init__(self, length, range):
        self.length = length #or lengths[length]
        self.range = range
        self.volume = random.uniform(0, 6)
        self.setValue()
    
    def setValue(self):
        if self.range == 'uniform':
            self.value = random.randint(0, 87)
        else:
            self.value = int(random.gauss(float(self.range[1] + self.range[0]) / 2.0, 
                                          self.range[1] - self.range[0]))
        self.checkValue()
        #self.checkMode()
    
    def checkValue(self):
        if self.value < 0:
            self.setValue()
        if self.value > 87:
            self.setValue()

    def checkMode(self):
        while self.value % 12 not in mode:
            self.value += random.choice((-1, 1))
            if self.value < 0:
                self.value = 0
            elif self.value > 87:
                self.value = 87
            
    def getNotes(self):
        return [self.value]
     
    def sumPitch(self):
        return self.value
    
    def numNotes(self):
        return 1
    
    def sumVolume(self):
        return self.volume
    
    def mutate(self, rate):
        if rate > random.random():
            self.volume += random.uniform(-1, 1)
            if self.volume > 6:
                self.volume = 5.9
            elif self.volume < 0:
                self.volume = 0
            self.value += random.randint(-4, 4)
            if self.value < 0:
                self.value = 0
            elif self.value > 87:
                self.value = 87
        #self.checkMode()
    
    def __str__(self):
        return str(self.value) + ',' + lengths[self.length] + ',' + str(self.volume) + ' '