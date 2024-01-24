gon,killua,nen = 'gosto', 'muito', 'hxh'

print('%s %s %s' %(gon,killua,nen))
print('{} {} {}'.format(gon,killua,nen))
print(f'{gon} {killua} {nen}')

#tipos de formatação existentes 


print('{nome}'.format(nome='Luca'))
print('Opa {nome} {sobrenome}, tudo bem?'.format(nome='Gon', sobrenome='Freecs'))

print(f'{nen.upper()}')

nome = 'ração'
print(f'{nome.upper()=!a}')

print(len(f'{nome:20}'))

nomes = ['Luca','Puro Osso','Billy']
idades = [22, 999, 13]

for nome,idade in zip(nomes,idades):
    print(f'{nome:9} {idade}')


gatinho =  'Chiclete'
print(f'{gatinho:*^10}')