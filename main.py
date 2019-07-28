import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
print("Running FLASK_APP: {}".format(os.getenv('FLASK_APP') or __file__))


@app.shell_context_processor
def make_shell_context():
    return None


if __name__ == '__main__':
    app.run(debug=True,
            use_debugger=False,
            use_reloader=False,
            passthrough_errors=True)
