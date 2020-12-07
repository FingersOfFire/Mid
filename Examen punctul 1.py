# noinspection PyGlobalUndefined
def exercitiu(string_de_modificat):
    global alte_valori
    patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
    alt_patch = True
    start = 1
    end = 1
    text = input("Introduceti cuvantul inlocuitor")
    start = 5
    end = 14

    patch_temporar = [start, end, text]
    patches.append(patch_temporar)
    string_list = list(string_de_modificat)

    for patch in patches:
        string_de_modificat = string_de_modificat.replace(string_de_modificat[patch[0]-1:patch[1]-1], patch[2])
    print(string_de_modificat)
    return string_de_modificat

string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced"
string_modificat = exercitiu(string)
print(string_modificat)





