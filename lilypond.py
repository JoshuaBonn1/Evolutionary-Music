from bar import lengths

note_names = ('a', 'ais', 'b', 'c', 'cis', 'd', 'dis', 'e', 'f', 'fis', 'g', 'gis')

volumes = ('\\pp', '\\p', '\\mp', '\\mf', '\\f', '\\ff')

def printPiece(piece, filename):
    f = open(filename, 'w')
    f.write("\\score{\n")
    f.write('\t{ ')
    for bar in piece.bars:
        str_bar = str(bar)
        for note in str_bar.split(' '):
            if note == '':
                break
            val, dur, volume = note.split(',')
            duration = ''
            for fraction, name in lengths.iteritems():
                if dur == name:
                    duration = str(int(1.0/ float(fraction)))
            f.write(_valToNote(val) + duration + volumes[int(float(volume))] + ' ')
    f.write('}')
    f.write("\n\t\\midi{\n")
    f.write("\t\t\\tempo 4 = " + str(piece.tempo))
    f.write("\n\t}\n")
    f.write("\t\\layout{}\n")
    f.write("}")

def printBar(bar, filename):
    f = open(filename, 'w')
    f.write("\\score{\n")
    f.write('\t{ ')
    str_bar = str(bar)
    for note in str_bar.split(' '):
        if note == '':
            break
        val, dur, volume = note.split(',')
        duration = ''
        for fraction, name in lengths.iteritems():
            if dur == name:
                duration = str(int(1.0/ float(fraction)))
        f.write(_valToNote(val) + duration + volumes[int(float(volume))] + ' ')
    f.write('}')
    f.write("\n\t\\midi{}\n")
    f.write("\t\\layout{}\n")
    f.write("}")

def _valToNote(note):
    assert note < 0 or note > 87, 'Must be between 0 and 88'
    result = int(note) % 12
    note_name = note_names[result]
    trailing = ''
    if 0 <= int(note) < 4: 
        trailing = ',,,'
    elif 4 <= int(note) < 16: 
        trailing = ',,'
    elif 16 <= int(note) < 28: 
        trailing = ','
    elif 28 <= int(note) < 40: 
        trailing = ''
    elif 40 <= int(note) < 52: 
        trailing = "'"
    elif 52 <= int(note) < 64: 
        trailing = "''"
    elif 64 <= int(note) < 87: 
        trailing = "'''"
    elif int(note) == 87: 
        trailing = "''''"
    else:
        trailing = 'ERROR'
    return note_name + trailing
    