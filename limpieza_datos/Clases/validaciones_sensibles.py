import re

class VerificadorSensibilidad:
    def __init__(self):
        self.tarjeta_credito_re = re.compile(r"\b(?:\d[ -]*?){13,19}\b")  # Expresión regular para tarjetas de crédito
        self.email_re = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")  # Expresión regular para emails
        self.dni_honduras_re = re.compile(r"\b\d{4}-\d{4}-\d{5}\b")  # Expresión regular para DNI hondureño
        self.rtn_honduras_re = re.compile(r"\b\d{4}-\d{4}-\d{6}\b")  # Expresión regular para RTN hondureño
        self.telefono_honduras_re = re.compile(r"\b(?:\d[ -]*?){8,9}\b")  # Expresión regular para teléfonos hondureños
        self.direccion_hondurena_re = re.compile(r"\b(?:calle|col|colonia|avenida|av|callejon|casa|frente a|contiguo a|cuadra|barrio|residencial|esquina opuesta|esquina|carretera|aldea|pueblo)\b(?:\s[#]?\d{1,4}\b)?(?:[a-zA-Z0-9\s.,'-]*)\b")


    def es_sensible(self, campo):
        if self.tarjeta_credito_re.search(campo) or \
           self.email_re.search(campo) or \
           self.dni_honduras_re.search(campo) or \
           self.rtn_honduras_re.search(campo) or \
           self.telefono_honduras_re.search(campo) or \
           self.direccion_hondurena_re.search(str.lower(campo)):
            return "*********"
        return campo