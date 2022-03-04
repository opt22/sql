--Create DB
CREATE DATABASE IF NOT EXISTS course_management_db;
show databases;
--Create Tables
use course_management_db;
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
grades_professor_id int(10) NOT NULL ,
grade int NOT NULL DEFAULT(0));
show tables;

