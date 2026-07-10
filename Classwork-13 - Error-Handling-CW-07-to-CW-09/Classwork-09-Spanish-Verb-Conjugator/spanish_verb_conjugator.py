# Required Structures
pronouns = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

endings = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# INPUT
verb = input("Write a spanish verb (ar/er/ir): ")

# PROCESS
# Get the stem 
stem = verb[:-2]
# Get the ending 
ending = verb[-2:]

conjugations = endings[ending]

# OUTPUT
for index, pronoun in enumerate(pronouns):
    termination = conjugations[index]
    print(f"{pronoun} {stem}{termination}")