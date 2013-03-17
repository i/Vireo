

tones = {'1': 'a4', '2': 'a#4', '3': 'b4', '4': 'c4', '5': 'c#4', '6': 'd4',
         '7': 'd#4', '8': 'e4', '9': 'f4', 'A': 'f#4', 'B': 'g4', 'C': 'g#4',
         'D': 'a5', 'E': 'a#5', 'F': 'b', 'G': 'c', 'H': 'c#5', 'I': 'd5',
         'J': 'd#5', 'K': 'e5', 'L': 'f5', 'M': 'f#5', 'N': 'g5', 'O': 'g#5'}

scales = ['13568AC1', '134689B1']


def melodize(tweet, mood):
    if tweet is None:
        return -1
    scale = scales[mood]  # scales[ord(tweet[0]) % 2]
    offset = ord(tweet[0]) % 12
    melody = []

    for i in range(1, len(tweet)):
        scaletone = ord(tweet[i]) % 8
        tone = makeTone(scale, scaletone, offset)
        length = ord(tweet[i]) % 4
        melody.append(tones[chr(tone)] + ' ' + str(2**(length + 6)))

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
