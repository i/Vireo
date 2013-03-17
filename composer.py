

tones = {'1': 'a', '2': 'a#', '3': 'b', '4': 'c', '5': 'c#', '6': 'd',
         '7': 'd#', '8': 'e', '9': 'f', 'A': 'f#', 'B': 'g', 'C': 'g#',
         'D': 'A', 'E': 'A#', 'F': 'B', 'G': 'C', 'H': 'C#', 'I': 'D',
         'J': 'D#', 'K': 'E', 'L': 'F', 'M': 'F#', 'N': 'G', 'O': 'G#'}

scales = ['13568AC1', '134689B1']


def melodize(tweet, mood):
    if tweet is None:
        return -1
    scale = mood  # scales[ord(tweet[0]) % 2]
    offset = ord(tweet[0]) % 12
    melody = []

    for i in range(1, len(tweet)):
        scaletone = ord(tweet[i]) % 8
        tone = makeTone(scale, scaletone, offset)
        length = ord(tweet[i]) % 4
        melody.append(tones[chr(tone)] + ' ' + str(2**length))

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
