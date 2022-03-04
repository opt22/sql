import mysql
from mysql.connector import Error
import random
import pandas
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
print("START")
#CONNECTOR FUNCTIONALITY
def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database connection successful")
        print(connection)

    except Error as err:
        print(f"Connection Error: '{err}'")

    return connection

def read_query(query):
    connection = create_server_connection(
        "localhost",
        "root",
        "password",
        'course_management_db'
        )
    cursor = connection.cursor() 
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return [cursor.column_names, result]
    except Error as err:
        print(f"Error: '{err}'")

def read_query_extended(query, params):
    connection = create_server_connection(
        "localhost",
        "root",
        "password",
        'course_management_db'
        )

    cursor = connection.cursor() 
    result = None
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def run_query(query):
    connection = create_server_connection(
        "localhost",
        "root",
        "password",
        'course_management_db'
        )
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        #connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Query Error: '{err}'")
    finally:
        connection.close

def run_query_extended(query, params):
    connection = create_server_connection(
        "localhost",
        "root",
        "password",
        'course_management_db'
        )
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        print(query)
        #connection.commit()
        print("Query successful")

    except Error as err:
        print(f"Query Error: '{err}'")
    return 
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#CREATE BASE DB

def create_db_tables():
    create_base = """
    CREATE DATABASE IF NOT EXISTS course_management_db;
    USE course_management_db;
    create table if not exists students(
    student_id int(10) NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
    student_name varchar(40) NOT NULL);

    create table if not exists courses(
    course_id int(10) UNIQUE PRIMARY KEY AUTO_INCREMENT,
    course_name varchar(40) NOT NULL);

    create table if not exists professors(
    professor_id int(10) UNIQUE PRIMARY KEY AUTO_INCREMENT,
    professor_name varchar(40) NOT NULL);

    create table if not exists grades(
    grades_record_id int(10) UNIQUE PRIMARY KEY AUTO_INCREMENT,
    grades_student_id int(10) NOT NULL,
    grades_course_id int(10) NOT NULL ,
    grades_professor_id int(10) NULL ,
    grade int NOT NULL DEFAULT(0));
    show tables;
    """
    add_foreign_keys = """
    use course_management_db;

    alter table grades
    add CONSTRAINT if not exissts grades_student_id
    FOREIGN KEY (grades_student_id)
    REFERENCES students (student_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION;

    alter table grades
    add CONSTRAINT if not exissts grades_student_id
    FOREIGN KEY (grades_student_id)
    REFERENCES students (student_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION;

    alter table grades
    add CONSTRAINT if not exissts grades_course_id
    FOREIGN KEY (grades_course_id)
    REFERENCES courses (course_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION;
    """
    run_query(create_base)
    print("created")
    run_query(add_foreign_keys)
    print("fk assigned")
    pass

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
##POPULATE DB
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#QUERIES

#get_student_list_q = """
#SELECT student_id FROM students;
#"""
#
#get_course_list_q = """
#SELECT course_id FROM courses;
#"""
#
#set_course_choices_q = """
#INSERT INTO grades 
#    (
#    grades_student_id, 
#    grades_course_id
#    )
#    VALUES
#    (
#    "%s", 
#    "%s"
#    )
# """
#
#set_grades_q = """
# """
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#GETTERS
def flatten_list(list):
    flat_list = [item for tup in list for item in tup]
    return flat_list

def get_student_list():
    query = """
    SELECT student_id FROM students;
    """
    student_list_q_results = read_query(query)
    flat_student_list = flatten_list(student_list_q_results)
    print(flat_student_list)
    return flat_student_list
#get_student_list()

def get_course_list():
    query="""
    SELECT course_id FROM courses;
    """
    course_list_q_results = read_query(query)
    flat_course_list = flatten_list(course_list_q_results)
    print(flat_course_list)
    return flat_course_list
#get_course_list()

def get_course_choices(student):
    print(f'STUDENT: {student}')

#get_course_choices()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#SETTERS
def populate_students():
    query = """
    use course_management_db;
    INSERT INTO students
    (
    student_name
    )
    VALUES
    (
    "Student_%s"
    ); 
    commit;
    """
    student_count = list(range(1,201))
    for item in student_count:
        run_query_extended(query, [item])
#populate_students()

def populate_professors():
    query = """
    use course_management_db;
    INSERT INTO professors
    (
    professor_name
    )
    VALUES
    (
    "Professor_%s"
    ); 
    commit;
    """
    professor_count = list(range(1,6))
    for item in professor_count:
        run_query_extended(query, [item])
    pass
#populate_professors()

def populate_courses():
    pass
    query = """
    use course_management_db;
    INSERT INTO courses
    (
    course_name
    )
    VALUES
    (
    "Course_%s"
    ); 
    commit;
    """
    course_count = list(range(1,11))
    for item in course_count:
        run_query_extended(query, [item])
#populate_courses()
#- - - - - - - - - - 
#Assign Courses Populate Grades
def generate_course_choices():
    """generate student course selection
    :returns: list
    """
    c_list = list(range(1,11))
    random.shuffle(c_list)
    student_courses_min = 2
    student_courses_max = 8
    entry_count = list(range(random.randrange(student_courses_min,student_courses_max)))
    choices = []
    for entry in entry_count:
        choice = c_list.pop()
        choices.append(choice)
    print(choices)
    return choices

def assign_courses_to_students():
    student_list = get_student_list()
    query = """
    use course_management_db;
    INSERT INTO grades
    (
    grades_student_id,
    grades_course_id
    )
    VALUES
    (
    %s,
    %s
    ); 
    COMMIT;
    """
    for student in student_list:
        courses = generate_course_choices()
        for course in courses:
            params = (student, course)
            print("something")
            print(params)
            print(query)
            run_query_extended(query, params)
        pass
    pass

#populate_grades()

#def build_grades_query():
#    students = list(range(0,200))
#    professors = list(range(0,5))
#    courses_count = list(range(2,5))
#    pass

#def set_grades():
#    query = """
#    INSERT INTO grades
#    (
#    grades_student_id, 
#    grades_course_id, 
#    grades_professor_id, 
#    grade
#    )
#    VALUES
#    (
#    1001, 
#    1, 
#    3,
#    4
#    );
#    commit;
#    """
#    print(query)
#    run_query(query)

def assign_professors():
    query = """
    UPDATE grades 
    set grades_professor_id = 1
        where grades_course_id between 1 and 2;
    UPDATE grades 
    set grades_professor_id = 2
        where grades_course_id between 3 and 4; 
    UPDATE grades 
    set grades_professor_id = 3
        where grades_course_id between 5 and 6;  
    UPDATE grades 
    set grades_professor_id = 4
        where grades_course_id between 7 and 8;
    UPDATE grades 
    set grades_professor_id = 5
        where grades_course_id between 9 and 10;
    commit;
    """      
    #grade = random.randrange(100)
    run_query(query)
    pass

def assign_grades():
    query = """
    UPDATE grades 
    SET grade = rand()*100;
    commit;
    """      
    #grade = random.randrange(100)
    run_query(query)
    pass
#assign_grade()

def populate_grades():
    assign_courses_to_students();
    assign_grades()
    assign_professors()
    pass
#populate_grades()

#def set_course_choices(student, courses_list, query):
#    """assign grade to each course for given student
#    :returns: assignment status 
#    """
#    student_id = 1
#    #student_courses = generate_course_choices(course_list)
#    student_courses = [2]
#
#    for course_id in student_courses:
#      params = (student_id, course_id)
#      print(params)
#      #print(f'STUDENT: {student_id}')
#      #print(f'Course: {course_id}')
#      run_query_extended(set_course_choices_q, params)
#      pass

#FORMATTING
#def generate_course_choices():
#    """generate student course selection
#    :returns: list
#    """
#    c_list = list(range(1,10))
#    random.shuffle(c_list)
#    student_courses_min = 2
#    student_courses_max = 6
#    entry_count = list(range(random.randrange(student_courses_min,student_courses_max)))
#    choices = []
#    for entry in entry_count:
#        choice = c_list.pop()
#        choices.append(choice)
#    print(choices)
#    return choices

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
##MACROS
#- - - - - - - - - - 
#Delete
def clear_db_data():
    query = """
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
    DELETE from courses;
    select * from courses
    limit 4;
    ALTER TABLE students AUTO_INCREMENT = 0;
    ALTER TABLE courses AUTO_INCREMENT = 0;
    ALTER TABLE professors AUTO_INCREMENT = 0;
    """
    run_query(query)
    pass

def delete_db_tables():
    query = """
    use course_management_db;
    drop table students;
    drop table professors;
    drop table courses;
    drop table grades;
    """
    run_query(query)
    pass

#- - - - - - - - - - 
#Create
def create_db():
    #create/configure database
    create_db_tables()
    pass

#- - - - - - - - - - 
#Populate
def populate_db():
    populate_students()
    populate_courses()
    populate_professors()
    populate_grades()
    pass

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#QUERIES

professor_grade_average = ["professor grade average","""
select avg(grades.grade) grade_avg,
coalesce(professors.professor_name, 0) as professor
from grades
LEFT JOIN professors
ON professors.professor_id = grades.grades_professor_id
GROUP BY professor_name
limit 10;
"""]

top_grades_for_student = ["top grades for student", """
select avg(grades.grade) grade_avg,
coalesce(students.student_name, 0) as student
from grades
inner JOIN students
ON students.student_id = grades.grades_student_id
GROUP BY student_name ORDER BY grade_avg DESC
limit 10;
"""]

group_students_by_courses = ["group students by courses", """
select courses.course_name as course,
coalesce(students.student_name, 0) as student_name
from courses
inner JOIN grades
ON grades.grades_course_id = courses.course_id
INNER JOIN students
ON grades.grades_student_id = students.student_id
ORDER BY course DESC;
"""]

course_grade_avg_summary = ["course grade avg summary", """
select avg(grades.grade) grade_avg,
coalesce(courses.course_name, 0) as course
from grades
right JOIN courses
ON courses.course_id = grades.grades_course_id
GROUP BY course_name ORDER BY grade_avg asc
limit 100;
"""]

student_professor_commonality = [ "student professor commonality", """
select grades_professor_id, grades_student_id, count(*) as common
from grades
GROUP BY grades_professor_id, grades_student_id
ORDER BY common DESC
limit 10;

"""]

#--select grades_student_id, grades_professor_id, count(distinct grades_course_id) as common
#- - - - - - - - - - 
#Format Output
def format_output(ipt):
    #format output, display with pandas 
    q_name, query= ipt
    display_row_limit = 10
    pandas.set_option('display.max_rows', display_row_limit)
        #do not abridge results
    col, results = read_query(query)
    new_list = []
    for result in results:
        result = list(result)
        new_list.append(result)
    columns = col
    df = pandas.DataFrame(new_list, columns=columns)
    print('-----------------------')
    print(q_name)
    print(df)
    print('-----------------------')
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#FUNCTIONS MACRO
#---
#create_db()
#populate_db()
#delete_db_tables()
#clear_db_data()
#---
#QUERY MACRO
#---
#format_output(professor_grade_average)
#format_output(top_grades_for_student)
#format_output(group_students_by_courses)
#format_output(course_grade_avg_summary)
format_output(student_professor_commonality)
#---
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
print("END")

