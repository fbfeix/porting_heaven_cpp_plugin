'''
import porting_heaven

class CppParser(porting_heaven.iSourceCodeSynchronizer):
       
    def loadFromFile(iSourceCodeSynchronizer, str):
        return super(CppParser, iSourceCodeSynchronizer).loadFromFile(str)

    def saveToFile(iSourceCodeSynchronizer, str):
        return super(CppParser, iSourceCodeSynchronizer).saveToFile(str)

        '''



from Preprocessor import Preprocessor

pr = Preprocessor("example.hpp")
pr.run()
