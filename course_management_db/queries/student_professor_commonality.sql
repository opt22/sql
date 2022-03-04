use course_management_db; 
select grades_student_id, grades_professor_id, count(*)
from grades
GROUP BY grades_student_id, grades_professor_id
ORDER BY count(*) DESC, grades_student_id desc
limit 10
;
