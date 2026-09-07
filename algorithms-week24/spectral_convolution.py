from collections import Counter

def spectral_convolution(spectrum):
    diffs = []
    for i in range(len(spectrum)):
        for j in range(len(spectrum)):
            if i != j:
                diff = spectrum[i] - spectrum[j]
                if diff > 0:
                    diffs.append(diff)
    return diffs

spectrum = [0, 137, 186, 323]

counts = Counter(spectral_convolution(spectrum))
ordered = sorted(counts.items(), key=lambda item: -item[1])
result = []
for value, count in ordered:
    result.extend([value] * count)

print(" ".join(str(v) for v in result))
