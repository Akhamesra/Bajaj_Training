CREATE TABLE emp(eid varchar(5), name varchar(20), sal int, primary key (eid));
ALTER TABLE emp add primary key(eid);
INSERT INTO emp values('EO1', 'Ram', 15000);
INSERT INTO emp values('EO2', 'Akshit', 20000);
SELECT * FROM emp;

CREATE TABLE dept (dept_id int, dept_name varchar(20), primary key(dept_id));
ALTER TABLE emp ADD COLUMN dept_id int; 
ALTER TABLE emp add FOREIGN KEY (dept_id) REFERENCES dept (dept_id);

INSERT INTO dept values (1, 'CSE');
INSERT INTO dept values (2, 'IT');

UPDATE emp SET dept_id =1 WHERE eid = 'EO2';
UPDATE emp SET dept_id =2 WHERE eid = 'EO1';

SELECT emp.eid, emp.name, emp.sal, dept.dept_name FROM emp INNER JOIN dept ON emp.dept_id = dept.dept_id;

ALTER TABLE emp DROP CONSTRAINT emp_dept_id_fkey;
ALTER TABLE emp ADD FOREIGN KEY (dept_id) REFERENCES dept (dept_id) ON DELETE CASCADE;


SELECT * FROM emp;
SELECT * FROM emp WHERE name ~* '^A.*s.*' or name ~* '^R';


