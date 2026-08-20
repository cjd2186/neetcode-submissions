#just check the number of students
#O(n) time, O(n) space
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hungry = len(students)
        studentChoices = Counter(students)

        for s in sandwiches:
            if studentChoices[s] > 0:
                studentChoices[s]-=1
                hungry -=1
            else:
                break
        return hungry