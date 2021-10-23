from cryptography.fernet import Fernet
import os

os.chdir('C:/Users/Dynamic/Desktop/Code/python/playaround')
#path should be changed to suit user

print("changed dir")

if (os.path.exists('C:/Users/Dynamic/Desktop/Code/python/playaround/filekey.key')) == False:
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
else:
    print('Hmmmm, seems theres already a key')
    try:
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

    except:
        print("There seems to be an exeption")

# using the generated key
fernet = Fernet(key)

import sys
import random
from PyQt5 import QtCore, QtWidgets, QtGui

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.encrypt_btn = QtWidgets.QPushButton("Encrypt")
        self.decrypt_btn = QtWidgets.QPushButton("Decrypt")
        self.text = QtWidgets.QLabel("Encrypted Journal (v.1)", alignment = QtCore.Qt.AlignCenter)
        self.text_box = QtWidgets.QTextEdit()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.encrypt_btn)
        self.layout.addWidget(self.decrypt_btn)

        self.encrypt_btn.clicked.connect(self.encrypt)
        self.decrypt_btn.clicked.connect(self.decrypt)
        # self.text_box.textChanged.connect(self.encrypt)

        # self.key = Fernet.generate_key()
        # self.encryption = Fernet(self.key)


    def encrypt(self):
        text_in_box = self.text_box.toPlainText()
        encrypted_text = fernet.encrypt(text_in_box.encode())
        self.text_box.setText(encrypted_text.decode())


    def decrypt(self):
        text_in_box = self.text_box.toPlainText().encode()
        decrypted_message = fernet.decrypt(text_in_box).decode()
        self.text_box.setText(decrypted_message)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MainWidget()
    widget.resize(800,600)
    widget.show()   

    sys.exit(app.exec())
