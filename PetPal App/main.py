from PyQt5.QtCore import Qt,QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QHeaderView, QComboBox, QMessageBox
from PyQt5 import uic
import mysql.connector
import re


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
    def addVet(veterinarians):

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM vets")
            addVetQuery = "INSERT INTO vets (vetLicense, firstName, lastName, contactNo, sex) VALUES (%s, %s, %s, %s, %s)"

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

    def deleteVet(self):
        
        selectedVet = self.vetTable.selectionModel().selectedRows() # checks if any row is selected

        vetToDelete = self.vetTable.item(selectedVet[0].row(),0).text()

        # Delete the row from the database
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            deleteVetQuery = "DELETE FROM your_table_name WHERE id = %s"
            cursor.execute(deleteVetQuery, (vetToDelete,))
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
                password='admin123',
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
                sex
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

    def deleteClient(petpal_clinic, clients):

        try:  # Connect to Database

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
        print(pets)
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM pets")
            addPetQuery = """
            INSERT INTO pets (
                petID,
                ownerID,
                ownerName,
                petName,
                species,
                breed,
                birthDate,
                sex,
                status,
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for pet in pets:
                petID, ownerID, ownerName, petName, species, breed, birthDate, sex, status = pet
                cursor.execute(addPetQuery,(petID, ownerID, ownerName, petName, species, breed, birthDate, sex, status))
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
    def addAppointment(appointments):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin123',
                database='petpal_clinic'
            )
            cursor = connection.cursor()
            cursor.execute("TRUNCATE TABLE appointments")
            addAppointmentQuery = """
            INSERT INTO appointments (
                appointmentCode, 
                requesteeID, 
                attendingVet, 
                petID, 
                requesteeName,
                attendingVetName,
                petName,
                date,
                timeSched,
                service,
                status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for appointment in appointments:
                appointmentCode, requesteeID, attendingVet, petID, requesteeName, attendingVetName, petName, date,timeSched,service,status = appointment
                cursor.execute(addAppointmentQuery,(appointmentCode, requesteeID, attendingVet, petID, requesteeName, attendingVetName, petName, date,timeSched,service,status))
            connection.commit()

        except mysql.connector.Error as err:
            print(f"Error saving appointments: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

class bookingWindow(QMainWindow):

    def __init__(self):

        super(mainWindow, self).__init__()
        uic.loadUi("bookApptmntWindow.ui", self)
        self.show()


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
            clientID = client[0]
            self.ownerID.addItem(str(clientID))

        for veterinarian in self.veterinarians:
            vetLicense = veterinarian[0]
            self.mainVet.addItem(str(vetLicense))

        for pet in self.pets:
            petID = petID[0]
            self.petID.addItem(str(petID))

        for appointment in self.appointments:
            appointmentCode = appointmentCode[0]
            self.appointmentCode.addItem(str(appointmentCode))

        self.homeButton.clicked.connect(self.homeClicked)
        self.clientButton.clicked.connect(self.clientClicked)
        self.petButton.clicked.connect(self.petClicked)
        self.vetButton.clicked.connect(self.vetClicked)
        self.bookAppointmentButton.clicked.connect(self.bookAppointmentClicked)
        self.deleteVetButton.clicked.connect(self.deleteVetClicked)

        addVetButton = self.stackedWidget.findChild(QPushButton, 'addButton')
        addVetButton.clicked.connect(self.addVetClicked)
        addClientButton = self.stackedWidget.findChild(QPushButton, 'addClientButton')
        addClientButton.clicked.connect(self.addClientClicked)
        addPetButton =self.stackedWidget.findChild(QPushButton, 'addPetButton')
        addPetButton.clicked.connect(self.addPetClicked)
        bookAppointmentButton = self.frame.findChild(QPushButton, 'bookAppointmentButton')
        bookAppointmentButton.clicked.connect(self.bookAppointmentClicked)

        self.readVet()
        self.readClients()
        self.readPets()
        self.readAppts()

    # DISPLAY DATABASE ---------------------------------------------------------------------------------------------

    def readVet(self):
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

            pet_id, client_id, owner_name, pet_name, species, breed, birth_date, sex, status = pet
            items = [QTableWidgetItem(str(item)) for item in
                     [pet_id, client_id, owner_name, pet_name, species, breed, birth_date, sex, status]]
            for i, item in enumerate(items):
                self.petTable.setItem(row_position, i, item)

        self.petTable.horizontalHeader()
    
    def readAppts(self):
        self.appointments = databaseHandler.fetchData("appointments")
        self.apptTable.setRowCount(0)
        self.apptTable.setColumnCount(8)

        for appointment in self.appointments:
            row_position = self.apptTable.rowCount()
            self.apptTable.insertRow(row_position)

            appointmentCode, requesteeID, attendingVet, petID, requesteeName, attendingVetName, petName, date,timeSched,service,status = appointment
            items = [QTableWidgetItem(str(item)) for item in
                     [appointmentCode, requesteeID, attendingVet, petID, requesteeName, attendingVetName, petName, date,timeSched,service,status]]
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
    
    def bookAppointmentClicked(self):
        
        # Create an instance of bookAppointmentWindow and show it
        self.bookingWindow = bookAppointmentWindow()
        self.bookingWindow.show()

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
        ownerName = None
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

    def deleteVetClicked(self):

        selectedVet = self.vetTable.selectionModel().selectedRows() # checks if any row is selected
        
        if not selectedVet:
            QMessageBox.warning(self, "No Selection", "Please select a vet to delete.")
            return
        
        # Confirm deletion
        confirmation = QMessageBox.question(self, "Confirm Deletion",
                                    "Are you sure you want to delete the selected vet?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation != QMessageBox.Yes:
            return
        
        vetToDelete = self.vetTable.item(selectedVet[0].row(),0).text()

        for index in selectedVet:
            vetLicense = self.vetTable.model().data(index, Qt.DisplayRole)
            
            try:
                # Attempt to delete the vet from the database
                databaseHandler.deleteVet(vetLicense)
                
                # Remove the row from the table view
                for index in reversed(selectedVet):  # Iterate in reverse to avoid index shifting
                    self.vetTable.removeRow(index.row())
                
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to delete vet: {e}")
                break  # Stop processing further deletions on error
            
        else:
            # Refresh the vet list if all deletions were successful
            self.readVet()
            QMessageBox.information(self, "Success", "Selected vets deleted successfully.")

class bookAppointmentWindow(QMainWindow):

    def __init__(self):
        super(bookAppointmentWindow, self).__init__()
        uic.loadUi("bookApptmntWindow.ui", self)
        self.show()


def main():
    app = QApplication([])
    window = mainWindow()
    app.exec_()


if __name__ == "__main__":
    main()
