import random
from string import punctuation


def lese_von_datei(dateiname):
    with open(dateiname, "r", encoding="utf-8") as datei:
        inhalt = datei.read().splitlines()
    return inhalt

def read_file(file):
    with open(file) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def generate_password(adjectives_path, nouns_path):
    adjectives = read_file(adjectives_path)
    nouns = read_file(nouns_path)

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(0, 100)
    sc = random.choice(punctuation)

    password = adjective + noun + str(number) + sc
    return password