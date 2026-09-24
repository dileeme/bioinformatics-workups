def slice_and_join(s, a, b, c, d):
    return s[a:b + 1] + " " + s[c:d + 1]

s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"
a, b, c, d = 22, 27, 97, 102

print(slice_and_join(s, a, b, c, d))
