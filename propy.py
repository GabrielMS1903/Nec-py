#fazer um programa com tudo o que foi estudado até agora com o propósito de listar a entrada e saída de corpos em um necrotério policial com a causa da morte, nome da vítima, idade, sexo e afins

import mysql.connector
from mysql.connector import Error

class DataBase:
    def __init__(self, host, database, user, password) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connect_db()

    def connect_db(self):
        try:
            self.connection = mysql.connector.connect(
                host = 'localhost',
                database = 'datainfo',
                user = 'root',
                password = ''
            )
            if self.connection.is_connected():
                print("Conectado ao MYSQL")
        except Error as e:
            print(f"Erro ao conectar {e}")

    def save_to_db(self, name, age, gender, cause, localDeath):
        try:
            cursor = self.connection.cursor()
            query = """
            INSERT INTO registros (name, age, gender, cause, localDeath)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = ( name, age, gender, cause, localDeath)
            cursor.execute(query, values)
            self.connection.commit()
            print("Dados salvos com sucesso!")
        except Error as e:
            print(f"Erro ao salvar os dados, {e}")


    def fetch_from_db(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM registros")
            records = cursor.fetchall()
            for row in records:
                print(row)
        except Error as e:
            print(f"Erro ao busar dados, {e}")



#classe pai
class Entrance(DataBase):
    def __init__(self, host, database, user, password):
        super().__init__(host, database, user, password)
        self.BR = [
           "Acre",
            "Alagoas",
            "Amapá",
            "Amazonas",
            "Bahia",
            "Ceará",
            "Distrito Federal",
            "Espírito Santo",
            "Goiás",
            "Maranhão",
            "Mato Grosso",
            "Mato Grosso do Sul",
            "Minas Gerais",
            "Pará",
            "Paraíba",
            "Paraná",
            "Pernambuco",
            "Piauí",
            "Rio de Janeiro",
            "Rio Grande do Norte",
            "Rio Grande do Sul",
            "Rondônia",
            "Roraima",
            "Santa Catarina",
            "São Paulo",
            "Sergipe",
            "Tocantins" 
        ]
        
    
    

     #função para registrar       
    def Register(self):
        while True:
            name = input("Type the name of deceased.")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("Please, just letters.")
        
        while True:
            age = input("Age")
            try:
                age = int(age)
                if age >= 199:
                    print("Incorrect age")
                else:
                    print("accepted age")
                    break
            except ValueError:
                print("Please, type an age between 1-100")

        while True:
            gender = input("Gender") 
            if gender == "feminine" or gender == "masculine":
                break
            else:
                print("Please, masculine or feminine")
        

        cause = input("Cause of the death")   

        while True:
            localDeath = input("Exactly the place of death.")
        
         
            if localDeath in self.BR:
                print("The place is an state of The Brazil. Accepted")
                break
            else:
                print("Please, type an Brazil state.")

        self.save_to_db(name, age, gender, cause, localDeath)
        

    
    def informacao(self):
        RED = "\033[31m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        WHITE = "\033[37m"

        opcao = True
        while opcao:
            opcao = int(input(f"{YELLOW}[1] Register  \n[2] Cause of death  \n[3] Local \n[4] Describe  \n[5] Exit"))

            if opcao == 1:
                self.Register()
                
            elif opcao == 2:
                print(f"Cause of death: {self.cause if hasattr(self, 'cause') else "No register"}")
            elif opcao == 3:
               print(f"Local da morte: {self.localDeath if hasattr(self, 'localDeath') else "No register"}")
            elif opcao == 4:
                descricao = (
                    f" {WHITE}Name: {GREEN} {self.name if hasattr(self, 'name') else f'{RED} No register'}, \n "
                    f"{WHITE}Age: {GREEN} {self.age if hasattr(self, 'age') else f'{RED} No register'}, \n"
                    f"{WHITE}Gender: {GREEN} {self.gender if hasattr(self, 'gender') else f'{RED} No register'}, \n "
                    f"{WHITE}Cause of death: {GREEN} {self.cause if hasattr(self, 'cause') else f'{RED} No register'} \n"
                    f"{WHITE}Place of death: {GREEN} {self.localDeath if hasattr(self, 'localDeath') else f'{RED} No register'} \n" )
                print(descricao)
            elif opcao == 5:
                break
            else:
                print("No option")

    

entrada = Entrance(host = 'localhost', database='datainfo', user='root', password='')
entrada.informacao()