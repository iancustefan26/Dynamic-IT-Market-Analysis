CREATE DATABASE jobs;
USE jobs;

CREATE TABLE roles (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE languages (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE tools (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE frameworks (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE cloud_services (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE libraries (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE dbases (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO roles(name)
VALUES
    ("Software Engineer"),
    ("Data Scientist"),
    ("Machine Learning Engineer"),
    ("Cloud Engineer"),
    ("Cybersecurity Specialist");

INSERT INTO languages (name)
VALUES 
    ('C++'),
    ('C'),
    ('Fortran'),
    ('Java'),
    ('Python'),
    ('PHP'),
    ('Ruby'),
    ('Rust'),
    ('C#'),
    ('Go'),
    ('JavaScript'),
    ('R'),
    ('Bash'),
    ('SQL'),
    ('NoSQL');

INSERT INTO tools (name)
VALUES 
    ('Tableau'),
    ('Excel'),
    ('Word'),
    ('SAS'),
    ('PowerPoint'),
    ('SAP'),
    ('Looker'),
    ('SSIS'),
    ('Docker'),
    ('Kubernetes'),
    ('Linux');

INSERT INTO frameworks (name)
VALUES 
    ('Express'),
    ('Node'),
    ('Angular'),
    ('Flask'),
    ('Django'),
    ('Phoenix'),
    ('Vue'),
    ('FastAPI'),
    ('iQuery'),
    ('Ruby on Rails'),
    ('.NET');

INSERT INTO libraries (name)
VALUES 
    ('Spark'),
    ('Hadoop'),
    ('Kafka'),
    ('Airflow'),
    ('PySpark'),
    ('TensorFlow'),
    ('Pandas'),
    ('PyTorch'),
    ('NumPy'),
    ('Spring'),
    ('Matplotlib');

INSERT INTO dbases (name)
VALUES 
    ('SQL Server'),  
    ('MySQL'),
    ('PostgreSQL'),  
    ('Cassandra'),
    ('MongoDB'),     
    ('Firebase'),
    ('Elasticsearch'),
    ('DynamoDB');    

INSERT INTO cloud_services (name)
VALUES 
    ('AWS'),
    ('Azure'),
    ('Google Cloud'),  
    ('Snowflake'),
    ('Databricks'),
    ('Redshift'),
    ('Oracle'),
    ('Redshift'),  
    ('GCP');

USE jobs;

CREATE TABLE role_languages (
    role_id INT NOT NULL,
    language_id INT NOT NULL,
    count INT,
    PRIMARY KEY (role_id, language_id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (language_id) REFERENCES languages(id)
);

CREATE TABLE role_frameworks (
    role_id INT NOT NULL,
    framework_id INT NOT NULL,
    count INT,
    PRIMARY KEY (role_id, framework_id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (framework_id) REFERENCES frameworks(id)
);

CREATE TABLE role_tools (
    role_id INT NOT NULL,
    tool_id INT NOT NULL,
    count INT,
    PRIMARY KEY (role_id, tool_id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (tool_id) REFERENCES tools(id)
);

CREATE TABLE role_cloud_services (
    role_id INT NOT NULL,
    cloud_service_id INT NOT NULL,
    count INT,
    PRIMARY KEY (role_id, cloud_service_id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (cloud_service_id) REFERENCES cloud_services(id)
);

CREATE TABLE role_libraries (
    role_id INT NOT NULL,
    library_id INT NOT NULL,
    count INT,
    PRIMARY KEY (role_id, library_id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (library_id) REFERENCES libraries(id)
);

CREATE TABLE role_databases (
    role_id INT NOT NULL,
    database_id INT NOT NULL,
    count INT,
    PRIMARY KEY (role_id, database_id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (database_id) REFERENCES dbases(id)
);

use jobs;
drop database jobs;

--INSERT INTO role_tools (role_id, tool_id, count)
--VALUES 
  --  (1, 1, 5),  -- role_id 1 refers to 'Software Engineer', tool_id 1 (Tableau) 5 times
  -- (1, 2, 3);  -- role_id 1 refers to 'Software Engineer', tool_id 2 (Excel) 3 times


--To get the number of appearances of each language for a specific job role:

--SELECT r.name as role_name, l.name as language_name, rl.count
--FROM role_languages rl
--JOIN roles r ON rl.role_id = r.id
--JOIN languages l ON rl.language_id = l.id
--WHERE r.id = 1;  -- Assuming you want data for role_id 1


--Retrieve Role Languages

--SELECT r.name AS role_name, l.name AS language_name, rl.count
--FROM role_languages rl
--JOIN roles r ON rl.role_id = r.id
--JOIN languages l ON rl.language_id = l.id;
