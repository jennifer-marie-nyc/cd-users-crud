from mysqlconnection import connectToMySQL

class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id =  data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(cls.DB).query_db(query)
        all_users = []
        for user in results:
            all_users.append(cls(user))
        return all_users
    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());'
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def get_user_by_id(cls, user_id):
        query = 'SELECT * FROM users WHERE id=%(id)s;'
        data = {'id': user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        selected_user = cls(results[0])
        return selected_user
    @classmethod
    def update_user(cls, data):
        query = """
                UPDATE users
                SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at=NOW()
                WHERE id=%(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    @classmethod
    def delete_user(cls, user_id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {'id': user_id}
        return connectToMySQL(cls.DB).query_db(query, data)
