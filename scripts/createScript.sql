/*
Created: 11.05.2021
Modified: 11.05.2021
Model: Logical model
Database: MySQL 8.0
*/

-- Create tables section -------------------------------------------------

-- Table students

CREATE TABLE `students`
(
  `student_id` Varchar(60) NOT NULL,
  `status` Varchar(50) NOT NULL,
  `group_id` Varchar(60) NOT NULL
)
;

CREATE INDEX `IX_student in groups` ON `students` (`group_id`)
;

ALTER TABLE `students` ADD PRIMARY KEY (`student_id`)
;

-- Table groups

CREATE TABLE `groups`
(
  `group_id` Varchar(60) NOT NULL,
  `major` Varchar(100) NOT NULL,
  `form_of_education` Varchar(100) NOT NULL,
  `qualificaion` Varchar(50) NOT NULL
)
;

ALTER TABLE `groups` ADD PRIMARY KEY (`group_id`)
;

-- Table marks

CREATE TABLE `marks`
(
  `mark` Varchar(20) NOT NULL,
  `year` Varchar(9) NOT NULL,
  `semestr` Int NOT NULL,
  `student_id` Varchar(60) NOT NULL,
  `discipline_id` Bigint NOT NULL
)
;

CREATE INDEX `IX_marks of students` ON `marks` (`student_id`)
;

CREATE INDEX `IX_disciplines in marks` ON `marks` (`discipline_id`)
;

-- Table disciplines

CREATE TABLE `disciplines`
(
  `discipline_id` Bigint NOT NULL,
  `name` Varchar(80) NOT NULL
)
;

ALTER TABLE `disciplines` ADD PRIMARY KEY (`discipline_id`)
;

-- Create foreign keys (relationships) section -------------------------------------------------

ALTER TABLE `marks` ADD CONSTRAINT `marks of students` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE `students` ADD CONSTRAINT `student in groups` FOREIGN KEY (`group_id`) REFERENCES `groups` (`group_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE `marks` ADD CONSTRAINT `disciplines in marks` FOREIGN KEY (`discipline_id`) REFERENCES `disciplines` (`discipline_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
;

