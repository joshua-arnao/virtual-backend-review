name = 'Joshua'

print(name)
# Concatenear valores
# el uso de "," al lado de la variable añaden espacios
print('El nombre es:', name, 'del usuario')

status_marital = 'widower'
# metodo .format() -> Es muy importante para los strings
print('La persona {} es {}'.format(name, status_marital))

print('{1} es una persona {0}'.format(status_marital, name))


# Working directory
# git add . solo agrega los archivos modificados y agregados del nivel actual o novel inferiro
# git add -A agregará TODOS los archivos que pertenezcan al repositorio
# U: Untracked(Sin seguimiento)

# ↓
# Stanting area
# A: Addesd(agregados al staging area)

# ↓
# git directory
