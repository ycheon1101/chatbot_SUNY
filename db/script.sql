CREATE TABLE tb_course_schedule (
	course_code INT,
	course_date INT NOT NULL,
	course_start DATE NOT NULL,
	course_end DATE NOT NULL,
	course_room VARCHAR(10) NOT NULL,
	course_prof VARCHAR(50) NOT NULL,
	course_number INT NOT NULL UNIQUE,
    CONSTRAINT FOREIGN KEY (course_code) REFERENCES tb_course(course_code)
);

CREATE TABLE tb_course (
	course_code INT PRIMARY KEY AUTO_INCREMENT,
	course_name VARCHAR(10) NOT NULL,
	course_fullname VARCHAR(300) NOT NULL,
	course_credit VARCHAR(30),
	course_coordinator VARCHAR(30),
	course_info TEXT,
    course_prereq VARCHAR(300),
	course_outcome TEXT,
	course_requirement TEXT,
	course_sbc VARCHAR(100)
);

CREATE TABLE tb_prof (
	prof_code INT PRIMARY KEY AUTO_INCREMENT,
	prof_name VARCHAR(70) NOT NULL,
    prof_office VARCHAR(50),
    prof_contact VARCHAR(50),
    prof_email VARCHAR(100)
);

CREATE TABLE tb_board (
	board_code INT PRIMARY KEY AUTO_INCREMENT,
	board_title VARCHAR(200) NOT NULL,
	board_content TEXT,
	board_type VARCHAR(30)
);

CREATE TABLE tb_qa (
	qa_code INT PRIMARY KEY AUTO_INCREMENT,
	qa_keyword VARCHAR(50) NOT NULL,
	qa_answer VARCHAR(200)
);

CREATE TABLE tb_qgpt(
	qpgt_code INT PRIMARY KEY AUTO_INCREMENT,
	qpgt_keyword VARCHAR(50) NOT NULL,
	qpgt_question VARCHAR(300)
); 

select * from tb_course;
select * from tb_prof;
