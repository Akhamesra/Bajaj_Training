CREATE TABLE teachers ( 
	id bigserial primary key,
	f_name varchar(20),
	l_name varchar(20),
	school varchar(20),
	hiredate date,
	salary numeric
);

INSERT INTO teachers VALUES 
(1,'Akshit','Khamesra','Steward Morris', '2023-01-01', 35000),
(2,'Aryamaan','Pandey','SRM', '2022-12-01', 35000),
(3,'Tanuj','Das','DanBosco', '2022-11-01', 35000),
(4,'Karan','Bengani','DanBosco', '2022-10-01', 35000),
(5,'Abhijit','Pachpande','Vidhya', '2022-09-01', 35000),
(6,'Harsh','Kulkarni','New look', '2022-08-01', 40000),
(7,'Nikhitha','Geddada','Little', '2022-07-01', 25000),
(8,'Shreyansh','Jain','Steward Morris', '2022-07-11', 65000);



SELECT * 
FROM teachers
Where school = 'DanBosco';

SELECT * FROM teachers
WHERE school <> 'DanBosco'; -- Where school is not DanBosco

SELECT l_name,school,hiredate
FROM teachers
ORDER BY hiredate desc;

SELECT f_name, school, hiredate
FROM teachers
ORDER BY school asc;

SELECT f_name, school,hiredate 
FROM teachers
ORDER BY school asc, hiredate desc; -- First order by school and then amoung them order by hiredate


SELECT * 
FROM teachers
WHERE school = 'DanBosco'
ORDER BY hiredate desc;

SELECT f_name, l_name, school, hiredate, salary
FROM teachers
WHERE school ILIKE '%dan%' -- ILIKE is case insensitive
ORDER BY hiredate desc;

-- ASSIGNMENT
--(1)Write a query that list schools in alphabetical order along teachers ordered by last name form A-Z
--(2)Write a query that finds the one teacher whose f_name starts with the letter 'S' and who earns more than 40000
--(3)Rank teachers hired since Jan 1 2022 ordered by highest paid to lowest paid
--(1) SOLUTION - 
SELECT school,f_name,l_name 
FROM teachers
ORDER BY school asc, l_name asc;

--(2) SOLUTION

SELECT f_name, l_name, salary
FROM teachers
WHERE f_name LIKE 'S%' AND salary > 40000;

-(3) 
SELECT f_name, l_name, hiredate, salary
FROM teachers
WHERE hiredate >= '2023-01-01'
ORDER BY salary desc;

----------------------------------------------------------------------------------


CREATE TABLE test_data (
	id serial,
	name text
);
INSERT INTO test_data(name) SELECT 'xyz' FROM generate_series(1,50); -- INSERT any pattern like xyz into the database multiple time 
SELECT * FROM test_data;

----------------------------------------------------------------------------------
-- Exporting and Importing table data to CSV file

CREATE TABLE emp_data(
	name varchar(30),
	address text
);

INSERT INTO emp_data VALUES
('Rahul', 'Pune'),
('Ram', 'Mumbai');

COPY emp_data to '/Users/akshitkhamesra/Desktop/emp.txt' WITH (FORMAT CSV, HEADER, DELIMITER '|'); -- It will export the file to csv
COPY emp_data1 FROM '/Users/akshitkhamesra/Desktop/emp.txt' WITH (FORMAT CSV, HEADER, DELIMITER '|'); -- It will import the file to csv

SELECT * FROM emp_data_copied;
SELECT * FROM emp_data;
SELECT name, address FROM emp_data GROUP BY name, address; -- to show unrepeated data
----------------------------------------------------------------------------------

CREATE TABLE licenses(
	license_id varchar(20),
	fname varchar(20),
	lname varchar(20),
	CONSTRAINT licenses_key PRIMARY KEY (license_id)
);

CREATE TABLE registrations (
	registration_id varchar(20),
	registration_date date,
	license_id varchar(20) REFERENCES licenses (license_id),
	CONSTRAINT registration_key PRIMARY KEY(registration_id, license_id)
);

INSERT INTO licenses (license_id, fname, lname) VALUES
('T229901', 'Lym', 'Malero');

INSERT INTO registrations (registration_id, registration_date, license_id) VALUES
('A203391', '3/17/2017', 'T229901');

-- check constraint  - IT evaluates whether data added to a column meets the expected criteria.

CREATE TABLE check_constraint_demo (
	userid serial,
	user_role varchar(20),
	salary int,
	CONSTRAINT user_id_key PRIMARY KEY (userid),
	CONSTRAINT check_role_in_list CHECK (user_role in ('Admin','Staffs')),
	CONSTRAINT check_salary_not_zero CHECK (salary>0)
);








