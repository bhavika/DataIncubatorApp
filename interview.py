import random
from pprint import pprint


def create_assignment(n, k):
    """
    Generates mappings for each student and k students that they are responsible for grading. 
    :param n: no. of students 
    :param k: no. of students to be graded by each
    :return: dict, grader -> students (list of lists)
    """

    assignments = {}

    # generate some student data
    students = [s for s in range(n)]

    assigned = []

    for s in students:
        groups = []
        temp = students[:]

        # a student can't grade themselves
        temp.remove(s)

        # students who have been assigned graders are no longer candidates
        temp = list(set(temp).difference(set(assigned)))

        try:
            x = random.sample(temp, k)
        except ValueError:
            # sample is larger than population - last batch
            x = temp
        groups.extend(x)
        assigned.extend(x)

        assignments[s] = groups

    return assignments


if __name__ == '__main__':
    import timeit
    print("For 1000 students, execution time (in seconds):", timeit.timeit("create_assignment(1000, 3, 5)",
        setup='from __main__ import create_assignment', number=100))

    print("For 10000 students, execution time (in seconds):", timeit.timeit("create_assignment(10000, 5, 5)",
        setup='from __main__ import create_assignment', number=100))

    weeks = 5

    for i in range(weeks):
        a = create_assignment(1000, 3)

        for k, v in a.items():
            print(k, v)