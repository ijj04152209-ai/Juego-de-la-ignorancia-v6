import pymysql

def registrar_jugadores(nombre1, nombre2, nombre3):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM jugadores")

    cursor.execute("INSERT INTO jugadores (id_jugador, nombre, puntos) VALUES (1, %s, 0)", (nombre1,))
    cursor.execute("INSERT INTO jugadores (id_jugador, nombre, puntos) VALUES (2, %s, 0)", (nombre2,))
    cursor.execute("INSERT INTO jugadores (id_jugador, nombre, puntos) VALUES (3, %s, 0)", (nombre3,))

    conn.commit()
    conn.close()


def recupera_categoria():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()
    cursor.execute('select descripcion from categoria')
    categorias = cursor.fetchall()
    conn.close()
    return categorias

def recupera_preguntas(cat):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()

    consulta = '''
    SELECT p.id_pregunta, p.pregunta,
           o.opcion_1, o.opcion_2, o.opcion_3, o.opcion_4, o.es_correcta
    FROM categoria c, preguntas p, opciones o
    where c.descripcion=%s
    AND p.id_categoria=c.id_categoria
    AND o.id_pregunta=p.id_pregunta
    '''

    cursor.execute(consulta, (cat,))
    preguntas = cursor.fetchall()
    conn.close()
    return preguntas

def recupera_jugadores():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()
    cursor.execute('SELECT id_jugador, nombre, puntos FROM jugadores')
    jugadores = cursor.fetchall()
    conn.close()
    return jugadores

def sumar_punto_jugador(id_jugador):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()
    cursor.callproc('sumar_punto_jugador', (id_jugador,))
    conn.commit()
    conn.close()

def registrar_jugadores(nombre1, nombre2, nombre3):

    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='ignorancia'
    )

    cursor = conn.cursor()

    # borrar jugadores anteriores
    cursor.execute("DELETE FROM jugadores")

    # insertar nuevos jugadores
    cursor.execute(
        "INSERT INTO jugadores (id_jugador, nombre, puntos) VALUES (1,%s,0)",
        (nombre1,)
    )

    cursor.execute(
        "INSERT INTO jugadores (id_jugador, nombre, puntos) VALUES (2,%s,0)",
        (nombre2,)
    )

    cursor.execute(
        "INSERT INTO jugadores (id_jugador, nombre, puntos) VALUES (3,%s,0)",
        (nombre3,)
    )

    conn.commit()
    conn.close()