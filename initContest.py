import os
import shutil

baiLam = "baiLam"
deThi = "deThi"
test = "test"

def ifExistContest() -> bool:
    return os.path.exists(baiLam) or os.path.exists(deThi) or os.path.exists(test)

def createContest():

    if os.path.exists(baiLam):
        shutil.rmtree(baiLam)
        pass
    os.mkdir(baiLam)

    if os.path.exists(deThi):
        shutil.rmtree(deThi)
        pass
    os.mkdir(deThi)

    if os.path.exists(test):
        shutil.rmtree(test)
        pass
    os.mkdir(test)