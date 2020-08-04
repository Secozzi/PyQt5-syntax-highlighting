from PyQt5 import QtWidgets
from PyQt5.Qt import Qt

import syntax_pars
from paren_highlight import TextEdit

app = QtWidgets.QApplication([])
editor = TextEdit()
editor.setStyleSheet("""QPlainTextEdit{font: 8pt "Courier New"; color: #383a42; background-color: #fafafa;}""")

highlight = syntax_pars.PythonHighlighter(editor.document())
editor.show()

# Load paren_highlight into the editor for demo purposes
#text = open("paren_highlight.py", "r")
editor.setPlainText("text.read()")

editor.setFixedSize(800, 800)
app.exec_()
