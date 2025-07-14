# https://leetcode.com/playground/DpnHmSbS

from collections import defaultdict


input1 = [
    ["Data Structures", "Algorithms"],
    ["COBOL", "Networking"],
    ["Algorithms", "COBOL"],
]

input2 = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Graphics", "Networking"],
    ["Networking", "Algorithms"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]

input3 = [
    ["Course_3", "Course_7"],
    ["Course_0", "Course_1"],
    ["Course_1", "Course_2"],
    ["Course_2", "Course_3"],
    ["Course_3", "Course_4"],
    ["Course_4", "Course_5"],
    ["Course_5", "Course_6"],
]


def find_mid_course(rules):
    indegrees = defaultdict(int)
    nextMap = defaultdict(str)
    for rule in rules:
        indegrees[rule[1]] += 1
        nextMap[rule[0]] = rule[1]

    head = None
    for course in nextMap:
        if course not in indegrees:
            head = course

    for i in range((len(nextMap) - 1) // 2):
        head = nextMap[head]
    return head


def find_mid_course_2(rules):

    # find in-degrees
    in_map = {}
    # {cs1:[cs1, cs2]}
    nex_map = {}
    for pre, nex in rules:
        in_map[nex] = in_map.get(nex, 0) + 1
        nex_map[pre] = nex_map.get(pre, [])
        nex_map[pre].append(nex)

    # find heads
    heads = []
    for pre in nex_map:
        if pre not in in_map:
            heads.append(pre)

    # find all paths
    all_paths = []
    find_all_path(heads, nex_map, all_paths, [])

    result = []
    # find all mid cs:
    for path in all_paths:
        mid_course = path[(len(path) - 1) // 2]
        if mid_course not in result:
            result.append(mid_course)

    return result


def find_all_path(courses, next_course_map, all_path, pre_path):
    if not courses:
        all_path.append(pre_path)
        return

    for course in courses:
        find_all_path(
            next_course_map.get(course, []),
            next_course_map,
            all_path,
            pre_path + [course],
        )


print(find_mid_course(input1))
print(find_mid_course_2(input2))
