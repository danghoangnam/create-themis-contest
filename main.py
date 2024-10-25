import tools
import initContest
import problem

while True:
    thaoTac = ['Tạo contest mới',
               'Thêm một bài tập',
               'Thêm test cho một bài tập có sẵn',
               'Xóa bài tập',
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
        pass

    elif luaChon == 3:
        pass
    
    elif luaChon == 4:
        break