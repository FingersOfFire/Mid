from collections import Counter

lista_nume = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']

print(sorted(('Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu')))

for vote in set(lista_nume):
    print("{0} - voted {1} times".format(vote, str(lista_nume.count(vote))))

word: str
aparitie_deasa_cuvinte = [word for word, word_count in Counter(lista_nume).most_common(3)]

print(aparitie_deasa_cuvinte)

aparitie_rara_cuvinte = Counter(lista_nume).most_common()[-1]

print(aparitie_rara_cuvinte)