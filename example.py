from PyQt5 import QtWidgets
from PyQt5.Qt import Qt

import syntax_pars
from paren_highlight import TextEdit

app = QtWidgets.QApplication([])
editor = TextEdit()
editor.setStyleSheet("""QPlainTextEdit{font: 8pt "Courier New"; color: #383a42; background-color: #fafafa;}""")

highlight = syntax_pars.PythonHighlighter(editor.document())
editor.show()

# Load syntax.py into the editor for demo purposes
text = r"""import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True

FLATPAGES_AUTO_REALOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)

pages = FlatPages(app)

class idk:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __eq__(self):
        print("UwU")

@app.route('/<path:path>.html')
def page(path):
    print("Page funcion running")
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()"""
editor.setPlainText(text)

editor.setFixedSize(500, 500)
app.exec_()
