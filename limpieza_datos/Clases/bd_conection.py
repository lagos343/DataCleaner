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

    def validate_login(self, user, password):
        self.connect()  # Abrimos la conexión

        cursor = self.connection.cursor()
        resultado = cursor.callproc('ValidarLogin', (user, password, 0))  # Cambio a None
        self.connection.commit()
        resultado_validacion = resultado[2]

        self.disconnect()  # Cerramos la conexión
        return resultado_validacion


