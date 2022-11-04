from datetime import date
from .config import configdb
import mysql.connector

class Contact:

    # Constructeur
    def __init__(self, id, firstname, lastname, birth_date, phone, email): 
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birth_date = birth_date
        self.phone = phone
        self.email = email

    # Permet de retourner l'age comme un attribut de l'objet
    @property
    def full_name(self): 
        return f'{self.firstname[:1].upper()}{self.firstname[1:].lower()} {self.lastname.upper()}'

    # La soustraction est un booléen qui retourne 0 ou 1 selon l'age de la personne
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
        
    def __str__(self): 
        return f"""
        id : {self.id}
        identité : {self.full_name}
        age : {self.age}
        telephone : {self.phone}
        email : {self.email}
        """
    
    # Récupérer la liste des contacts
    @staticmethod
    def get_all_contacts():

        contacts = []

        with mysql.connector.connect(**configdb) as db: 
            with db.cursor() as cursor:
                query = "SELECT id, firstname, lastname, birth_date, phone, email FROM contact"
                try:
                    cursor.execute(query)
                    results = cursor.fetchall()

                    # Parcours du jeu de résultats pour créer des contacts et les ajouter dans un tableau
                    for id, firstname, lastname, birth_date, phone, email in results:
                        contact = Contact(id, firstname, lastname, birth_date, phone, email)
                        contacts.append(contact)
                
                except Exception as ex:
                    print(ex)
        return contacts

    # Récupérer un contact par son identifiant unique
    @staticmethod
    def get_contact_by_id(id):
        contact = None
        with mysql.connector.connect(**configdb) as db:
            with db.cursor() as cursor:
                query = "SELECT id, firstname, lastname, birth_date, phone, email FROM contact WHERE id=%s"
                try:
                    cursor.execute(query, (id,))
                    result = cursor.fetchone()
                    contact = Contact(result[0], result[1], result[2], result[3], result[4], result[5])
                except Exception as ex:
                    print(ex)
        return contact

    # Supprimer un contact par son identifiant unique
    @staticmethod
    def delete_contact(id):
        result = 0
        with mysql.connector.connect(**configdb) as db:
            with db.cursor() as cursor:
                query = "DELETE FROM contact WHERE id = %s"
                try:
                    cursor.execute(query, (id,))
                    db.commit()
                    result = cursor.rowcount
                except Exception as ex:
                    db.rollback()
                    print(ex)
        return result == 1

    # ajouter un contact
    @staticmethod
    def add_contact(contact):
        result = None
        with mysql.connector.connect(**configdb) as db:
            with db.cursor() as cursor:
                query = "INSERT INTO contact(firstname, lastname, birth_date, phone, email) VALUES (%s, %s, %s, %s, %s)"

                values = (contact.firstname, contact.lastname, contact.birth_date, contact.phone, contact.email)

                try:
                    cursor.execute(query, values)
                    db.commit()
                    contact.id = cursor.lastrowid
                    result = contact
                except Exception as ex:
                    print(ex)

        return result

    @staticmethod
    def update_contact(contact):
        result = None
        with mysql.connector.connect(**configdb) as db:
            with db.cursor() as cursor:
                query = "UPDATE contact SET firstname = %s, lastname = %s, birth_date = %s, phone = %s, email = %s WHERE id = %s"
                values = (contact.firstname, contact.lastname, contact.birth_date, contact.phone, contact.email, contact.id)

                try:
                    cursor.execute(query, values)
                    db.commit()
                    result = contact
                except Exception as ex:
                    print(ex)

        return result