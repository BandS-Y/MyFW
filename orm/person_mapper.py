import orm.db_exeption
from orm.domain_object import Person


class PersonMapper:
    """
    Паттерн DATA MAPPER
    Слой преобразования данных
    """

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_id(self, id_person):
        statement = f"SELECT IDPERSON, FIRSTNAME, LASTNAME FROM PERSON WHERE IDPERSON=?"

        self.cursor.execute(statement, (id_person,))
        result = self.cursor.fetchone()
        if result:
            return Person(*result)
        else:
            raise orm.RecordNotFoundException(f'record with id={id_person} not found')

    def insert(self, person):
        statement = f"INSERT INTO PERSON (FIRSTNAME, LASTNAME) VALUES (?, ?)"
        self.cursor.execute(statement, (person.first_name, person.last_name))
        try:
            self.connection.commit()
        except Exception as e:
            raise orm.DbCommitException(e.args)

    def update(self, person):
        statement = f"UPDATE PERSON SET FIRSTNAME=?, LASTNAME=? WHERE IDPERSON=?"
        self.cursor.execute(statement, (person.first_name, person.last_name, person.id_person))
        try:
            self.connection.commit()
        except Exception as e:
            raise orm.DbUpdateException(e.args)

    def delete(self, person):
        statement = f"DELETE FROM PERSON WHERE IDPERSON=?"
        self.cursor.execute(statement, (person.id_person,))
        try:
            self.connection.commit()
        except Exception as e:
            raise orm.DbDeleteException(e.args)

