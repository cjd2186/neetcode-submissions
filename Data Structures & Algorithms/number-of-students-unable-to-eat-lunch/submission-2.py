#Algo
#Keep going until none of the queue students want to take top sandwich
#track when the students circle back around

#Time: O(n^2)  --> worst case, goes around the len(sandwiches) time after mismatch
#Space: O(1)
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