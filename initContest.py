import os
import shutil

baiLam = "baiLam"
deThi = "deThi"
stress = "stress"

def ifExistContest() -> bool:
    return os.path.exists(baiLam) or os.path.exists(deThi) or os.path.exists(stress)

def createContest():
    if os.path.exists(baiLam):
        shutil.rmtree(baiLam)
    os.mkdir(baiLam)

    if os.path.exists(deThi):
        shutil.rmtree(deThi)
    os.mkdir(deThi)

    if os.path.exists(stress):
        shutil.rmtree(stress)
    os.mkdir(stress)