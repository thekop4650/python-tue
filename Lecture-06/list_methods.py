heroes =['Ironman','Thor','Huik','Superman','Siderman']
h2 = ['Dr.Strang','Cpt. America','Black Panther','Antman']
heroes.insert(0,h2[0])
print(heroes.index('Thor'))
heroes.insert(heroes.index('Thor'),h2[1])
print(heroes)
heroes.remove('Superman')
heroes.append('Antman')
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
newheroes = heroes
newheroes[0] = 'Wonder Women'
print(heroes)
copyheroes =[] +heroes
print(copyheroes)
copyheroes[0] = 'Hanuman'
print(heroes)
print(copyheroes)