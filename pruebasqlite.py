import sqlite3

conexion = sqlite3.connect('data')
tabla = conexion.cursor()

# crear tabla
tabla.execute('''create table productos
(clave text, descripcion text, precio real)''')

# insertar datos
for t in (('aa101', 'PRODUCTO 101', 445.00),
('bb202', 'PRODUCTO 202', 742.00),
('cc303', 'PRODUCTO 303', 457.00),
):
          tabla.execute('insert into productos values (?,?,?)', t)

conexion.commit()
tabla.close()
