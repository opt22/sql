use course_management_db; 

select avg(grades.grade) grade_avg,
coalesce(students.student_name, 0) as student
from grades
inner JOIN students
ON students.student_id = grades.grades_student_id
GROUP BY student_name ORDER BY grade_avg DESC
limit 10;
