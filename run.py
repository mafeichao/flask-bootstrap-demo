from app import app

from flask_script import Manager

mgr = Manager(app)

if __name__ == "__main__":
    mgr.run()
