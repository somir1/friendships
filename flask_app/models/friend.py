from flask_app.config.mysqlconnection import connectToMySQL

class User():

    def __init__(self, data=None):
        if data != None:
            self.id = data['id']
            self.first_name = data['first_name']
            self.last_name = data['last_name']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
            self.friends = None

    @classmethod
    def get_all(cls):
        query = """SELECT users.id, users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name, friendships.friend_id  
        FROM users JOIN friendships ON users.id = friendships.users_id LEFT JOIN users as user2 on user2.id = friendships.friend_id"""
        results = connectToMySQL('friendships_schema').query_db(query)
        return results

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users(first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        
        return connectToMySQL('friendships_schema').query_db(query, data)

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('friendships_schema').query_db(query)
        return results

    @classmethod
    def make_friends(cls, data):
        print(data)
        query = "INSERT INTO friendships(users_id, friend_id) VALUES(%(users_id)s, %(friend_id)s);"

        return connectToMySQL('friendships_schema').query_db(query, data)

            


