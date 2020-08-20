human_characteristics = {
    "hair_color": {
        "black": "CCAGCAATCGC",
        "brown": "GCCAGTGCCG",
        "blonde": "TTAGCTATCGC"
    },
    "face_shape": {
        "square": "GCCACGG",
        "round": "ACCACAA",
        "oval": "AGGCCTCA"
    },
    "eye_color": {
        "blue": "TTGTGGTGGC",
        "green": "GGGAGGTGGC",
        "brown": "AAGTAGTGAC"
    },
    "gender": {
        "female": "TGAAGGACCTTC",
        "male": "TGCAGGAACTTC"
    },
    "race": {
        "white": "AAAACCTCA",
        "black": "CGACTACAG",
        "asian": "CGCGGGCCG"
    }
}


suspects_characteristics = {
    "Eva": {
        "gender": "female",
        "race": "white",
        "hair_color": "blond",
        "eye_color": "blue",
        "face_shape": "oval"
    },
    "Larisa": {
        "gender": "female",
        "race": "white",
        "hair_color": "brown",
        "eye_color": "brown",
        "face_shape": "oval"
    },
    "Matej": {
        "gender": "male",
        "race": "white",
        "hair_color": "black",
        "eye_color": "blue",
        "face_shape": "oval"
    },
    "Miha": {
        "gender": "male",
        "race": "white",
        "hair_color": "brown",
        "eye_color": "green",
        "face_shape": "square"
    }
}

with open("perpetrators_dna.txt", "r") as dna_file:
    perpetrators_dna = dna_file.read()

print("The perpetrator's DNA matches with suspect's DNA sequences stated below: ")

for key, value in human_characteristics.items():
    for characteristic, dna_sequence in value.items():
        if perpetrators_dna.find(dna_sequence) != -1:
            suspects_characteristics[key] = characteristic
            print(characteristic, dna_sequence)
            break

name = ''

for x, value in suspects_characteristics.items():
    current_name = ''

    for k, v in value.items():
        if suspects_characteristics[k] == v:
            current_name = x
        else:
            current_name = ''
            break

    if current_name:
        name = current_name
        break

print("The perpetrator is: {0}".format(name.upper()))
