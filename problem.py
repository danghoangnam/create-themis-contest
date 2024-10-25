import os
import shutil
import tools

def problemExist(problemName):
    if os.path.exists('./deThi/' + problemName):
        return True
    return False

def deleteProblem(problemName):
    shutil.rmtree('./deThi/' + problemName)

def createProblem(problemName):
    os.mkdir('./deThi/' + problemName)

def addTest(problemName):
    fi = input("Nhập tên file input: ")
    fo = input("Nhập tên file output: ")

    stt = len(list(filter(lambda x: x if x.find('.') != -1 else None,os.listdir('./deThi/' + problemName + '/'))))
    while True:
        path = './deThi/' + problemName + '/' + 'test' + str(stt)
        os.mkdir(path)

        with open(path + '/' + fi, 'w') as f:
            dataIn = []
            print("Nhập dữ liệu input (nhập EOF để kết thúc đoạn dữ liệu):")
            while True:
                tmp = input('> ')
                if tmp == 'EOF':
                    break
                dataIn.append(tmp)

            f.write('\n'.join(dataIn))

        with open(path + '/' + fo, 'w') as f:
            dataOut = []
            print("Nhập dữ liệu output (nhập EOF để kết thúc đoạn dữ liệu):")
            while True:
                tmp = input('> ')
                if tmp == 'EOF':
                    break
                dataOut.append(tmp)
            f.write('\n'.join(dataOut))

        stt += 1

        if tools.yesOrNo("Bạn có muốn thêm testcase không") == False:
            break