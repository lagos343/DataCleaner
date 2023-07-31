import mysql.connector


class MySQLConnector:
    def __init__(self):
        self.host = "localhost"
        self.user = "admin"
        self.password = "Ad_min_Security_class_2923"
        self.database = "datacleaner"
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connected to MySQL database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from MySQL database")

    def obtener_registros_por_tabla(self, tabla):
        self.connect()

        cursor = self.connection.cursor()
        cursor.callproc('obtener_registros', [tabla])

        # Obtener los resultados del procedimiento almacenado
        registros = []
        for result in cursor.stored_results():
            registros.extend(result.fetchall())

        cursor.callproc('obtener_columnas', [tabla])

        result = cursor.stored_results()
        column_names_result = next(result).fetchone()[0]
        column_names_list = column_names_result.split(',')

        self.disconnect
        return column_names_list, registros

    def validate_login(self, user, password):
        self.connect()  # Abrimos la conexión

        cursor = self.connection.cursor()
        resultado = cursor.callproc('ValidarLogin', (user, password, 0))  # Cambio a None
        self.connection.commit()
        resultado_validacion = resultado[2]

        self.disconnect()  # Cerramos la conexión
        return resultado_validacion


    def insercion_registromedico(self,nombre,edad,sexo,diagnostico):
        self.connect()

        cursor = self.connection.cursor()
        resultado = cursor.callproc('medico', (nombre, edad, sexo, diagnostico))
        self.connection.commit()

        self.disconnect()

    def insercion_datosprivados(self,nombre, apellido, dni, direccion, telefono, email):
        self.connect()

        cursor = self.connection.cursor()
        resultado = cursor.callproc('datosprivados', (nombre, apellido, dni, direccion, telefono, email))
        self.connection.commit()

        self.disconnect()

    def insercion_datosgenerales(self,nombre, apellido, direccion, edad, telefono, email):
        self.connect()

        cursor = self.connection.cursor()
        resultado = cursor.callproc('datos_generales', (nombre, apellido, direccion, edad, telefono, email))
        self.connection.commit()

        self.disconnect()

    def insercion_datoscompras(self,nombre, apellido, direccion, ciudad, telefono, email, tajetacredito):
        self.connect()

        cursor = self.connection.cursor()
        resultado = cursor.callproc('compras', (nombre, apellido, direccion, ciudad, telefono, email, tajetacredito))
        self.connection.commit()

        self.disconnect()





