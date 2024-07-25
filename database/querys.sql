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
    ('Ruby'),
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

