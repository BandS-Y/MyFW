import orm.domain_objects
from orm.exception import RecordNotFoundException, DbCommitException, DbUpdateException, DbDeleteException

"""
Паттерн DATA MAPPER
Слой преобразования данных
"""


class PersonMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_id(self, id_person):
        statement = f"SELECT IDPERSON, FIRSTNAME, LASTNAME,  email, telephone FROM PERSON WHERE IDPERSON=?"

        self.cursor.execute(statement, (id_person,))
        result = self.cursor.fetchone()
        if result:
            return orm.domain_objects.Person(*result)
        else:
            raise RecordNotFoundException(f'record with id={id_person} not found')

    def insert(self, person):
        statement = f"INSERT INTO PERSON (FIRSTNAME, LASTNAME,  email, telephone) VALUES (?, ?, ?, ?)"
        self.cursor.execute(statement, (person.first_name, person.last_name, person.email, person.telephone))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, person):
        statement = f"UPDATE PERSON SET FIRSTNAME=?, LASTNAME=? ,  email=?, telephone=? WHERE IDPERSON=?"
        self.cursor.execute(statement, (person.first_name, person.last_name, person.email, person.telephone,
                                        person.id_person))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, person):
        statement = f"DELETE FROM PERSON WHERE IDPERSON=?"
        self.cursor.execute(statement, (person.id_person,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class CategoryMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_id(self, id_category):
        statement = f"SELECT idcategory, categoryname FROM categories WHERE idcategory=?"

        self.cursor.execute(statement, (id_category,))
        result = self.cursor.fetchone()
        if result:
            return orm.domain_objects.Category(*result)
        else:
            raise RecordNotFoundException(f'record with id={id_category} not found')

    def insert(self, my_category):
        print('try insert(self, category) 1')
        statement = f"INSERT INTO categories (categoryname) VALUES (?)"
        print(statement, my_category.name)
        self.cursor.execute(statement, my_category.name)
        print(statement, my_category.name)
        try:
            print('try insert(self, category) 2')
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, category):
        statement = f"UPDATE categories SET categoryname=? WHERE idcategory=?"
        self.cursor.execute(statement, (category.name, category.id_category))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, category):
        statement = f"DELETE FROM categories WHERE idcategory=?"
        self.cursor.execute(statement, (category.id_category,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class LevelMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_id(self, id_level):
        statement = f"SELECT idlevel, levelname FROM levels WHERE idlevel=?"

        self.cursor.execute(statement, (id_level,))
        result = self.cursor.fetchone()
        if result:
            return orm.domain_objects.Level(*result)
        else:
            raise RecordNotFoundException(f'record with id={id_level} not found')

    def insert(self, my_level):
        print('try insert(self, levels) 1')
        statement = f"INSERT INTO levels (levelname) VALUES (?)"
        print(statement, my_level.name)
        self.cursor.execute(statement, my_level.name)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, level):
        statement = f"UPDATE levels SET levelname=? WHERE idlevel=?"
        self.cursor.execute(statement, (level.name, level.id_level))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, level):
        statement = f"DELETE FROM levels WHERE idlevel=?"
        self.cursor.execute(statement, (level.id_level,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class TypeMapper:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_id(self, id_type):
        statement = f"SELECT idtype, typename FROM types WHERE idtype=?"

        self.cursor.execute(statement, (id_type,))
        result = self.cursor.fetchone()
        if result:
            return orm.domain_objects.Level(*result)
        else:
            raise RecordNotFoundException(f'record with id={id_type} not found')

    def insert(self, type):
        statement = f"INSERT INTO types (typename) VALUES (?)"
        self.cursor.execute(statement, type.name)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, type):
        statement = f"UPDATE types SET typename=? WHERE idtype=?"
        self.cursor.execute(statement, (type.name, type.id_type))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, type):
        statement = f"DELETE FROM types WHERE idtype=?"
        self.cursor.execute(statement, (type.id_type,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)

