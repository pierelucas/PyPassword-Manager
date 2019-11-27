# Author: PiereLucas(Julian Huch)
# MIT LICENSE


from appJar import gui


class PyPassGui():

    def __init__(self):

        self.username = ""
        self.db_name = ""

        # Details:
        self.author = "Author: Julian Huch"
        self.version = "Version 1.0"
        
        # Main Window Object
        self.app = gui(title="PyPassword - Manager", geom="300x300")
        
        # Main Windows
        self.app.setTitle("PyPassword - Manager")
        #self.app.setIcon("")
        self.app.setResizable(False)
        self.app.setBg("White")

        # Labels: Info Text
        self.app.addLabel(title="Greeter", text="Welcome to PyPassword - Manager")
        #self.app.addImage("Greeter", "")

        # Labels: Version Text
        self.app.addLabel(title="Version", text="{0:^40}\n{1:^35}".format(self.version, self.author))

        # Buttons:
        self.app.addButtons(["Write", "Read", "Show all", "Delete"], self.main)
        self.app.addButton("Close", self.app.stop)

        # Statusbar:
        self.app.addStatusbar("Status")
        self.app.setStatusbarBg("White")

        # On Stop:
        self.app.setStopFunction(self.checkstop)

        # Login SubWindow
        self.app.startSubWindow(name="Login")
        self.app.addLabel("l2", "Login Window")

        self.app.addLabelEntry(title="Username")
        self.app.setLabel("Username", "Username:")

        self.app.addLabelEntry(title="DBname")
        self.app.setLabel("DBname", "Database:")

        self.app.addButton("SUBMIT", self.login)

        self.app.setFocus("Username")

        self.app.stopSubWindow()

    def main(self):
        pass

    def login(self):
        self.app.hideSubWindow("Login")

        self.username = self.app.getEntry("Username")
        self.db_name = self.app.getEntry("DBname")

        self.app.setStatusbar("Hello [%s] you successfully logged into [%s]" % (self.username, self.db_name))
        self.app.show()

    def checkstop(self):
        return self.app.yesNoBox("Confirm Exit", "Are you sure want to exit the Application?")

    def run(self):
        self.app.go(startWindow="Login")

if __name__ == "__main__":
    ppg = PyPassGui()
    ppg.run()