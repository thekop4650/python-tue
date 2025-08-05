phonebook = {'Anirach':'777-1111','Mickey':'777-2222','Kop':'777-3333'}
print(phonebook)
print(phonebook['Mickey'])
print(phonebook.get('Kop'))
key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + 'not found in phonebook')
phonebook['Simpson'] ="777-4567"       
phonebook['Pluto'] = "777-9999"
phonebook['Mickey'] = "777-8888"
del phonebook['Simpson']
print(phonebook)