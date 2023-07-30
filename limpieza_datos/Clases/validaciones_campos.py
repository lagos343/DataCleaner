import re
class validacionesCampos:
    #de haber errores estaran aca
    mensaje_error = "Lista de Errores:"
    def validar_registro_medico(self, nombre, edad, sexo, diagnostico):
        esta_correcto = True

        #------------------------------------------------------------------------------------------
        #validaciones para nombre
        if not self.solo_letras_y_espacios(nombre):
            esta_correcto = False
            self.mensaje_error += "\n-Nombre: solo letras o espacios son permitidos"

        if not self.no_vacio(nombre):
            esta_correcto = False
            self.mensaje_error += "\n-Nombre: no puede estar vacio"

        # ------------------------------------------------------------------------------------------
        # validaciones para edad
        if not self.no_vacio(edad):
            esta_correcto = False
            self.mensaje_error += "\n-Edad: no puede estar vacio"

        if not self.solo_digitos(edad):
            esta_correcto = False
            self.mensaje_error += "\n-Edad: solo numeros son permitidos"

        # ------------------------------------------------------------------------------------------
        # validaciones para sexo
        if not self.solo_letras_sin_espacios(sexo):
            esta_correcto = False
            self.mensaje_error += "\n-Sexo: solo letras sin espacios son permitidos"

        if not self.no_vacio(sexo):
            esta_correcto = False
            self.mensaje_error += "\n-Sexo: no puede estar vacio"

        # ------------------------------------------------------------------------------------------
        # validaciones para diagnostico
        if not self.no_vacio(diagnostico):
            esta_correcto = False
            self.mensaje_error += "\n-Diagnostico: no puede estar vacio"

        if not self.solo_letras_y_espacios(diagnostico):
            esta_correcto = False
            self.mensaje_error += "\n-Diagnostico: solo letras o espacios son permitidos"


        return esta_correcto

    # VALIDACIONES DATOS PRIVADOS
    def validar_registro_datos_privados(self, nombre, apellido, dni, direccion,telefono,email):
        esta_correcto = True

        #------------------------------------------------------------------------------------------
        #validaciones para nombre
        if not self.solo_letras_y_espacios(nombre):
            esta_correcto = False
            self.mensaje_error += "\n-Nombre: solo letras o espacios son permitidos"

        if not self.no_vacio(nombre):
            esta_correcto = False
            self.mensaje_error += "\n-Nombre: no puede estar vacio"

        # ------------------------------------------------------------------------------------------

        # validaciones para apellido
        if not self.solo_letras_y_espacios(apellido):
            esta_correcto = False
            self.mensaje_error += "\n-Apellido: solo letras o espacios son permitidos"

        if not self.no_vacio(nombre):
            esta_correcto = False
            self.mensaje_error += "\n-Apellido: no puede estar vacio"

        # ------------------------------------------------------------------------------------------
        # validaciones para DNI
        if not self.no_vacio(dni):
            esta_correcto = False
            self.mensaje_error += "\n-DNI: no puede estar vacio"

        if not self.solo_digitos(dni):
            esta_correcto = False
            self.mensaje_error += "\n-DNI: solo numeros son permitidos"

        # ------------------------------------------------------------------------------------------
        # validaciones para direccion
        if not self.solo_letras_y_espacios(direccion):
            esta_correcto = False
            self.mensaje_error += "\n-Direccion: solo letras o espacios son permitidos"

        if not self.no_vacio(direccion):
            esta_correcto = False
            self.mensaje_error += "\n-Direccion: no puede estar vacio"

        # ------------------------------------------------------------------------------------------
        # validaciones para telefono
        if not self.no_vacio(telefono):
            esta_correcto = False
            self.mensaje_error += "\n-Telefono: no puede estar vacio"

        if not self.solo_digitos(telefono):
            esta_correcto = False
            self.mensaje_error += "\n-Telefono: solo numeros son permitidos"

        # ------------------------------------------------------------------------------------------
        #validaciones para email
        if not self.es_email_valido(email):
            esta_correcto = False
            self.mensaje_error += "\n-Email: no es valido"

        if not self.no_vacio(nombre):
            esta_correcto = False
            self.mensaje_error += "\n-Email: no puede estar vacio"


        return esta_correcto

    #FIN VALIDACION DATOS PRIVADOS

    #-------------------------------------------------------------------------------
    # VALIDACIONES DATOS COMPRA
    def validar_registro_datos_compra(self, nombre, apellido, direccion, ciudad, telefono, email, tarjetacredito):
        esta_correcto = True

        #------------------------------------------------------------------------------------------
        #validaciones para nombre
        if not self.solo_letras_y_espacios(nombre):
            esta_correcto = False
            self.mensaje_error += "\n-Nombre: solo letras o espacios son permitidos"

        if not self.no_vacio(nombre):
            esta_correcto = False
            self.mensaje_error += "\n-Nombre: no puede estar vacio"

        # ------------------------------------------------------------------------------------------

        # validaciones para apellido
        if not self.solo_letras_y_espacios(apellido):
            esta_correcto = False
            self.mensaje_error += "\n-Apellido: solo letras o espacios son permitidos"

        if not self.no_vacio(apellido):
            esta_correcto = False
            self.mensaje_error += "\n-Apellido: no puede estar vacio"

        # ------------------------------------------------------------------------------------------

        # validaciones para direccion
        if not self.solo_letras_y_espacios(direccion):
            esta_correcto = False
            self.mensaje_error += "\n-Direccion: solo letras o espacios son permitidos"

        if not self.no_vacio(direccion):
            esta_correcto = False
            self.mensaje_error += "\n-Direccion: no puede estar vacio"

        # ------------------------------------------------------------------------------------------
        # validaciones para ciudad
        if not self.solo_letras_y_espacios(ciudad):
            esta_correcto = False
            self.mensaje_error += "\n-Ciudad: solo letras o espacios son permitidos"

        if not self.no_vacio(ciudad):
            esta_correcto = False
            self.mensaje_error += "\n-Ciudad: no puede estar vacio"

        # ------------------------------------------------------------------------------------------
        # validaciones para telefono
        if not self.no_vacio(telefono):
            esta_correcto = False
            self.mensaje_error += "\n-Telefono: no puede estar vacio"

        if not self.solo_digitos(telefono):
            esta_correcto = False
            self.mensaje_error += "\n-Telefono: solo numeros son permitidos"

        # ------------------------------------------------------------------------------------------
        #validaciones para email
        if not self.es_email_valido(email):
            esta_correcto = False
            self.mensaje_error += "\n-Email: no es valido"

        if not self.no_vacio(nombre):
            esta_correcto = False
            self.mensaje_error += "\n-Email: no puede estar vacio"

        # ------------------------------------------------------------------------------------------
        # validaciones para Tarjeta Credito
        if not self.no_vacio(tarjetacredito):
            esta_correcto = False
            self.mensaje_error += "\n-Tarjeta de Credito: no puede estar vacio"

        if not self.solo_digitos(tarjetacredito):
            esta_correcto = False
            self.mensaje_error += "\n-Tarjeta de Credito: solo numeros son permitidos"

        # ------------------------------------------------------------------------------------------

        return esta_correcto

    #FIN VALIDACION DATOS COMPRA

    def solo_digitos(self, campo):
        return campo.isdigit()

    def solo_letras_y_espacios(self, campo):
        return campo.replace(" ", "").isalpha()

    def solo_letras_sin_espacios(self, campo):
        return campo.isalpha()

    def no_vacio(self, campo):
        return bool(campo.strip())

    def es_email_valido(self, email):
        # Expresión regular para validar el formato de un email
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron_email, email) is not None

