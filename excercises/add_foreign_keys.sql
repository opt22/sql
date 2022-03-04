use course_management_db;
show columns from grades;

alter table grades
add CONSTRAINT grades_student_id
    FOREIGN KEY (grades_student_id) 
    REFERENCES students (student_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION;
alter table grades
add CONSTRAINT grades_student_id
    FOREIGN KEY (grades_student_id) 
    REFERENCES students (student_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION;
alter table grades
add CONSTRAINT grades_course_id
    FOREIGN KEY (grades_course_id) 
    REFERENCES courses (course_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION;
