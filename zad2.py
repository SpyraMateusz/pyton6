def unikalne_elementy(lista):
    zbior_unikalnych = set(lista)
    lista_unikalnych = list(zbior_unikalnych)
    return lista_unikalnych

# Przykładowe użycie
moja_lista = [1, 2, 3, 4, 2, 3, 5]
unikalne = unikalne_elementy(moja_lista)
print("Oryginalna lista:", moja_lista)
print("Unikalne elementy:", unikalne)