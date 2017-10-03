import bar
import random

lydian = (0, 2, 3, 5, 7, 9, 10)
ionian = (0, 2, 3, 5, 7, 8, 10)
mixolydian = (0, 1, 3, 5, 7, 8, 10)
dorian = (0, 1, 3, 5, 6, 8, 10)
aeolian = (1, 3, 5, 6, 8, 10, 11)
phrygian = (1, 3, 4, 6, 8, 10, 11)
locrian = (1, 3, 4, 6, 8, 9, 11)
mode = locrian

class Piece:
    solfege = {'do': 0.1987, 'di': 0.0424, 're': 0.0871, 'ri': 0.0265, 'mi': 0.1178, 'fa': 0.0944, 'fi': 0.037, 'sol': 0.1668, 'si': 0.0657, 'la': 0.057, 'li': 0.0381, 'ti': 0.0693}


    moods = {'happy': {'intensity': (0.4, 0.6), 
                       'timbre': (0.4, 0.6),
                       'pitch': (70, 87),
                       'rhythm': (184, 220)},
             'exuberant': {'intensity': (0.6, 0.8), 
                           'timbre': (0.4, 0.6),
                           'pitch': (52, 69),
                           'rhythm': (148, 184)},
             'energetic': {'intensity': (0.8, 1.0), 
                           'timbre': (0.4, 0.6),
                           'pitch': (34, 51),
                           'rhythm': (148, 184)},
             'frantic': {'intensity': (0.6, 0.8), 
                         'timbre': (0.8, 1.0),
                         'pitch': (16, 33),
                         'rhythm': (184, 220)},
             'sad': {'intensity': (0.4, 0.6), 
                     'timbre': (0.0, 0.2),
                     'pitch': (0, 16),
                     'rhythm': (76, 112)},
             'depression': {'intensity': (0.2, 0.4), 
                            'timbre': (0.2, 0.4),
                            'pitch': (16, 33),
                            'rhythm': (76, 112)},
             'calm': {'intensity': (0.0, 0.2), 
                      'timbre': (0.0, 0.2),
                      'pitch': (34, 51),
                      'rhythm': (40, 76)},
             'contentment': {'intensity': (0.2, 0.4), 
                             'timbre': (0.2, 0.4),
                             'pitch': (52, 69),
                             'rhythm': (76, 112)}}
                             
    def __init__(self, mood, length='random'):
        self.mood = mood
        if length == 'random':
            self.bars = [bar.Bar(self.moods[mood]['pitch']) for _ in xrange(random.randint(5, 10))]
        else:
            self.bars = [bar.Bar(self.moods[mood]['pitch']) for _ in xrange(int(length))]
        self.tempo = random.randint(self.moods[mood]['rhythm'][0], self.moods[mood]['rhythm'][1])
        self.findFitness()
    
    def info(self):
        notes = self.getNotes()
        num_notes = float(len(notes))
        sum_notes = sum(notes)
        normalized_notes = [n % 12 for n in notes]  
        
        percent = lambda x: normalized_notes.count(x) / num_notes
        do_val = percent(3)
        di_val = percent(4)
        re_val = percent(5)
        ri_val = percent(6)
        mi_val = percent(7)
        fa_val = percent(8)
        fi_val = percent(9)
        sol_val = percent(10)
        si_val = percent(11)
        la_val = percent(0)
        li_val = percent(1)
        ti_val = percent(2)
        
        
        print self.getSolfegeError('do', do_val)
        print self.getSolfegeError('di', di_val)
        print self.getSolfegeError('re', re_val)
        print self.getSolfegeError('ri', ri_val)
        print self.getSolfegeError('mi', mi_val)
        print self.getSolfegeError('fa', fa_val)
        print self.getSolfegeError('fi', fi_val)
        print self.getSolfegeError('sol', sol_val)
        print self.getSolfegeError('si', si_val)
        print self.getSolfegeError('la', la_val)
        print self.getSolfegeError('li', li_val)
        print self.getSolfegeError('ti', ti_val)
    
    def getSolfegeError(self, solfege, value):
        return (abs(self.solfege[solfege] - value)*100)**2/100
    
    def findFitness(self, desired_length=None):
        self.fitness = 0
        target_intensity = self.moods[self.mood]['intensity']
        target_timbre = self.moods[self.mood]['timbre']
        target_pitch = self.moods[self.mood]['pitch']
        target_rhythm = self.moods[self.mood]['rhythm']
        
        # Penalize for departure from desired length
        if desired_length is not None:
            self.fitness -= abs(len(self.bars) - desired_length)
        
        notes = self.getNotes()
        num_notes = float(len(notes))
        sum_notes = sum(notes)
        normalized_notes = [n % 12 for n in notes]  
        
        percent = lambda x: normalized_notes.count(x) / num_notes
        do_val = percent(3)
        di_val = percent(4)
        re_val = percent(5)
        ri_val = percent(6)
        mi_val = percent(7)
        fa_val = percent(8)
        fi_val = percent(9)
        sol_val = percent(10)
        si_val = percent(11)
        la_val = percent(0)
        li_val = percent(1)
        ti_val = percent(2)
        
        # Penalize for distance away from average
        self.fitness -= self.getSolfegeError('do', do_val)
        self.fitness -= self.getSolfegeError('di', di_val)
        self.fitness -= self.getSolfegeError('re', re_val)
        self.fitness -= self.getSolfegeError('ri', ri_val)
        self.fitness -= self.getSolfegeError('mi', mi_val)
        self.fitness -= self.getSolfegeError('fa', fa_val)
        self.fitness -= self.getSolfegeError('fi', fi_val)
        self.fitness -= self.getSolfegeError('sol', sol_val)
        self.fitness -= self.getSolfegeError('si', si_val)
        self.fitness -= self.getSolfegeError('la', la_val)
        self.fitness -= self.getSolfegeError('li', li_val)
        self.fitness -= self.getSolfegeError('ti', ti_val)

        
        # Reward for intensity within range, penalize for larger values outside range
        avg_intensity = float(self.sumVolume()) / num_notes
        if target_intensity[0]*6 <= avg_intensity <= target_intensity[1]*6:
            self.fitness += 1
        elif target_pitch[0]*6 > avg_intensity:
            self.fitness -= (avg_intensity - target_intensity[0]*6)**2
        else:
            self.fitness -= (avg_intensity - target_intensity[1]*6)**2
        
        # Reward for pitch within range, penalize for larger values outside range
        # avg_pitch = float(sum_notes) / num_notes
        for n in notes:
            if target_pitch[0] > n:
                self.fitness -= ((n - target_pitch[0])/10)**2
            elif target_pitch[1] < n:
                self.fitness -= ((n - target_pitch[1])/10)**2
        # if target_pitch[0] <= avg_pitch <= target_pitch[1]:
            # self.fitness += 1
        # elif target_pitch[0] > avg_pitch:
            # self.fitness -= (avg_pitch - target_pitch[0])**2
        # else:
            # self.fitness -= (avg_pitch - target_pitch[1])**2
        
        # Reward for rhythm within range, penalize for larger values outside range
        if target_rhythm[0] <= self.tempo <= target_rhythm[1]:
            self.fitness += 1
        elif target_rhythm[0] > self.tempo:
            self.fitness -= (self.tempo - target_rhythm[0])**2
        else:
            self.fitness -= (self.tempo - target_rhythm[1])**2
    
    def getNotes(self):
        notes = []
        for b in self.bars:
            notes.extend(b.getNotes())
        return notes
    
    def sumPitch(self):
        return sum([b.sumPitch() for b in self.bars])
    
    def numNotes(self):
        return sum([b.numNotes() for b in self.bars])
    
    def sumVolume(self):
        return sum([b.sumVolume() for b in self.bars])
    
    def mutate(self, rate):
        for b in self.bars:
            b.mutate(rate)
    
    def crossover(self, other, method='one-point'):
        if method == 'one-point':
            crossover_point_self = random.randint(1, len(self.bars)-1)
            crossover_point_other = random.randint(1, len(other.bars)-1)
            self.bars[crossover_point_self:], other.bars[crossover_point_other:] = \
              other.bars[crossover_point_other:], self.bars[crossover_point_self:]
        else:
            assert True, 'Method not implemented yet'
    
    def __str__(self):
        full = ''
        for bar in self.bars:
            full += str(bar)
        return full