use course_management_db;
SET SQL_SAFE_UPDATES = 0;
DELETE from students;
select * from students
limit 4;
DELETE from professors;
select * from professors
limit 4;
DELETE from courses;
select * from courses
limit 4;
ALTER TABLE students AUTO_INCREMENT = 0;
ALTER TABLE courses AUTO_INCREMENT = 0;
ALTER TABLE professors AUTO_INCREMENT = 0;
