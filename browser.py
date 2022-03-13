import os
import webbrowser

# Opens the Results html file
class Results:

    # Pass in file to be opened
    def __init__(self, name):
        self.name = name
        self.file = 'file:///'+os.getcwd()+'/'+self.name

    def showResults(self):
        webbrowser.open_new_tab(self.file)
