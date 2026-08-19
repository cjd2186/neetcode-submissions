#Algo
#Keep going until none of the queue students want to take top sandwich
#track when the students circle back around
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        cutOff = len(sandwiches)
        while (students or sandwiches) and i < cutOff:
            if students[0] == sandwiches[0]:
                sandwiches= sandwiches[1:]
                i=0
            else:
                students.append(students[0])
                i+=1
            students= students[1:]
        return len(students)