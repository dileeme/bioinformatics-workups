def even_lines(text):
    lines = text.strip("\n").split("\n")
    return [line for i, line in enumerate(lines, start=1) if i % 2 == 0]

text = """Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat"""

for line in even_lines(text):
    print(line)
