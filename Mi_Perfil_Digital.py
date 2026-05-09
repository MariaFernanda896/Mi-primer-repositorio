#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Maira Fernanda Baños Prieto"
edad = 15
estatura = 1.63
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("Mariafernanda896", "Ferx__bp")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Lugar Seguro", "artista": "jay wheeler y noreh", "duracion": "3:04"},
{"titulo": "Ordinary", "artista":"Alex warren", "duracion": "3:24"},
{"titulo": "En el proximo big bang", "artista": "Wuicho kun y Orión", "duracion": "3:07"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:")
for cancion in Playlist: 
 print(f"{cancion['titulo']} - {cancion['artista']})({cancion['duracion']})min")
print ("----------------------------------")