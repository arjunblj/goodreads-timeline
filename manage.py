
import os
import sys

from flask.ext.script import Manager, Server

from bookviz import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

manager = Manager(app)

# Turn on debugger and reloader by default.
manager.add_command("runserver", Server(
    use_debugger = app.config['DEBUG'],
    use_reloader = app.config['USE_RELOADER'])
)

if __name__ == "__main__":
    manager.run()
