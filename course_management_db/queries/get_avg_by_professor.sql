use course_management_db; 

select avg(grades.grade) grade_avg,
coalesce(professors.professor_name, 0) as professor
from grades
LEFT JOIN professors
ON professors.professor_id = grades.grades_professor_id
GROUP BY professor_name
limit 100;
