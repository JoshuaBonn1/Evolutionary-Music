import piece
import random
import heapq
from copy import deepcopy

class Generation:

    def __init__(self, size, elite, mutate, tournament, mood):
        self.size = size
        self.elite = elite
        self.mutate = mutate
        self.tournament = tournament
        self.mood = mood
        self.crossover_method = 'one-point'
        self._createGeneration()
    
    def _createGeneration(self):
        self.pieces = []
        for _ in xrange(self.size):
            self.pieces.append(piece.Piece(self.mood))
        self.best = max(self.pieces, key=lambda x: x.fitness)
        self.worst = min(self.pieces, key=lambda x: x.fitness)
    
    def run(self, generations, desired_length=5):
        # for g in xrange(generations):
        try:
            g = 0
            while True:
                length = len(self.pieces)    
                elite_num = int(self.elite * length)
                new_pieces = heapq.nlargest(elite_num, self.pieces, key=lambda x: x.fitness)
                
                while len(new_pieces) < length:
                    child1, child2 = self.crossover(self.selection(), self.selection())
                    child1.mutate(self.mutate)
                    child2.mutate(self.mutate)
                    child1.findFitness(desired_length=desired_length)
                    child2.findFitness(desired_length=desired_length)
                    new_pieces.append(child1)
                    new_pieces.append(child2)
                
                if len(new_pieces) > length:
                    new_pieces = new_pieces[:-1]
                
                self.pieces = new_pieces
                self.best = max(self.pieces, key=lambda x: x.fitness)
                self.worst = min(self.pieces, key=lambda x: x.fitness)
                avg_fit = sum([p.fitness for p in self.pieces]) / float(len(self.pieces))
                print 'Generation ' + str(g) + ': Best Fitness: ' + str(self.best.fitness) + '; Average Fitness: ' + str(avg_fit)
                g += 1
        except KeyboardInterrupt as e:
            print e
            print 'Finished generations'
    
    def crossover(self, piece1, piece2):
        child1 = deepcopy(piece1)
        child2 = deepcopy(piece2)
        child1.crossover(child2, method=self.crossover_method)
        return child1, child2
    
    def selection(self):
        # Tournament Selection
        try:
            selection = random.sample(self.pieces, self.tournament)
        except ValueError:
            selection = self.pieces
        return max(selection, key=lambda x: x.fitness)

    def __str__(self):
        r = 'Generation Info:' + '\n'
        r += '\tPopulation Size: ' + str(self.size) + '\n'
        r += '\tMutation Rate: ' + str(self.mutate) + '\n'
        r += '\tElite Percentage: ' + str(self.elite) + '\n'
        r += '\tTournament Size: ' + str(self.tournament) + '\n'
        r += '\tMood: ' + str(self.mood) + '\n'
        return r