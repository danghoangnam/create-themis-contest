import os
import shutil

baiLam = "baiLam"
deThi = "deThi"

def ifExistContest() -> bool:
    return os.path.exists(baiLam) or os.path.exists(deThi)

def createContest():

    if os.path.exists(baiLam):
        shutil.rmtree(baiLam)
        pass
    os.mkdir(baiLam)

    if os.path.exists(deThi):
        shutil.rmtree(deThi)
        pass
    os.mkdir(deThi)