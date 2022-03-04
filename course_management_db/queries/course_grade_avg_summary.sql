use course_management_db; 
select avg(grades.grade) grade_avg,
coalesce(courses.course_name, 0) as course
from grades
right JOIN courses
ON courses.course_id = grades.grades_course_id
GROUP BY course_name ORDER BY grade_avg asc
limit 100;

