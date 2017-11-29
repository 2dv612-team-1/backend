from mongo_client import db_conn

"""Auth admin by comparing username and password in admin collection"""


def auth_and_return_admin(form):
    username = form['username']
    password = form['password']

    found_admin = db_conn.admin.find_one({'username': username, 'password': password})
    return found_admin


"""Creates default admin account in admin collection"""


def create_default_admin(self):
    default_admin = {
        'username': 'admin',
        'password': 'admin123',
        'role': 'admin'
    }

    db_conn.admin.update({}, default_admin, upsert=True)