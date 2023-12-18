# Miniprograma que te encuentra la palabra que quieres buscar, te encuentra la primera
# y te dice el número, toma el número y lo aplica en otra variable que hace que te enseñe
# todo el texto despues de la primera palabra especificada.

texto_base = "Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy"

palabra_buscar = (texto_base.find("room"))

print(palabra_buscar)

Resto_de_texto = texto_base[palabra_buscar:]

print(Resto_de_texto)