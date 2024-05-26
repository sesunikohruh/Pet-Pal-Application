from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QHeaderView, QComboBox
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
                password='password',
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
    def addVet(veterinarians):

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
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

    def deleteVet(petpal_clinic, vets):

        try:  # Connect to Database

            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
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
                password='password',
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

            print("Pet Pal updated successfully.")

        except mysql.connector.Error as err:
            print(f"Error updating veterinarian: {err}")

        finally:
            # Close the cursor and connection
            if connection.is_connected():
                cursor.close()
                connection.close()

    # --------------------------------------------------------------------------------------------------------------------------------

    # CLIENTS function
    def addClients(clients):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute(
                "TRUNCATE TABLE clients")
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

    def deleteClient(petpal_clinic, clients):

        try:  # Connect to Database

            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
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
                password='password',
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
            cursor.execute(updateClientQuery,
                           (clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet, petID))

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
        print(pets)
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
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
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for pet in pets:
                petID, clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet = pet
                cursor.execute(addPetQuery,
                               (petID, clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet))
            connection.commit()

        except mysql.connector.Error as err:
            print(f"Error saving pets: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def deletePet(petpal_clinic, pets):

        try:  # Connect to Database

            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
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
                password='password',
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
            cursor.execute(updatePetQuery,
                           (clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet, petID))

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
                password='password',
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
                cursor.execute(insert_query_template,
                               (appointmentCode, date, schedule, service, clientID, clientName, attendingVet, status))
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
        self.pets = databaseHandler.fetchData("pets")
        self.communicate = communicate()

        for client in self.clients:
            client_ID = client[0]
            self.ownerID.addItem(str(client_ID))

        for veterinarian in self.veterinarians:
            vet_license = veterinarian[0]
            self.mainVet.addItem(str(vet_license))

        self.homeButton.clicked.connect(self.homeClicked)
        self.clientButton.clicked.connect(self.clientClicked)
        self.petButton.clicked.connect(self.petClicked)
        self.vetButton.clicked.connect(self.vetClicked)

        addVetButton = self.stackedWidget.findChild(QPushButton, 'addButton')
        addVetButton.clicked.connect(self.addClicked)
        addClientButton = self.stackedWidget.findChild(QPushButton, 'addClientButton')
        addClientButton.clicked.connect(self.addClientClicked)
        addPetButton =self.stackedWidget.findChild(QPushButton, 'addPetButton')
        addPetButton.clicked.connect(self.addPetClicked)

        self.read()
        self.readClients()
        self.readPets()

    def read(self):
        self.vetTable.setRowCount(0)
        self.vetTable.setColumnCount(5)

        for veterinarian in self.veterinarians:
            row_position = self.vetTable.rowCount()
            self.vetTable.insertRow(row_position)

            vet_license, first_name, last_name, contact_no, sex = veterinarian
            items = [QTableWidgetItem(str(item)) for item in [vet_license, first_name, last_name, contact_no, sex]]
            for i, item in enumerate(items):
                self.vetTable.setItem(row_position, i, item)

        self.vetTable.resizeColumnsToContents()
        self.vetTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def readClients(self):
        self.clients = databaseHandler.fetchData("clients")
        self.clientTable.setRowCount(0)
        self.clientTable.setColumnCount(6)

        for client in self.clients:
            row_position = self.clientTable.rowCount()
            self.clientTable.insertRow(row_position)

            client_ID, first_name, last_name, contact_number, address, sex = client
            items = [QTableWidgetItem(str(item)) for item in [client_ID, first_name, last_name, contact_number, address, sex]]
            for i, item in enumerate(items):
                self.clientTable.setItem(row_position, i, item)

        self.clientTable.resizeColumnsToContents()
        self.clientTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def readPets(self):
        self.pets = databaseHandler.fetchData("pets")
        self.petTable.setRowCount(0)
        self.petTable.setColumnCount(10)

        for pet in self.pets:
            row_position = self.petTable.rowCount()
            self.petTable.insertRow(row_position)

            pet_id, client_id, owner_name, pet_name, species, breed, birth_date, sex, status, main_vet = pet
            items = [QTableWidgetItem(str(item)) for item in
                     [pet_id, client_id, owner_name, pet_name, species, breed, birth_date, sex, status, main_vet]]
            for i, item in enumerate(items):
                self.petTable.setItem(row_position, i, item)

        self.petTable.horizontalHeader()

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
        databaseHandler.addVet(self.veterinarians)
        self.read()

    def addClientClicked(self):
        client_ID = None
        last_name = self.clientLastName.text()
        first_name = self.clientFirstName.text()
        contact_number = self.clientContactNo.text()
        address = self.clientAddress.text()
        sex = self.clientSex.currentText()

        new_client = (client_ID, first_name, last_name, contact_number, address, sex)
        self.clients.append(new_client)
        databaseHandler.addClients(self.clients)
        self.readClients()

    def addPetClicked(self):
        pet_id = None
        owner_id = self.ownerID.currentText()
        owner_name = None
        pet_name = self.petName.text()
        species = self.species.currentText()
        breed = self.breed.text()
        birth_date = self.birthDate.text()
        sex = self.sex.currentText()
        status = self.status.currentText()
        main_vet = self.mainVet.currentText()

        new_pet = (pet_id, owner_id, owner_name, pet_name, species, breed, birth_date, sex, status, main_vet)
        self.pets.append(new_pet)
        databaseHandler.addPets(self.pets)
        self.readPets()

def main():
    app = QApplication([])
    window = mainWindow()
    app.exec_()


if __name__ == "__main__":
    main()

