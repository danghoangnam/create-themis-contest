import os
import shutil

def problemExist(problemName):
    if os.path.exists('./deThi/' + problemName):
        return True
    return False

def deleteProblem(problemName):
    shutil.rmtree('./deThi/' + problemName)

def createProblem(problemName):
    os.mkdir('./deThi/' + problemName)