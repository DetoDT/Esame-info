domandef = 'domande1.txt'
filepersonaggi = open('personaggi.txt', 'r')
filedomande = open(domandef, 'r')

personaggi = filepersonaggi.readlines()
domande = filedomande.readlines()
dizionario_personaggi = {}
dizionario_indici = {'Sesso': 1,
                     'Colore Capelli': 2,
                     'Lunghezza Capelli':3,
                     'Occhiali':4,
                     'Capelli':5,
                     'Baffi':6,
                     'Barba':7,
                     'Pelato':8}

# Creo una lista con i nomi dei personaggi

c = False
nomi_personaggi = []
for i in personaggi:
    i = i.strip('\n').split(';')
    if c:
        dizionario_personaggi[i[0]] = [n for n in i]
        nomi_personaggi.append(i[0])
    else:
        c = True

# Stampo i personaggi del gioco e le loro caratteristiche     

print('Personaggi del gioco:')
count = False
for i in personaggi:
    i = i.strip('\n').split(';')
    if count == True:
        d = dizionario_personaggi[i[0]]
        print(f'{i[0]}: Sesso: {d[1]}, Colore Capelli: {d[2]}, Lunghezza capelli: {d[3]}, Occhiali: {d[4]}, Capelli: {d[5]}, Baffi {d[6]}, Barba: {d[7]}, Pelato: {d[8]}')
    else:
        count = True

# Filtro i personaggi in base alle domande inserendoli in un lista l e togliendo coloro che
# non rispecchiano le caratteristiche richieste  
      
l = list(nomi_personaggi)
z = 1
for domanda in domande:
    
    print(f'\nMossa {z} - domanda: {domanda}')
    z+=1
    print('Personaggi selezionati:')
    domanda = domanda.strip('\n').split('=')

    for i in dizionario_personaggi:
        n = dizionario_personaggi[i]
        index = int(dizionario_indici[domanda[0]])
        if domanda[1] == 'True':
            if i in l and n[index] == 'NO':
                l.remove(i)
        elif domanda[1] == 'False':
            if i in l and n[index] == 'SI':
                l.remove(i)
        elif domanda[1] != n[index] and index<4:
            if i in l:
                l.remove(i)
    for p in l:
        print(p) 

# Controllo se si ha vinto o perso
         
if len(l) == 1:
    print("\nGioco terminato, hai vinto! E' stato selezionato: ")
    d = dizionario_personaggi[l[0]]
    print(f'{l[0]}: Sesso: {d[1]}, Colore Capelli: {d[2]}, Lunghezza capelli: {d[3]}, Occhiali: {d[4]}, Capelli:{d[5]}, Baffi: {d[6]}, Barba: {d[7]}, Pelato: {d[8]}')
else:
    print('\nPeccato, hai perso!')
