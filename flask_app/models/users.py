from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def view(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL("esquema_usuarios").query_db(query)
        user = []
        for d in results:
            user.append(cls(d))
        return user

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(mail)s)"
        result = connectToMySQL("esquema_usuarios").query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM users WHERE id = (%(id)s)"
        result = connectToMySQL("esquema_usuarios").query_db(query, formulario)
        return result
    
    @classmethod
    def buscar(cls, formulario):
        query = "SELECT * FROM users WHERE id = (%(id)s)"
        result = connectToMySQL("esquema_usuarios").query_db(query, formulario)
        return result

    @classmethod
    def edit(cls, formulario):
        query = "UPDATE users SET first_name = (%(fname)s), last_name = (%(lname)s), email = (%(mail)s) WHERE  id = (%(id)s)"
        result = connectToMySQL("esquema_usuarios").query_db(query, formulario)
        return result
        


