student_info=[{"name": '1', "age": '1', "score": '1'},{"name": '2', "age": '2', "score": '2'}]
def mod_student_info(student_info):
    mod_name = input("请输入修改的学生姓名：")
    for info in student_info:
        if mod_name == info.get("name"):
            a = int(input("请输入年龄："))
            s = int(input("请输入成绩："))
            info = {"name": mod_name, "age": a, "score": s}
            return info
    raise IndexError("学生信息不匹配,没有找到%s" % mod_name)


info=mod_student_info(student_info)
print(student_info)
print(info)