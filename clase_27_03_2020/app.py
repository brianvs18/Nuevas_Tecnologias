class Persona:

    #Constructor de la clase, siempre se llama el constructor primero
    #def__init__(self, name, lastname):
    #        self.nombre = name
    #self.apellido = lastname

    #Atributos
    name = []
    lastname = []

    #Metodos
    #def hablar(self, message):
    #print(message)
    def addPerson(self, name, lastname):
        self.name.append(name)
        self.lastname.append(lastname)
    def showPeople(self):
        for i in range(0, len(self.name)):
            print("name:" + str(self.name[i]) + " lastname: " + str(self.lastname[i]))

persona = Persona()
persona.addPerson("Brian", "Vanegas")
persona.addPerson("Pedro", "Torres")
persona.showPeople()