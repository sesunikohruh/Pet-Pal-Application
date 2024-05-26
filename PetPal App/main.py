from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic
import mysql.connector

class communicate(QObject):
    updateVet = pyqtSignal(list)
    updateAppointments = pyqtSignal(list)

class databaseHandler():
    def fetchData(table):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # VETS functions
    def addVet(veterinarians): # Function where you are able to add a new vet

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute("TRUNCATE TABLE vets")
            addVetQuery = "INSERT INTO vets (vetLicense, firstName, lastName, contactNo, sexOr) VALUES (%s, %s, %s, %s, %s)"

            for veterinarian in veterinarians:
                vetLicense, firstName, lastName, contactNo, sex = veterinarian
                cursor.execute(addVetQuery, (vetLicense, firstName, lastName, contactNo, sex))
            connection.commit()

        except mysql.connector.Error as err:
            print(f"Error saving veterinarians: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def deleteVet(petpal_clinic,vets):

        try: # Connect to Database

            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )

            cursor = connection.cursor()

            deleteVetQuery = """DELETE FROM vets"""

            cursor.execute(deleteVetQuery)

            connection.commit()

        except mysql.connector.Error as error:
            print(f"Failed to delete row from MySQL table: {error}")
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def updateVet(vetLicense, firstName, lastName, contactNo, sex):
        try:
            # Connect to Database
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()

            # SQL query to update a veterinarian record
            updateVetQuery = """
            UPDATE vets SET 
                firstName = %s,
                lastName = %s,
                contactNo = %s,
                sexOr = %s
            WHERE vetLicense = %s
            """
            
            # Execute the query
            cursor.execute(updateVetQuery, (firstName, lastName, contactNo, sex, vetLicense))

            # Commit the transaction
            connection.commit()

            print("Veterinarian updated successfully.")

        except mysql.connector.Error as err:
            print(f"Error updating veterinarian: {err}")

        finally:
            # Close the cursor and connection
            if connection.is_connected():
                cursor.close()
                connection.close()

    
    # --------------------------------------------------------------------------------------------------------------------------------

    # CLIENTS function
    def addClient(clients): # Function where you are able to add a new client

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute("TRUNCATE TABLE clients")
            addClientQuery = """
            INSERT INTO clients (
                clientID, 
                firstName, 
                lastName, 
                contactNo, 
                address, 
                sexOr
            ) VALUES (%s, %s, %s, %s, %s, %s)"""

            for client in clients:
                clientID, firstName, lastName, contactNo, address, sexOr = client
                cursor.execute(addClientQuery, (clientID, firstName, lastName, contactNo, address, sexOr))
            connection.commit()

        except mysql.connector.Error as err:
            print(f"Error saving client: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def deleteClient(petpal_clinic,clients):

        try: # Connect to Database

            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )

            cursor = connection.cursor()

            deleteClientQuery = """DELETE FROM clients"""

            cursor.execute(deleteClientQuery)

            connection.commit()

        except mysql.connector.Error as error:
            print(f"Failed to delete row from MySQL table: {error}")
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def updateClient(clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet, petID):

        try:
            # Connect to Database
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()

            # SQL query to update a pet record
            updateClientQuery = """
            UPDATE pets SET 
                clientID = %s,
                ownerName = %s,
                name = %s,
                species = %s,
                breed = %s,
                birthDate = %s,
                sexOr = %s,
                status = %s,
                mainVet = %s
            WHERE petID = %s
            """

            # Execute the query
            cursor.execute(updateClientQuery, (clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet, petID))

            # Commit the transaction
            connection.commit()

            print("Pet updated successfully.")

        except mysql.connector.Error as err:
            print(f"Error updating pet: {err}")

        finally:
            # Close the cursor and connection
            if connection.is_connected():
                cursor.close()
                connection.close()
    # --------------------------------------------------------------------------------------------------------------------------------
                
    # PETS function
    def addPets(pets):

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute("TRUNCATE TABLE pets")
            addPetQuery = """
            INSERT INTO pets (
                petID, 
                clientID, 
                ownerName, 
                name, 
                species, 
                breed, 
                birthDate, 
                sexOr, 
                status, 
                mainVet
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            for pet in pets:
                petID, clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet = pet
                cursor.execute(addPetQuery, (petID, clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet))
            connection.commit()

        except mysql.connector.Error as err:
            print(f"Error saving new pet: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def deletePet(petpal_clinic,pets):

        try: # Connect to Database

            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )

            cursor = connection.cursor()

            deletePetQuery = """DELETE FROM pets"""

            cursor.execute(deletePetQuery)

            connection.commit()

        except mysql.connector.Error as error:
            print(f"Failed to delete row from MySQL table: {error}")
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def updatePet(petID, clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet):
        try:
            # Connect to Database
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()

            # SQL query to update a pet record
            updatePetQuery = """
            UPDATE pets SET 
                clientID = %s,
                ownerName = %s,
                name = %s,
                species = %s,
                breed = %s,
                birthDate = %s,
                sexOr = %s,
                status = %s,
                mainVet = %s
            WHERE petID = %s
            """

            # Execute the query
            cursor.execute(updatePetQuery, (clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet, petID))

            # Commit the transaction
            connection.commit()

            print("Pet updated successfully.")

        except mysql.connector.Error as err:
            print(f"Error updating pet: {err}")

        finally:
            # Close the cursor and connection
            if connection.is_connected():
                cursor.close()
                connection.close()
    # --------------------------------------------------------------------------------------------------------------------------------

    def saveAppointmentsToDatabase(appointments):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute("TRUNCATE TABLE appointments")
            insert_query_template = """
            INSERT INTO appointments (
                appointmentCode, 
                date, 
                schedule, 
                service, 
                clientID, 
                clientName,
                attendingVet,
                status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            for appointment in appointments:
                appointmentCode, date, schedule, service, clientID, clientName, attendingVet, status = appointment
                cursor.execute(insert_query_template,(appointmentCode, date, schedule, service, clientID, clientName, attendingVet, status))
            connection.commit()

        except mysql.connector.Error as err:
            print(f"Error saving appointments: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        uic.loadUi("mainWindow.ui", self)
        self.show()

        self.appointments = databaseHandler.fetchData("appointments")
        self.veterinarians = databaseHandler.fetchData("vets")
        self.clients = databaseHandler.fetchData("clients")
        self.communicate = communicate()

        self.homeButton.clicked.connect(self.homeClicked)
        self.clientButton.clicked.connect(self.clientClicked)
        self.petButton.clicked.connect(self.petClicked)
        self.vetButton.clicked.connect(self.vetClicked)
        button = self.stackedWidget.findChild(QPushButton, 'addButton')
        if button:
            # Connect the button's clicked signal to the addClicked slot
            button.clicked.connect(self.addClicked)

    def homeClicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def clientClicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def petClicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def vetClicked(self):
        self.stackedWidget.setCurrentIndex(3)

    def addClicked(self):
        vet_license = self.licenseInput.text()
        first_name = self.firstNameInput.text()
        last_name = self.lastNameInput.text()
        contact_number = self.contactInput.text()
        sex = self.sexInput.currentText()

        new_tuple = (vet_license, first_name, last_name, contact_number, sex)
        self.veterinarians.append(new_tuple)

        print(self.veterinarians)
        databaseHandler.saveVetToDatabase(self.veterinarians)

def main():
    app = QApplication([])
    window = mainWindow()
    app.exec_()

if __name__ == "__main__":
    main()
