import os
import shutil
import tools
import json

# config.json structure:
# {
#     "name": "Tên bài tập",
#     "test_cases": [ Danh sách các test case ],
#     "input_file": "Tên file input.",
#     "output_file": "Tên file output.",
# }

class problem:
    name = ""
    test_cases = []
    input_file = ""
    output_file = ""
    
    def setInputFile(self, input_file):
        self.input_file = input_file

    def setOutputFile(self, output_file):
        self.output_file = output_file

    def configExist(self):
        if os.path.exists('./deThi/' + self.name + '/config.json'):
            return True
        return False
    
    def saveConfig(self):
        config = {
            'name': self.name,
            'test_cases': self.test_cases,
            'input_file': self.input_file,
            'output_file': self.output_file
        }
        with open('./deThi/' + self.name + '/config.json', 'w') as f:
            json.dump(config, f, indent=4)
    
    def updateTestCaseList(self):
        dirs = [i for i in os.listdir('./deThi/' + self.name) if os.path.isdir(os.path.join('./deThi/' + self.name, i))]
        self.test_cases = [i for i in os.listdir('./deThi/' + self.name) if os.path.isdir(os.path.join('./deThi/' + self.name, i))]

    def loadConfig(self):
        if not self.configExist():
            return
        
        # Load the configuration from the JSON file
        with open('./deThi/' + self.name + '/config.json', 'r') as f:
            config = json.load(f)
        self.name = config.get('name', self.name)
        self.test_cases = config.get('test_cases', [])
        self.input_file = config.get('input_file', self.input_file)
        self.output_file = config.get('output_file', self.output_file)

        self.updateTestCaseList()
    
    def addTestCase(self, test_case_name, input_data, output_data):
        if not os.path.exists('./deThi/' + self.name + '/' + test_case_name):
            os.mkdir('./deThi/' + self.name + '/' + test_case_name)
            self.test_cases.append(test_case_name)
            with open(os.path.join('./deThi', self.name, test_case_name, self.input_file), 'w') as f_in:
                f_in.write(input_data)
            with open(os.path.join('./deThi', self.name, test_case_name, self.output_file), 'w') as f_out:
                f_out.write(output_data)
            self.updateTestCaseList()
            self.saveConfig()
        else:
            raise FileExistsError(f"Test case '{test_case_name}' đã có trong bài tập '{self.name}'.")
    
    def deleteTestCase(self, test_case_name):
        if test_case_name in self.test_cases:
            shutil.rmtree(os.path.join('./deThi', self.name, test_case_name))
            self.test_cases.remove(test_case_name)
            self.updateTestCaseList()
            self.saveConfig()
        else:
            raise FileNotFoundError(f"Test case '{test_case_name}' đã có trong bài tập '{self.name}'.")
        
    def __init__(self, name, input_file = "input.txt", output_file = "output.txt"):
        self.name = name
        self.input_file = input_file
        self.output_file = output_file

        if not os.path.exists(os.path.join('./deThi', name)):
            os.makedirs(os.path.join('./deThi', name))

        self.loadConfig()

problemList = []

def problemExist(problemName):
    for i in problemList:
        if i.name == problemName:
            return True
    return False

def deleteProblem(problemName):
    for i in problemList:
        if i.name == problemName:
            problemList.remove(i)
            break
    shutil.rmtree('./deThi/' + problemName)

def createProblem(problemName):
    if problemExist(problemName):
        if not tools.yesOrNo("Bài tập đã tồn tại. Bạn có muốn thay thế không?"):
            return

    newProblem = problem(problemName)
    problemList.append(newProblem)

    print(f"Bài tập '{problemName}' đã được tạo thành công.")

def updateProblemList():
    global problemList
    problemList = []
    if not os.path.exists('./deThi'):
        os.makedirs('./deThi')
        return

    dirs = [i for i in os.listdir('./deThi') if os.path.isdir(os.path.join('./deThi', i))]
    for dir_name in dirs:
        newProblem = problem(dir_name)
        newProblem.loadConfig()
        problemList.append(newProblem)

def saveAllProblems():
    for i in problemList:
        i.saveConfig()

def addTest(problemName):
    if not problemExist(problemName):
        raise ValueError(f"Bài tập '{problemName}' không tồn tại.")
        
    currentProblem = None
    for i in problemList:
        if i.name == problemName:
            currentProblem = i
            break

    print(f"File input của bài tập '{currentProblem.name}' là: {currentProblem.input_file}")
    print(f"File output của bài tập '{currentProblem.name}' là: {currentProblem.output_file}")

    if tools.yesOrNo("Bạn có muốn thay đổi tên file input/output không?"):
        fi = input("Nhập tên file input mới: ")
        fo = input("Nhập tên file output mới: ")
        currentProblem.setInputFile(fi)
        currentProblem.setOutputFile(fo)
    else:
        fi = currentProblem.input_file
        fo = currentProblem.output_file

    stt = len(currentProblem.test_cases)
    while True:
        dataIn = []
        print("Nhập dữ liệu input (nhập EOF để kết thúc đoạn dữ liệu):")
        while True:
            tmp = input('> ')
            if tmp == 'EOF':
                break
            dataIn.append(tmp)

        dataOut = []
        print("Nhập dữ liệu output (nhập EOF để kết thúc đoạn dữ liệu):")
        while True:
            tmp = input('> ')
            if tmp == 'EOF':
                break
            dataOut.append(tmp)

        currentProblem.addTestCase('test' + str(stt), '\n'.join(dataIn), '\n'.join(dataOut))

        stt += 1

        if tools.yesOrNo("Bạn có muốn thêm testcase không") == False:
            break