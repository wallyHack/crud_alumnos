class Alumno():
    """ clase que representa un alumno"""
    
    def __init__(self, matricula: int):
        """ constructor con 1 parametros"""
        self.matricula = matricula
    
    def __init__(self, matricula: int, nombres: str, apellido_paterno: str, apellido_materno: str, genero: str, ciudad: str, edad: int):
        """ constructor completo con todos los parametros"""
        self.matricula = matricula
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.genero = genero
        self.ciudad = ciudad
        self.edad = edad

    # getters y setters
    def get_matricula(self) -> int:
        return self.matricula

    def set_matricula(self, matricula: int):
        self.matricula = matricula

    def get_nombres(self) -> str:
        return self.nombres

    def set_nombres(self, nombres: str):
        self.nombres = nombres

    def get_apellido_paterno(self) -> str:
        return self.apellido_paterno

    def set_apellido_paterno(self, apellido_paterno: str):
        self.apellido_paterno = apellido_paterno

    def get_apellido_materno(self) -> str:
        return self.apellido_materno

    def set_apellido_materno(self, apellido_materno: str):
        self.apellido_materno = apellido_materno

    def get_genero(self) -> str:
        return self.genero

    def set_genero(self, genero: str):
        self.genero = genero

    def get_ciudad(self) -> str:
        return self.ciudad

    def set_ciudad(self, ciudad: str):
        self.ciudad = ciudad

    def get_edad(self) -> int:
        return self.edad

    def set_edad(self, edad: int):
        self.edad = edad

    def __str__(self):
        """ descripcion del alumno"""
        return "Alumno [matricula=" + str(self.matricula) + " " + self.nombres + " " + self.apellido_paterno + "]"

class Escuela():
    """ clase que representa una escuela"""
    
    def __init__(self):
        """ constructor sin parametros, inicializa la lista de alumnos vacia"""
        self.lista_alumnos = [] # lista vacia
    
    def listar_alumnos(self):
        """ listar todos los alumnos de la escuela"""
        # iterar lista
        for alumno in self.lista_alumnos:
            print(alumno)
    
    def buscar_alumno(self, matricula: int) -> str:
        """ buscar un alumno por su matricula"""
        # iterar lista
        for alumno in self.lista_alumnos:
            if alumno.get_matricula() == matricula: # comparar matricula
                return "Alumno encontrado: " + str(alumno)
            
        return "Alumno no encontrado"    

    def agregar_alumno(self, alumno: Alumno) -> None:
        """ agregar un alumno a la escuela"""
        self.lista_alumnos.append(alumno)

    def actualizar_alumno(self, alumno: Alumno) -> str:   
        """ actualizar un alumno de la escuela"""     
        # buscar el alumno
        for i in range(len(self.lista_alumnos)):
            # comparamos las matriculas
            if(self.lista_alumnos[i].get_matricula() == alumno.get_matricula()): 
                self.lista_alumnos[i] = alumno
                return "Alumno actualizado correctamente"
                        
        return "Alumno no encontrado"

    def eliminar_alumno(self, matricula: int) -> str:
        """ eliminar un alumno de la escuela"""
        # buscar el alumno
        for i in range(len(self.lista_alumnos)):
            # comparamos las matriculas
            if(self.lista_alumnos[i].get_matricula() == matricula): 
                self.lista_alumnos.pop(i)
                return "Alumno eliminado correctamente"
        
        return "Alumno no encontrado"

class TestEscuela():
    
    # creamos el objeto escuela 
    escuela = Escuela()
    
    # agregamos 5 alumnos de prueba a la escuela
    escuela.agregar_alumno(Alumno(12345, "Juan", "Perez", "Perez", "Masculino", "CDMX", 20))
    escuela.agregar_alumno(Alumno(24567, "Maria", "Gonzalez", "Gonzalez", "Femenino", "CDMX", 22))
    escuela.agregar_alumno(Alumno(36789, "Pedro", "Garcia", "Garcia", "Masculino", "CDMX", 21))
    escuela.agregar_alumno(Alumno(48901, "Ana", "Lopez", "Lopez", "Femenino", "CDMX", 31))
    escuela.agregar_alumno(Alumno(56789, "Luis", "Martinez", "Martinez", "Masculino", "CDMX", 25))

    for i in range(10):
        # MENU DE OPCIONES
        opciones = int(
            input("\nMENU: SISTEMA ESCOLAR \n1. Listar alumnos\n2. Buscar alumno\n3. Agregar alumno\n4. Actualizar alumno\n5. Eliminar alumno\n6. Salir\nSeleccione una opcion: ")  
        )
        
        match opciones:
            case 1: 
                print("LISTAR ALUMNOS")
                escuela.listar_alumnos()
            
            case 2:
                print("BUSCAR ALUMNO")
                matricula = int(input("Ingrese la matricula del alumno a buscar: "))
                print(escuela.buscar_alumno(matricula))
                
            case 3:
                print("AGREGAR ALUMNO")
                # cremaos objeto alumno con los datos ingresados por el usuario
                matricula = int(input("Ingrese la matricula del alumno: "))
                nombres = input("Ingrese los nombres del alumno: ")
                apellido_paterno = input("Ingrese el apellido paterno del alumno: ")
                apellido_materno = input("Ingrese el apellido materno del alumno: ")
                genero = input("Ingrese el genero del alumno: ")
                ciudad = input("Ingrese la ciudad del alumno: ")
                edad = int(input("Ingrese la edad del alumno: "))   

                # creamos el alumno
                nuevo_alumno = Alumno(matricula, nombres, apellido_paterno, apellido_materno, genero, ciudad, edad)
                # agregamos el alumno a la escuela
                escuela.agregar_alumno(nuevo_alumno)
                print("Alumno agregado correctamente")
                
            case 4:
                print("ACTUALIZAR ALUMNO")
                matricula = int(input("Ingrese la matricula del alumno a actualizar: "))
                
                nombres = input("Ingrese los nuevos nombres del alumno: ")
                apellido_paterno = input("Ingrese el nuevo apellido paterno del alumno: ")      
                apellido_materno = input("Ingrese el nuevo apellido materno del alumno: ")
                genero = input("Ingrese el nuevo genero del alumno: ")
                ciudad = input("Ingrese la nueva ciudad del alumno: ")
                edad = int(input("Ingrese la nueva edad del alumno: "))
                # creamos el alumno actualizado
                alumno_actualizado = Alumno(matricula, nombres, apellido_paterno, apellido_materno, genero, ciudad, edad)
                # actualizamos el alumno en la escuela
                print(escuela.actualizar_alumno(alumno_actualizado))
                
            case 5:
                print("ELIMINAR ALUMNO")
                matricula = int(input("Ingrese la matricula del alumno a eliminar: "))
                print(escuela.eliminar_alumno(matricula))
                
            case 6:
                print("SALIR")
                break
    
        
    """
    ### CRUD DE ALUMNOS SIN MENU - FORMA MANUAL
    
    # creamos 3 alumnos
    juan = Alumno(12345, "Juan", "Perez", "Perez", "Masculino", "CDMX", 20)
    maria = Alumno(24567, "Maria", "Gonzalez", "Gonzalez", "Femenino", "CDMX", 22)
    pedro = Alumno(36789, "Pedro", "Garcia", "Garcia", "Masculino", "CDMX", 21)

    # creamos una escuela
    escuela = Escuela()

    # agregamos los alumnos a la escuela
    escuela.agregar_alumno(juan)
    escuela.agregar_alumno(maria)
    escuela.agregar_alumno(pedro)

    # listar todos los alumnos
    print("LISTAR ALUMNOS")
    escuela.listar_alumnos()
    print("\n")

    # buscar alumno
    print("BUSCAR ALUMNO: 12345")
    print(escuela.buscar_alumno(12345))
    # print(escuela.buscar_alumno(9009)) NO ENCONTRADO
    print("\n")

    # agregar alumno
    print("AGREGAR ALUMNO: ANA")
    escuela.agregar_alumno(Alumno(48901, "Ana", "Lopez", "Lopez", "Femenino", "CDMX", 31))
    escuela.listar_alumnos()
    print("\n")

    # actualizar alumno
    print("ACTUALIZAR ALUMNO: JUAN")
    escuela.actualizar_alumno(Alumno(12345, "Juan", "Molina", "Perez", "Masculino", "CDMX", 42))
    escuela.listar_alumnos()
    print("\n")

    # eliminar alumno
    print("ELIMINAR ALUMNO: 12345")
    escuela.eliminar_alumno(12345)
    escuela.listar_alumnos()
    print("\n")
    """