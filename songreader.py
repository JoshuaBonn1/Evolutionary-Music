import music21
import glob
import time

def addpitch(p):
    try:
        dict[currkey.solfeg(p)] += 1
    except KeyError:
        dict[currkey.solfeg(p)] = 1

dict = {}
good = 0
total = 0
for filename in glob.glob('midi/*.mid'):
    #filename = 'midi/BanjoKazooie - Freezeezy Peak.mid'
    mf = music21.midi.MidiFile()
    mf.open(filename)
    mf.read()
    mf.close()
    print 'reading ' + filename
    test = music21.midi.translate.midiFileToStream(mf)
    print 'Read ' + filename
    currkey = music21.key.Key()
    for part in test:
        for a in part:
            if isinstance(a, music21.key.Key):
                currkey = a
            elif isinstance(a, music21.note.Note):
                addpitch(a.pitch)
            elif isinstance(a, music21.stream.Voice):
                for chordrest in a:
                    if isinstance(chordrest, music21.chord.Chord):
                        for pitch in chordrest.pitches:
                            addpitch(pitch)
                    elif isinstance(chordrest, music21.note.Note):
                        addpitch(chordrest.pitch)
            
        # for chord in part[7]:
            # if isinstance(chord, music21.chord.Chord):
                # for pitch in chord.pitches:
                    # print pitch
            # elif isinstance(chord, music21.note.Note):
                # print chord.pitch
            # else:
                # print chord
    print dict
    # mid.ticks_per_beat = 96
    # mid.beats_per_minute = 120
    # print filename
    # messages = [t for t in mid.tracks]
    # #messages.sort(key=lambda message: message.time)
    # for m in messages:
        # m.sort(key=lambda message: message.time)
        # for mes in m:
            # print mes

    # print mid.type
    # break
    # try:
        # total += 1
        # result = midi_in.MIDI_to_Composition(filename)
    # except (midi_in.FormatError, 
            # midi_in.HeaderError, ValueError,
            # exceptions.NoteFormatError) as e:
        # #print e
        # print filename
        # continue
    # print filename
    # good += 1
    # for n in result[0].tracks[1].get_notes():
        # for note in n[2].notes:
            # note_name = str(note).split('-')[0][1:]
            # try:
                # dict[note_name] += 1
            # except KeyError:
                # dict[note_name] = 1
# print dict
# print good, total
    
#for t in result[0].tracks:
# song = result[0]
# melody = song.tracks[1]
# print song.tracks[0]
# print len(melody)
# for b in melody.bars:
    # try:
        # print b.key.key
    # except AttributeError:
        # print b.key
    #print b.determine_progression()
# for n in result[0].tracks[1].get_notes():
    # mcc.determine(n[2])
    # for note in n[2].notes:
        # note_name = str(note).split('-')[0][1:]
        # try:
            # dict[note_name] += 1
        # except KeyError:
            # dict[note_name] = 1

        # sum_velocities += int(note.velocity)
        # sum_pitches += int(note) - 9
        # num_notes += 1
# print float(sum_pitches) / float(num_notes)
# print float(sum_velocities) / float(num_notes)
# print dict