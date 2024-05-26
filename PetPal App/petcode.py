import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk
from PyQt5 import uic
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
        

class Pet():

    def showPetData(self):
        try:
            connection = mysql.connector.connect(host = "localhost",port = 3306,user = "root",password = "admin123",database = "pet")
        except mysql.connector.Error as error:
            messagebox.showerror("Connection Error", "Error connecting to the database")


    def addNewPet(self):

        petID = self.petID.get()
        clientID = self.clientID.get()
        ownerName = self.ownerName.get()
        name = self.name.get()
        breed = self.breed.get()
        species = self.species.get()
        birthDate= self.birthDate.get()
        sexOr = self.sexOr.get()
        status = self.status.get()

        # Connect to Pet Database
        try:

            connection = mysql.connector.connect(host = "localhost",port = 3306,user = "root",password = "admin123",database = "petpal_clinic")
            cursor = connection.cursor()

            # Execution of SQL Query that inserts data about pets to Table
            cursor.execute(""" INSERT INTO pets(petID,clientID,ownerName,petName,breed,species,birthDate,sexOr,status
                           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (petID,clientID,ownerName,name,breed,species,birthDate,sexOr,status))
    
            connection.commit()
            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "New Pet Addedd Successfully")
        except mysql.connector.Error as error:
            messagebox.showerror("Connection Error", "Error connecting to the database")

    def deletePet(self):

        connection = mysql.connector.connect(host = "localhost",port = 3306,user = "root",password = "admin123",database = "pet")