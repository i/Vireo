import midiutil.MidiFile as MIDIFile

tones = {'1': 69, '2': 70, '3': 71, '4': 72, '5': 73, '6': 74,
         '7': 75, '8': 76, '9': 77, 'A': 78, 'B': 79, 'C': 80,
         'D': 81, 'E': 82, 'F': 83, 'G': 84, 'H': 85, 'I': 86,
         'J': 87, 'K': 88, 'L': 89, 'M': 90, 'N': 91, 'O': 92}

scales = ['13568AC1', '134689B1', '1358A135', '134678B1']


def melodize(tweet, mood):
    if tweet is None:
        return -1
    tweet = str(tweet)
    scale = scales[mood]  # scales[ord(tweet[0]) % 2]
    offset = ord(tweet[0]) % 12
    melody = []

    for i in range(1, len(tweet)):
        scaletone = ord(tweet[i]) % 8
        tone = makeTone(scale, scaletone, offset)
        length = ord(tweet[i]) % 4
        melody.append(str(tones[chr(tone)]) + ' ' + str(length + 1))

    return melody


def makeTone(scale, st, offset):
    n = ord(scale[st])
    if n > 57:
        n = n - ord('A') + 10
    else:
        n = n - ord('0')
    if n + offset > 9:
        return n + offset - 10 + ord('A')
    return n + offset + ord('0')


def midFile(melody):
    MyMIDI = MIDIFile(1)

    track = 0
    time = 0

    MyMIDI.addTrackName(track, time, "Vireo")
    MyMIDI.addTempo(track, time, 340)

    track = 0
    channel = 0
    time = 0
    volume = 100

    for i in melody:
        data = i.split()
        MyMIDI.addNote(track, channel, int(data[0].strip()), time,
                       int(data[1].strip()), volume)
        time = time + int(data[1].strip())

    midi = ""
    binfile = open("./static/test.mid", "wb")
    MyMIDI.writeFile(binfile)
    binfile.close()
    binfile = open("./static/test.mid", "rb")
    midi = binfile.read()
    binfile.close()

    return midi
