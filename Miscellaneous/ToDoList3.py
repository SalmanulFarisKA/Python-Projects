import sys
from PyQt5.QtWidgets import *

# Create main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("To-Do List")

# Create list widget to hold to-do items
todo_list = QListWidget()

# Create function to add items to list
def add_item():
    item = entry.text()
    todo_list.addItem(item)
    entry.clear()

# Create function to remove selected items from list
def remove_selected():
    for item in todo_list.selectedItems():
        todo_list.takeItem(todo_list.row(item))

# Create entry field and button to add items to list
entry = QLineEdit()
add_button = QPushButton("Add")
add_button.clicked.connect(add_item)

# Create button to remove selected items from list
remove_button = QPushButton("Remove Selected")
remove_button.clicked.connect(remove_selected)

# Create layout and add widgets
layout = QVBoxLayout()
layout.addWidget(todo_list)
layout.addWidget(entry)
layout.addWidget(add_button)
layout.addWidget(remove_button)

window.setLayout(layout)
window.show()

# Run main loop
app.exec_()
