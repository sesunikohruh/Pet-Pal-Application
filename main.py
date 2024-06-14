from PyQt5.QtCore import Qt,QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QHeaderView, QComboBox, QMessageBox
from PyQt5 import uic
import mysql.connector

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
            cursor.execute("DELETE FROM vets")
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

    def deleteVet(vetLicense):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            deleteVetQuery = "DELETE FROM vets WHERE vetLicense = %s"
            cursor.execute(deleteVetQuery, (vetLicense,))
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
            cursor.execute("DELETE FROM clients")
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
                clientID, firstName, lastName, contactNo, address, sex = client
                cursor.execute(addClientQuery, (clientID, firstName, lastName, contactNo, address, sex))
            connection.commit()

        except mysql.connector.Error as err:
            print(f"Error saving client: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def deleteClient(clientID):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            deleteVetQuery = "DELETE FROM clients WHERE clientID = %s"
            cursor.execute(deleteVetQuery, (clientID,))
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
            cursor.execute(updateClientQuery,(clientID, ownerName, name, species, breed, birthDate, sex, status, mainVet, petID))

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
                password='password',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM pets")
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
                status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for pet in pets:
                petID, clientID, ownerName, name, species, breed, birthDate, sexOr, status = pet
                cursor.execute(addPetQuery,(petID, clientID, ownerName, name, species, breed, birthDate, sexOr, status))
            connection.commit()

        except mysql.connector.Error as err:
            print(f"Error saving pets: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def deletePet(petID):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            deleteVetQuery = "DELETE FROM pets WHERE petID = %s"
            cursor.execute(deleteVetQuery, (petID,))
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

    # APPOINTMENTS function
    def addAppointments(appointments):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM appointments")
            addPetQuery = """
            INSERT INTO appointments (
                appointmentCode,
                date,
                schedule,
                service,
                status,
                vetLicense,
                clientID,
                petID,
                vetName,
                clientName,
                petName
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for appointment in appointments:
                appointmentCode, date, schedule, service, status, vetLicense, clientID, petID, vetName, clientName, petName = appointment
                cursor.execute(addPetQuery,
                               (appointmentCode, date, schedule, service, status, vetLicense, clientID, petID, vetName, clientName, petName))
            connection.commit()

        except mysql.connector.Error as err:
            print(f"Error saving appointments: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def deleteAppointment(appointmentCode):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            deleteVetQuery = "DELETE FROM appointments WHERE appointmentCode = %s"
            cursor.execute(deleteVetQuery, (appointmentCode,))
            connection.commit()
        except mysql.connector.Error as error:
            print(f"Failed to delete row from MySQL table: {error}")
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

        for client in self.clients:
            clientID = client[0]
            self.ownerID.addItem(str(clientID))

        for client in self.clients:
            clientID = client[0]
            self.clientID.addItem(str(clientID))

        for veterinarian in self.veterinarians:
            vetLicense = veterinarian[0]
            self.vetLicense.addItem(str(vetLicense))

        for pet in self.pets:
            petID = pet[0]
            self.petID.addItem(str(petID))

        self.homeButton.clicked.connect(self.homeClicked)
        self.clientButton.clicked.connect(self.clientClicked)
        self.petButton.clicked.connect(self.petClicked)
        self.vetButton.clicked.connect(self.vetClicked)

        addVetButton = self.stackedWidget.findChild(QPushButton, 'addButton')
        addVetButton.clicked.connect(self.addVetClicked)
        addClientButton = self.stackedWidget.findChild(QPushButton, 'addClientButton')
        addClientButton.clicked.connect(self.addClientClicked)
        addPetButton =self.stackedWidget.findChild(QPushButton, 'addPetButton')
        addPetButton.clicked.connect(self.addPetClicked)
        addAppointmentButton = self.stackedWidget.findChild(QPushButton, 'addAppointmentButton')
        addAppointmentButton.clicked.connect(self.addAppointmentClicked)

        deleteVetButton = self.stackedWidget.findChild(QPushButton, 'deleteVetButton')
        deleteVetButton.clicked.connect(self.deleteVetClicked)
        deleteClientButton = self.stackedWidget.findChild(QPushButton, 'deleteClientButton')
        deleteClientButton.clicked.connect(self.deleteClientClicked)
        deletePetButton = self.stackedWidget.findChild(QPushButton, 'deletePetButton')
        deletePetButton.clicked.connect(self.deletePetClicked)
        deleteAppointment = self.stackedWidget.findChild(QPushButton, 'deleteAppointment')
        deleteAppointment.clicked.connect(self.deleteAppointmentClicked)

        self.vetTable.itemChanged.connect(self.itemChanged)

        """
        editVetButton = self.stackedWidget.findChild(QPushButton, 'editVetButton')
        editVetButton.clicked.connect(self.editVetClicked)
        editClientButton = self.stackedWidget.findChild(QPushButton, 'editClientButton')
        editClientButton.clicked.connect(self.editClientClicked)
        editPetButton = self.stackedWidget.findChild(QPushButton, 'editPetButton')
        editPetButton.clicked.connect(self.editPetClicked)
        editAppointment = self.stackedWidget.findChild(QPushButton, 'editAppointment')
        editAppointment.clicked.connect(self.editAppointmentClicked)
        """

        self.readVet()
        self.readClients()
        self.readPets()
        self.readAppointments()

    # DISPLAY DATABASE ---------------------------------------------------------------------------------------------

    def readVet(self):
        self.ownerID.clear()
        self.vetLicense.clear()
        self.clientID.clear()
        self.petID.clear()
        for client in self.clients:
            clientID = client[0]
            self.ownerID.addItem(str(clientID))

        for client in self.clients:
            clientID = client[0]
            self.clientID.addItem(str(clientID))

        for veterinarian in self.veterinarians:
            vetLicense = veterinarian[0]
            self.vetLicense.addItem(str(vetLicense))

        for pet in self.pets:
            petID = pet[0]
            self.petID.addItem(str(petID))

        self.veterinarians = databaseHandler.fetchData("vets")
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
        self.ownerID.clear()
        self.vetLicense.clear()
        self.clientID.clear()
        self.petID.clear()
        for client in self.clients:
            clientID = client[0]
            self.ownerID.addItem(str(clientID))

        for client in self.clients:
            clientID = client[0]
            self.clientID.addItem(str(clientID))

        for veterinarian in self.veterinarians:
            vetLicense = veterinarian[0]
            self.vetLicense.addItem(str(vetLicense))

        for pet in self.pets:
            petID = pet[0]
            self.petID.addItem(str(petID))

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
        self.ownerID.clear()
        self.vetLicense.clear()
        self.clientID.clear()
        self.petID.clear()
        for client in self.clients:
            clientID = client[0]
            self.ownerID.addItem(str(clientID))

        for client in self.clients:
            clientID = client[0]
            self.clientID.addItem(str(clientID))

        for veterinarian in self.veterinarians:
            vetLicense = veterinarian[0]
            self.vetLicense.addItem(str(vetLicense))

        for pet in self.pets:
            petID = pet[0]
            self.petID.addItem(str(petID))

        self.pets = databaseHandler.fetchData("pets")
        self.petTable.setRowCount(0)
        self.petTable.setColumnCount(9)

        for pet in self.pets:
            row_position = self.petTable.rowCount()
            self.petTable.insertRow(row_position)

            pet_id, client_id, owner_name, pet_name, species, breed, birth_date, sex, status = pet
            items = [QTableWidgetItem(str(item)) for item in
                     [pet_id, client_id, owner_name, pet_name, species, breed, birth_date, sex, status]]
            for i, item in enumerate(items):
                self.petTable.setItem(row_position, i, item)

        self.petTable.horizontalHeader()
    
    def readAppointments(self):
        self.ownerID.clear()
        self.vetLicense.clear()
        self.clientID.clear()
        self.petID.clear()
        for client in self.clients:
            clientID = client[0]
            self.ownerID.addItem(str(clientID))

        for client in self.clients:
            clientID = client[0]
            self.clientID.addItem(str(clientID))

        for veterinarian in self.veterinarians:
            vetLicense = veterinarian[0]
            self.vetLicense.addItem(str(vetLicense))

        for pet in self.pets:
            petID = pet[0]
            self.petID.addItem(str(petID))

        self.appointments = databaseHandler.fetchData("appointments")
        self.apptTable.setRowCount(0)
        self.apptTable.setColumnCount(11)

        for appointment in self.appointments:
            row_position = self.apptTable.rowCount()
            self.apptTable.insertRow(row_position)

            appointmentCode, date, schedule, service, status, vetLicense, clientID, petID, vetName, clientName, petName = appointment
            items = [QTableWidgetItem(str(item)) for item in
                     [appointmentCode, date, schedule, service, status, vetLicense, clientID, petID, vetName, clientName, petName]]
            for i, item in enumerate(items):
                self.apptTable.setItem(row_position, i, item)

        self.apptTable.horizontalHeader()

    # BUTTON FUNCTIONS / ACTIONS ---------------------------------------------------------------------------------------------

    def homeClicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def clientClicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def petClicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def vetClicked(self):
        self.stackedWidget.setCurrentIndex(3)

    def addVetClicked(self): # Add New Vet Button

        vetLicense = self.licenseInput.text()
        firstName = self.firstNameInput.text()
        lastName = self.lastNameInput.text()
        contactNo = self.contactInput.text()
        sex = self.sexInput.currentText()

        newVet = (vetLicense, firstName, lastName, contactNo, sex)
        self.veterinarians.append(newVet)
        databaseHandler.addVet(self.veterinarians)
        self.readVet()

        # Clearing the fields after adding new vet
        self.licenseInput.clear()  
        self.firstNameInput.clear() 
        self.lastNameInput.clear()  
        self.contactInput.clear()  
        self.sexInput.setCurrentIndex(-1)

    def addClientClicked(self):

        clientID = None
        lastName = self.clientLastName.text()
        firstName = self.clientFirstName.text()
        contactNo = self.clientContactNo.text()
        address = self.clientAddress.text()
        sex = self.clientSex.currentText()

        # Validate inputs (example validation, adjust according to actual requirements)
        if not lastName or not firstName or not contactNo or not address or not sex:
            QMessageBox.information(self, "Error", "All fields must be filled.")
            return

        newClient = (clientID, firstName, lastName, contactNo, address, sex)
        self.clients.append(newClient)
        databaseHandler.addClients(self.clients)
        self.readClients()

        # Clearing the fields after adding the client
        self.clientLastName.clear()  
        self.clientFirstName.clear()  
        self.clientContactNo.clear()  
        self.clientAddress.clear() 
        self.clientSex.setCurrentIndex(-1) 

    def addPetClicked(self):

        petID = None
        ownerID= self.ownerID.currentText()
        ownerName = self.setClientNameBasedOnID(ownerID)
        petName = self.petName.text()
        species = self.species.currentText()
        breed = self.breed.text()
        birthDate = self.birthDate.text()
        sex = self.sex.currentText()
        status = self.status.currentText()

        # Validates 
        if not petName or not species or not breed or not birthDate or not sex or not status:
            QMessageBox.information(self, "Error", "All fields must be filled.")
            return

        newPet = (petID, ownerID, ownerName, petName, species, breed, birthDate, sex, status) # dictionary for new pet record
        self.pets.append(newPet)
        databaseHandler.addPets(self.pets)
        self.readPets()

        # Clearing the fields after adding new pet
        self.ownerID.setCurrentIndex(-1) 
        self.petName.clear()  
        self.species.setCurrentIndex(-1) 
        self.breed.clear() 
        self.birthDate.clear()
        self.sex.setCurrentIndex(-1) 
        self.status.setCurrentIndex(-1)

    def addAppointmentClicked(self):
        appointmentCode = None
        date = self.date.text()
        schedule = self.schedule.currentText()
        service = self.service.currentText()
        status = self.statusAppointment.currentText()
        vetLicense = self.vetLicense.currentText()
        clientID = self.clientID.currentText()
        petID = self.petID.currentText()
        vetName = self.setVetNameBasedOnID(vetLicense)
        clientName = self.setClientNameBasedOnID(clientID)
        petName = self.setPetNameBasedOnID(petID)

        newAppointment = (appointmentCode, date, schedule, service, status, vetLicense, clientID, petID, vetName, clientName, petName)
        self.appointments.append(newAppointment)
        databaseHandler.addAppointments(self.appointments)
        self.readAppointments()

    def deleteVetClicked(self):
        selectedVet = self.vetTable.selectionModel().selectedRows()

        if not selectedVet:
            QMessageBox.warning(self, "No Selection", "Please select a vet to delete.")
            return
        confirmation = QMessageBox.question(self, "Confirm Deletion",
                                            "Are you sure you want to delete the selected vet?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation != QMessageBox.Yes:
            return

        for index in selectedVet:
            vetLicense = self.vetTable.item(index.row(), 0).text()
            try:
                databaseHandler.deleteVet(vetLicense)
                self.readVet()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete vet: {e}")
                break

    def deleteClientClicked(self):
        selectedClient = self.clientTable.selectionModel().selectedRows()

        if not selectedClient:
            QMessageBox.warning(self, "No Selection", "Please select a client to delete.")
            return
        confirmation = QMessageBox.question(self, "Confirm Deletion",
                                            "Are you sure you want to delete the selected client?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation != QMessageBox.Yes:
            return

        for index in selectedClient:
            clientID = self.clientTable.item(index.row(), 0).text()
            try:
                databaseHandler.deleteClient(clientID)
                self.readClients()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete client: {e}")
                break

    def deletePetClicked(self):
        selectedPet = self.petTable.selectionModel().selectedRows()

        if not selectedPet:
            QMessageBox.warning(self, "No Selection", "Please select a pet to delete.")
            return
        confirmation = QMessageBox.question(self, "Confirm Deletion",
                                            "Are you sure you want to delete the selected pet?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation != QMessageBox.Yes:
            return

        for index in selectedPet:
            petID = self.petTable.item(index.row(), 0).text()
            try:
                databaseHandler.deletePet(petID)
                self.readPets()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete pet: {e}")

    def deleteAppointmentClicked(self):
        selectedAppt = self.apptTable.selectionModel().selectedRows()

        if not selectedAppt:
            QMessageBox.warning(self, "No Selection", "Please select an appointment to delete.")
            return
        confirmation = QMessageBox.question(self, "Confirm Deletion",
                                            "Are you sure you want to delete the selected appointment?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation != QMessageBox.Yes:
            return

        for index in selectedAppt:
            appointmentCode = self.apptTable.item(index.row(), 0).text()
            try:
                databaseHandler.deleteAppointment(appointmentCode)
                self.readAppointments()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete appointment: {e}")

    def itemChanged(self, item):
        print(item.row(), item.column())

    def setVetNameBasedOnID(self, vetIdentification):
        for veterinarian in self.veterinarians:
            vetLicense, firstName, lastName, contactNo, sex = veterinarian
            if str(vetLicense) == vetIdentification:
                self.vetName = f"{firstName} {lastName}"
                return self.vetName
                break

    # Example function to set clientName based on clientID
    def setClientNameBasedOnID(self, clientIdentification):
        for client in self.clients:
            clientID, firstName, lastName, contactNo, address, sex = client
            if str(clientID) == clientIdentification:
                self.clientName = f"{firstName} {lastName}"
                print(self.clientName)
                return self.clientName
                break

    # Example function to set petName based on petID
    def setPetNameBasedOnID(self, petIdentification):
        for pet in self.pets:
            petID, clientID, ownerName, petName, species, breed, birthDate, sex, status = pet
            if str(petID) == petIdentification:
                self.petName = petName
                return self.petName
                break

class editVetWindow(QMainWindow):
    def __init__(self):
        super(editVetWindow, self).__init__()
        uic.loadUi("editVetWindow.ui", self)
        self.show()

def main():
    app = QApplication([])
    window = mainWindow()
    app.exec_()

if __name__ == "__main__":
    main()
