import tools
import initContest
import problem

problem.updateProblemList()

while True:
    thaoTac = ['Tạo contest mới',
               'Thêm một bài tập',
               'Thêm test cho một bài tập có sẵn',
               'Xóa bài tập',
               'Xem danh sách bài tập',
               'Tạo stress test',
               'Thoát chương trình']
    
    luaChon = tools.menu(thaoTac)
    if luaChon == 0:
        if initContest.ifExistContest():
            print("Contest hiện tại sẽ bị xóa dữ liệu.")
            if tools.yesOrNo("Bạn có chắc không"):
                initContest.createContest()
        else:
            initContest.createContest()

    elif luaChon == 1:
        name = input("Nhập tên bài tập: ")

        if problem.problemExist(name):
            if tools.yesOrNo("Bài tập này đã tồn tại. Bạn có muốn thay thế không"):
                problem.deleteProblem(name)
                problem.createProblem(name)
        else:
            problem.createProblem(name)

    elif luaChon == 2:
        name = input("Nhập tên bài tập: ")

        if problem.problemExist(name):
            problem.addTest(name)
        else:
            print("Bài tập không tồn tại")
            if tools.yesOrNo("Bạn có muốn tạo bài tập mới không"):
                problem.createProblem(name)
                problem.addTest(name)

    elif luaChon == 3:
        name = input("Nhập tên bài tập: ")

        if problem.problemExist(name):
            problem.deleteProblem(name)
        else:
            print("Bài tập không tồn tại")
    
    elif luaChon == 4:
        problem.updateProblemList()
        if not problem.problemList:
            print("Không có bài tập nào.")
            continue

        print("Danh sách bài tập:")
        for i in problem.problemList:
            print(f"- {i.name}")
    
    elif luaChon == 5:
        name = input("Nhập tên bài tập: ")
        if problem.problemExist(name):
            try:
                problem.createStressTest(name)
            except ValueError as e:
                print(e)
            except FileNotFoundError as e:
                print(e)
        else:
            print("Bài tập không tồn tại")
    
    elif luaChon == 6:
        problem.saveAllProblems()
        print("Đã lưu tất cả bài tập.")
        break