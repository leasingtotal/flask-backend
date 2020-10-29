import bcrypt
from cnx import conn


def validar_usuarios(usuario, clave):
    try:
        cursor = conn.cursor()
        query = f"select * from usuarios where usuario='{usuario}' and clave='{clave}'"
        cursor.execute(query)
        data = cursor.fetchall()

        for datos in data:
            id = datos[0]
            nombre = datos[1]
            user = datos[2]
            cla = datos[3]
            estado = datos[4]
            mail = datos[5]

        if usuario == user and clave == cla:
            enc = cla.encode()
            sal = bcrypt.gensalt()
            hashpass = bcrypt.hashpw(enc,sal)
            print(hashpass)
            retorno = [{
                "status": "200",
                "id": id,
                "nombre": nombre,
                "usuario": user,
                "clave": str(hashpass),
                "activo": estado,
                "mail": mail
            }]
            return retorno
    except Exception as e:
        data = [{
            "status": "400",
            "detalle": str(e),
            "simple": "No se encontraron datos"
        }]
        return data


def crear_usuario(usuario, clave, nombre, email):
    try:
        cursor = conn.cursor()
        query = f"""INSERT INTO public.usuarios(nombre, usuario, clave, status, email) 
        VALUES ('{nombre}', '{usuario}', '{clave}', 'A', '{email}')"""
        cursor.execute(query)
        conn.commit()
        datos = [{
            "status": "200",
            "descripcion": "Se ha registrado el usuario correctamente"
        }]
        return datos

    except Exception as e:
        data = [{
            "status": "400",
            "detalle": str(e)
        }]
        return data

def validar_correo(mail):
    return 'hola'