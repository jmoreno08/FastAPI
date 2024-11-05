import bcrypt

# Contraseña a encriptar
password = b'Chamorro86*'

# Generar un salt con el factor de costo de 12
salt = bcrypt.gensalt(rounds=12)

# Generar el hash de la contraseña
hashed = bcrypt.hashpw(password, salt)

# Mostrar el hash resultante
print(hashed.decode())