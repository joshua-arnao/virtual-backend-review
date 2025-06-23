from camelcase import CamelCase

instaciaCC = CamelCase('mundo', 'del')

texto = 'Bienvenidos al mundo del backend'

print(instaciaCC.hump(texto))
