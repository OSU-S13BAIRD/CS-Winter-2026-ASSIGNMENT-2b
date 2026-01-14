# Author: Sam Baird
# GitHub username: OSU-S13BAIRD
# Date: 01/14/2026
# Description: Implements a Student class for storing student information and a
#              basic_stats function that computes statistical measures from student grades.

import statistics


class Student:
    """
    A class that encapsulates student information including name and grade.
    
    This class maintains private data members for student identification
    and academic performance tracking.
    """

    def __init__(self, name, grade):
        """
        Creates a Student instance with specified name and grade.
        
        Parameters:
            name: The student's name
            grade: The student's numeric grade
        """
        self._name = name
        self._grade = grade

    def get_grade(self):
        """
        Retrieves the student's grade.
        
        Returns:
            The numeric grade value for this student
        """
        return self._grade


def basic_stats(student_list):
    """
    Computes statistical measures for a collection of students.
    
    Calculates the mean, median, and mode of grades from the provided
    list of Student objects.
    
    Parameters:
        student_list: A list containing Student objects
        
    Returns:
        A tuple containing (mean, median, mode) of all student grades
    """
    grade_values = [student.get_grade() for student in student_list]
    
    grade_mean = statistics.mean(grade_values)
    grade_median = statistics.median(grade_values)
    grade_mode = statistics.mode(grade_values)
    
    return (grade_mean, grade_median, grade_mode)
