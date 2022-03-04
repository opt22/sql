use course_management_db; 

select courses.course_name as course,
coalesce(students.student_name, 0) as student_name
from courses
inner JOIN grades
ON grades.grades_course_id = courses.course_id
INNER JOIN students
ON grades.grades_student_id = students.student_id
ORDER BY course DESC;
