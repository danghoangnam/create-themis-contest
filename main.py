import tools
import initContest

while True:
    thaoTac = ['Tạo contest mới',
               'Thêm một bài tập',
               'Thêm test cho một bài tập có sẵn',
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
        pass

    elif luaChon == 2:
        pass
    
    elif luaChon == 3:
        if tools.yesOrNo("Bạn có chắc không"):
            break