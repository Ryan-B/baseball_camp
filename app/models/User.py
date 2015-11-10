from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create(self, user_info):
        errors = []
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

        if not user_info['camper_first']:
            errors.append('First Name cannot be blank')
        elif len(user_info['camper_first']) < 2:
            errors.append('First Name must be at least 2 charaters long')

        if not user_info['camper_last']:
            errors.append('Last Name cannot be blank')
        elif len(user_info['camper_last']) < 2:
            errors.append('Last Name must be at least 2 charaters long')

        if not user_info['parent_first']:
            errors.append('First Name cannot be blank')
        elif len(user_info['parent_first']) < 2:
            errors.append('First Name must be at least 2 charaters long')

        if not user_info['parent_last']:
            errors.append('Last Name cannot be blank')
        elif len(user_info['parent_last']) < 2:
            errors.append('Last Name must be at least 2 charaters long')

        if not user_info['email']:
            errors.append('Email cannot be blank')
        elif len(user_info['email']) < 2:
            errors.append('Email must be at least 2 charaters long')
        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append('Email is not valid')

        if not user_info['camper_password']:
            errors.append('Camper Password cannot be blank')
        elif not user_info['camper_password_confirm']:
            errors.append('Camper Password confirmation cannot be blank')
        elif len(user_info['camper_password']) < 1:
            errors.append('Password must be at least 5 charaters long')
        elif user_info['camper_password'] != user_info['camper_password_confirm']:
            errors.append("Camper's Passwords do not match")

        if not user_info['parent_password']:
            errors.append('Parent Password cannot be blank')
        elif not user_info['parent_password_confirm']:
            errors.append('Parent Password confirmation cannot be blank')
        elif len(user_info['parent_password']) < 1:
            errors.append('Password must be at least 5 charaters long')
        elif user_info['parent_password'] != user_info['parent_password_confirm']:
            errors.append("Parent's Passwords do not match")

        if errors:
            return {'status': False, 'errors': errors}
        else:
            pw_hash = self.bcrypt.generate_password_hash(user_info['camper_password'])
            pw_hash2 = self.bcrypt.generate_password_hash(user_info['parent_password'])
            insert_query = "INSERT INTO registered_campers (camper_first, camper_last, parent_first, parent_last, email, phone_number, home_address, camper_password, parent_password, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}','{}', NOW(), NOW())".format(user_info['camper_first'], user_info['camper_last'], user_info['parent_first'], user_info['parent_last'], user_info['email'], user_info['phone_number'], user_info['home_address'], pw_hash, pw_hash2)
            self.db.query_db(insert_query)
            get_user_query = "SELECT * FROM registered_campers ORDER BY id DESC LIMIT 1"
            user = self.db.query_db(get_user_query)
            print user
            return {'status': True, 'user': user[0]}

    def sign_in(self, user_info):
        sign_in_query = "SELECT * FROM registered_campers WHERE email = '{}'".format(user_info['email'])
        user = self.db.query_db(sign_in_query)
        if user and self.bcrypt.check_password_hash(user[0]['parent_password'], user_info['parent_password']):
            return {'status': True, 'user': user[0]}
        else:
            return {'status': False}

    def get_all_campers(self):
        get_all_campers_query = "SELECT * FROM registered_campers ORDER BY id DESC"
        return self.db.query_db(get_all_campers_query)

    def get_one_camper(self, id):
        get_one_camper_query = "SELECT * FROM registered_campers WHERE id = '{}'".format(id)
        print  get_one_camper_query
        return self.db.query_db(get_one_camper_query)

    def favorite(self, favorite_info, id):
        print favorite_info['pizza']
        favorite_query = "UPDATE registered_campers SET pizza = '{}', favorite_baseball = '{}', favorite_seahawk = '{}', favorite_book = '{}' WHERE id = '{}'".format(favorite_info['pizza'],favorite_info['favorite_baseball'], favorite_info['favorite_seahawk'], favorite_info['favorite_book'], id)
        print favorite_query
        return self.db.query_db(favorite_query) 

















