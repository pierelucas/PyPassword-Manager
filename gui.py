# Author: PiereLucas(Julian Huch)
# MIT LICENSE


from appJar import gui


class PyPassGui():

    def __init__(self):

        # Details:
        self.author = "Author: Julian Huch"
        self.version = "Version 1.0"
        
        # Main Window Object
        self.app = gui(title="PyPassword - Manager", geom="400x500")
        
        # Main Windows
        self.app.setTitle("PyPassword - Manager")
        self.app.setIcon("")
        self.app.setResizable(False)
        self.app.setBg("White")

        # Labels: Info Text
        self.app.addLabel(title="Greeter", text="Welcome to PyPassword - Manager")
        self.app.addImage("Greeter", "")

        # Labels: Version Text
        self.app.addLabel(title="Version", text="{0:^40}\n{1:^35}".format(self.version, self.author))

        # Labels: Entry Boxes
        self.app.addLabelEntry(title="Username")
        self.app.setLabel("Username", "Username:")

        self.app.addLabelEntry(title="DBname")
        self.app.setLabel("DBname", "Database:")

        # Buttons:
        self.app.addButton("Login", self.login)
        self.app.addButton("Close", self.app.stop)

        # Statusbar:
        self.app.addStatusbar("Status")
        self.app.setStatusbar("Ready")
        self.app.setStatusbarBg("White")

        # Focus on:
        self.app.setFocus("Username")
        
        # On Stop:
        self.app.setStopFunction(self.checkstop)

    def main(self):
        pass

    def login(self):
        pass

    def checkstop(self):
        return self.app.yesNoBox("Confirm Exit", "Are you sure want to exit the Application?")
    