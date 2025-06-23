from collections import defaultdict

standardGradingType = "Standard"
passFailGradingType = "Pass/Fail"


class Course:
    def __init__(
        self,
        courseId: str,
        courseName: str,
        credit: int,
        type: str = standardGradingType,
    ):
        self.id = courseId
        self.name = courseName
        self.credit = credit
        self.type = type
        self.students: list[str] = []


class Grade:
    def __init__(self):
        self.midterm = 0
        self.final = 0
        self.homeworks = 0

    def setMid(self, grade: int):
        self.midterm = grade

    def setFinal(self, grade: int):
        self.final = grade

    def setHome(self, grade: int):
        self.homeworks = grade

    def sumAll(self):
        return self.midterm + self.final + self.homeworks

    def allGraded(self):
        return self.midterm and self.final and self.homeworks


class Student:
    def __init__(self, id: str):
        self.id = id
        self.courses: dict = defaultdict(list[Course, Grade])


class Management:

    def __init__(self):
        self.courses = defaultdict(Course)
        self.students = defaultdict(Student)

    def createCourses(self, id: str, name: str, credits: int) -> bool:
        if id in self.courses:
            return False

        for course in self.courses.values():
            if name == course.name:
                return False

        self.courses[id] = Course(id, name, credits)
        print(self.courses.keys())

        return True

    def createCourseExt(
        self, id: str, name: str, credits: int, gradingType: str = standardGradingType
    ) -> bool:
        if id in self.courses:
            return False

        for course in self.courses.values():
            if name == course.name:
                return False

        self.courses[id] = Course(id, name, credits, gradingType)
        print(self.courses[id].type)

        return True

    def registerForCourse(self, stuId: str, courseId: str):
        if courseId not in self.courses:
            return False
        if stuId in self.courses[courseId].students:
            return False

        if stuId not in self.students:
            self.students[stuId] = Student(stuId)

        if (
            sum([course[0].credit for course in self.students[stuId].courses.values()])
            + self.courses[courseId].credit
            > 24
        ):
            return False

        self.students[stuId].courses[courseId] = [self.courses[courseId], Grade()]
        self.courses[courseId].students.append(stuId)

        print(self.courses.keys())
        print(self.students.keys())

        return True

    def getPairs(self):
        res = set()
        for _, course in self.courses.items():
            if course.type != standardGradingType:
                continue
            for i in range(len(course.students)):
                for j in range(i + 1, len(course.students)):
                    res.add((course.students[i], course.students[j]))
        return list(res)

    def setComponentGrade(self, stuId: str, cId: str, component: str, grade: int):
        if stuId not in self.courses[cId].students:
            return -1

        course = self.students[stuId].courses[cId]
        if component == "midterm":
            course[1].setMid(grade)
        if component == "final":
            course[1].setFinal(grade)
        if component == "homeworks":
            course[1].setHome(grade)
        print(self.students[stuId].courses[cId][1].midterm)
        return 0

    def getGPA(self, sId: str):
        if not self.students[sId]:
            return -1
        total = 0
        sCount = 0
        pCount = 0
        fCount = 0
        for course in self.students[sId].courses.values():
            if not course[1].allGraded():
                return -1
            if course[0].type == standardGradingType:
                sCount += 1
                total += course[1].sumAll()
            if course[0].type == passFailGradingType:

                if course[1].sumAll() >= 66:
                    pCount += 1
                else:
                    fCount += 1
        return total / sCount, pCount, fCount


m = Management()
m.createCourseExt("C001", "Course1", 3)
m.createCourseExt("C002", "Course2", 4)
m.createCourseExt("C003", "Course3", 5, passFailGradingType)
m.registerForCourse("S1", "C001")
m.registerForCourse("S2", "C003")
m.registerForCourse("S3", "C003")
m.registerForCourse("S2", "C001")
print(m.getPairs())
print(m.setComponentGrade("S2", "C001", "midterm", 30))
print(m.setComponentGrade("S2", "C001", "final", 40))
print(m.setComponentGrade("S2", "C001", "homeworks", 30))
print(m.setComponentGrade("S2", "C003", "midterm", 30))
print(m.setComponentGrade("S2", "C003", "final", 1))
print(m.setComponentGrade("S2", "C003", "homeworks", 1))
print(m.getGPA("S2"))
