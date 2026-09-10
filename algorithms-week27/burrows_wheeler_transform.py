def burrows_wheeler_transform(text):
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    rotations.sort()
    return "".join(rotation[-1] for rotation in rotations)

text = "banana$"

print(burrows_wheeler_transform(text))
