import tempfile
import fileinput
import re

class Preprocessor(object):
    """the preprocessor object"""
    def __init__(self, path):
        self.path_ = path
        self.tmpFilePath_ = ""

        self.temp_file_ = tempfile.NamedTemporaryFile()

        


    def run(self):
        """start preprocessing the file"""

        with open(self.path_, "r") as file:
            for line in file:
                if(self.isPreprocessorLine(line)):
                    if(self.whatPreprocessorDirective(line) == "define"):
                        print line
        

    def replace(self, what, value):
        """replaces what with the value"""
       
    

    def isPreprocessorLine(self, line):
        b = ""
        pos = 0;

        for s in line:
            pos += 1
            if(b == "" and s == "#"):
                return True
            else:
                if(b == ""):
                    b = s
                else:
                    return False

    def whatPreprocessorDirective(self, line):
        b = ""
        
        for index in range(len(line)):
            
            if(b == "" and line[index] == "#"):
                index += 1
                if(line.find("define", index) >= 0):
                    return "define"
                elif(line.find("elif", index) >= 0):
                    return "elif"
                if(line.find("else", index) >= 0):
                    return "else"
                elif(line.find("ifndef", index) >= 0):
                    return "ifndef"
                elif(line.find("error", index) >= 0):
                    return "error"
                elif(line.find("if", index) >= 0):
                    return "if"
                elif(line.find("ifdef", index) >= 0):
                    return "ifdef"
                elif(line.find("pragma", index) >= 0):
                    return "pragma"
                elif(line.find("import", index) >= 0):
                    return "import"
                elif(line.find("include", index) >= 0):
                    return "include"
                elif(line.find("line", index) >= 0):
                    return "line"
                elif(line.find("undef", index) >= 0):
                    return "undef"
                elif(line.find("using", index) >= 0):
                    return "using"
                elif(line.find("endif", index) >= 0):
                    return "endif"
                else:
                    return False

