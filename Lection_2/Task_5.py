# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}
dictionary=\
    {
        'up': '^',
        'left': '<',
        'down': 'v',
        'right': '>'
    }
print(dictionary)
print(dictionary['left'])                # Типы ключей могут отличаться  

print(dictionary['up'])
dictionary['up']='upppp'                    # Можно присвоить новое значение переменной        
print(dictionary['up'])


for k in dictionary.keys():              # Можно получить все ключи/значения  
    print(k)

for k in dictionary.values():
    print(k)

for v in dictionary:                     # Можно пробежать по всем элементам словаря
    print(v)
    print(dictionary[v])

