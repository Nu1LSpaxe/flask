# Delete
# In SQL called 'Delete'

from CRUD.model import User
from CRUD.model import app, db

def delete_user(username):
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()

# with app.app_context():
#     delete_user('admin')

# Check result
from CRUD.readUser import read_all_user, read_user_by_id
with app.app_context():
    print(read_all_user())
    print(read_user_by_id(2))