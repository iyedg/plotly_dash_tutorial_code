from . import callbacks
from .app import app
from .layouts import layout

app.layout = layout

if __name__ == "__main__":
    app.run_server(host="localhost", debug=True)
