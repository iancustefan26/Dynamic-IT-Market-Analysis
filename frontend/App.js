import React, { useState } from 'react';
import StatisticsDisplay from './StatisticsDisplay';
import './index.css';

const data = {
  "Software Engineer": {
    "languages": {
      "C++": 18.84,
      "C": 12.21,
      "Fortran": 0,
      "Java": 17.91,
      "Python": 9.19,
      "PHP": 0,
      "Ruby": 0.35,
      "Rust": 0,
      "C#": 10.35,
      "Go": 4.42,
      "JavaScript": 4.65,
      "R": 0,
      "Bash": 0,
      "SQL": 15.7,
      "NoSQL": 6.4
      },
      "databases": {
      "SQL Server": 0,
      "MySQL": 0,
      "PostgreSQL": 5.88,
      "Cassandra": 82.35,
      "MongoDB": 0,
      "Firebase": 0,
      "Elasticsearch": 11.76,
      "DynamoDB": 0
      },
      "frameworks": {
      "Express": 2.63,
      "Node": 23.68,
      "Angular": 31.58,
      "Flask": 0,
      "Django": 0,
      "Phoenix": 10.53,
      "Vue": 0,
      "FastAPI": 10.53,
      "iQuery": 0,
      "Ruby on Rails": 0,
      ".NET": 21.05
      },
      "tools": {
      "Tableau": 0,
      "Excel": 17.13,
      "Word": 2.21,
      "SAS": 0,
      "PowerPoint": 2.21,
      "SAP": 0,
      "Looker": 0,
      "SSIS": 0,
      "Docker": 11.05,
      "Kubernetes": 15.47,
      "Linux": 51.93
      },
      "libraries": {
      "Spark": 27.66,
      "Hadoop": 19.86,
      "Kafka": 25.53,
      "Airflow": 19.86,
      "PySpark": 0,
      "TensorFlow": 2.84,
      "Pandas": 0,
      "PyTorch": 2.84,
      "NumPy": 0,
      "Spring": 1.42,
      "Matplotlib": 0
      },
      "cloud_services": {
      "AWS": 27.46,
      "Azure": 16.58,
      "Google Cloud": 4.15,
      "Snowflake": 0,
      "Databricks": 2.07,
      "Oracle": 12.44,
      "Redshift": 0,
      "GCP": 37.31
      }
  },
  "Data Scientist" : {
    "languages": {
      "C++": 11.34,
      "C": 6.65,
      "Fortran": 0,
      "Java": 10.92,
      "Python": 22.34,
      "PHP": 0,
      "Ruby": 0.21,
      "Rust": 0,
      "C#": 5.46,
      "Go": 4.69,
      "JavaScript": 2.87,
      "R": 8.96,
      "Bash": 0,
      "SQL": 21.71,
      "NoSQL": 4.83
      },
      "databases": {
      "SQL Server": 0,
      "MySQL": 36,
      "PostgreSQL": 8,
      "Cassandra": 48,
      "MongoDB": 0,
      "Firebase": 0,
      "Elasticsearch": 8,
      "DynamoDB": 0
      },
      "frameworks": {
      "Express": 2.63,
      "Node": 23.68,
      "Angular": 31.58,
      "Flask": 0,
      "Django": 0,
      "Phoenix": 10.53,
      "Vue": 0,
      "FastAPI": 10.53,
      "iQuery": 0,
      "Ruby on Rails": 0,
      ".NET": 21.05
      },
      "tools": {
      "Tableau": 10.43,
      "Excel": 21.54,
      "Word": 0.91,
      "SAS": 14.51,
      "PowerPoint": 7.26,
      "SAP": 0.23,
      "Looker": 0,
      "SSIS": 0,
      "Docker": 9.52,
      "Kubernetes": 16.33,
      "Linux": 19.27
      },
      "libraries": {
      "Spark": 25.91,
      "Hadoop": 9.45,
      "Kafka": 9.76,
      "Airflow": 9.76,
      "PySpark": 8.23,
      "TensorFlow": 7.62,
      "Pandas": 7.32,
      "PyTorch": 14.02,
      "NumPy": 7.32,
      "Spring": 0.61,
      "Matplotlib": 0
      },
      "cloud_services": {
      "AWS": 20.94,
      "Azure": 18.72,
      "Google Cloud": 2.96,
      "Snowflake": 9.11,
      "Databricks": 22.17,
      "Oracle": 5.42,
      "Redshift": 1.23,
      "GCP": 19.46
      }
  },
  "Cloud Engineer" : {
    "languages": {
      "C++": 10.04,
      "C": 4.36,
      "Fortran": 0,
      "Java": 14.68,
      "Python": 27.63,
      "PHP": 0.19,
      "Ruby": 1.41,
      "Rust": 0,
      "C#": 4.46,
      "Go": 5.35,
      "JavaScript": 3.85,
      "R": 6.24,
      "Bash": 0.66,
      "SQL": 17.26,
      "NoSQL": 3.89
      },
      "databases": {
      "SQL Server": 27.59,
      "MySQL": 12.93,
      "PostgreSQL": 3.45,
      "Cassandra": 17.24,
      "MongoDB": 20.69,
      "Firebase": 0,
      "Elasticsearch": 17.24,
      "DynamoDB": 0.86
      },
      "frameworks": {
      "Express": 5.68,
      "Node": 38.64,
      "Angular": 23.86,
      "Flask": 0,
      "Django": 0,
      "Phoenix": 4.55,
      "Vue": 4.55,
      "FastAPI": 4.55,
      "iQuery": 0,
      "Ruby on Rails": 0,
      ".NET": 18.18
      },
      "tools": {
      "Tableau": 7.33,
      "Excel": 17.57,
      "Word": 0.55,
      "SAS": 7.33,
      "PowerPoint": 3.87,
      "SAP": 0.14,
      "Looker": 0,
      "SSIS": 2.07,
      "Docker": 17.15,
      "Kubernetes": 25.31,
      "Linux": 18.67
      },
      "libraries": {
      "Spark": 19.16,
      "Hadoop": 7.13,
      "Kafka": 12.31,
      "Airflow": 8.39,
      "PySpark": 5.87,
      "TensorFlow": 14.97,
      "Pandas": 7.27,
      "PyTorch": 17.9,
      "NumPy": 6.15,
      "Spring": 0.28,
      "Matplotlib": 0.56
      },
      "cloud_services": {
      "AWS": 33.11,
      "Azure": 25.79,
      "Google Cloud": 5.45,
      "Snowflake": 6.21,
      "Databricks": 7.06,
      "Oracle": 2.72,
      "Redshift": 0.6,
      "GCP": 19.06
      }
  },
  "Machine Learning Engineer" : {
    "languages": {
      "C++": 11.11,
      "C": 5.48,
      "Fortran": 0,
      "Java": 13.82,
      "Python": 28.06,
      "PHP": 0,
      "Ruby": 0.15,
      "Rust": 0,
      "C#": 4.3,
      "Go": 5.12,
      "JavaScript": 2.3,
      "R": 7.99,
      "Bash": 0,
      "SQL": 18.13,
      "NoSQL": 3.53
      },
      "databases": {
      "SQL Server": 0,
      "MySQL": 36,
      "PostgreSQL": 8,
      "Cassandra": 48,
      "MongoDB": 0,
      "Firebase": 0,
      "Elasticsearch": 8,
      "DynamoDB": 0
      },
      "frameworks": {
      "Express": 2.17,
      "Node": 28.26,
      "Angular": 34.78,
      "Flask": 0,
      "Django": 0,
      "Phoenix": 8.7,
      "Vue": 0,
      "FastAPI": 8.7,
      "iQuery": 0,
      "Ruby on Rails": 0,
      ".NET": 17.39
      },
      "tools": {
      "Tableau": 8.65,
      "Excel": 21.97,
      "Word": 0.69,
      "SAS": 11.07,
      "PowerPoint": 5.54,
      "SAP": 0.17,
      "Looker": 0,
      "SSIS": 0,
      "Docker": 13.84,
      "Kubernetes": 19.55,
      "Linux": 18.51
      },
      "libraries": {
      "Spark": 21.16,
      "Hadoop": 4.72,
      "Kafka": 8.09,
      "Airflow": 7.01,
      "PySpark": 6.87,
      "TensorFlow": 16.44,
      "Pandas": 8.09,
      "PyTorch": 19.81,
      "NumPy": 7.01,
      "Spring": 0.27,
      "Matplotlib": 0.54
      },
      "cloud_services": {
      "AWS": 25.57,
      "Azure": 21.77,
      "Google Cloud": 6.85,
      "Snowflake": 8.68,
      "Databricks": 14.61,
      "Oracle": 3.35,
      "Redshift": 1.07,
      "GCP": 18.11
      }
  },
  "Cybersecurity Specialist" : {
    "languages": {
      "C++": 10.15,
      "C": 4.35,
      "Fortran": 0,
      "Java": 14.65,
      "Python": 27.56,
      "PHP": 0.19,
      "Ruby": 1.4,
      "Rust": 0,
      "C#": 4.45,
      "Go": 5.43,
      "JavaScript": 3.84,
      "R": 6.22,
      "Bash": 0.66,
      "SQL": 17.22,
      "NoSQL": 3.88
      },
      "databases": {
      "SQL Server": 30,
      "MySQL": 12.5,
      "PostgreSQL": 3.33,
      "Cassandra": 16.67,
      "MongoDB": 20,
      "Firebase": 0,
      "Elasticsearch": 16.67,
      "DynamoDB": 0.83
      },
      "frameworks": {
      "Express": 6.74,
      "Node": 38.2,
      "Angular": 23.6,
      "Flask": 0,
      "Django": 0,
      "Phoenix": 4.49,
      "Vue": 4.49,
      "FastAPI": 4.49,
      "iQuery": 0,
      "Ruby on Rails": 0,
      ".NET": 17.98
      },
      "tools": {
      "Tableau": 7.13,
      "Excel": 18.84,
      "Word": 0.54,
      "SAS": 7.13,
      "PowerPoint": 3.77,
      "SAP": 0.13,
      "Looker": 0,
      "SSIS": 2.02,
      "Docker": 16.69,
      "Kubernetes": 24.63,
      "Linux": 19.11
      },
      "libraries": {
      "Spark": 19.16,
      "Hadoop": 7.13,
      "Kafka": 12.31,
      "Airflow": 8.39,
      "PySpark": 5.87,
      "TensorFlow": 14.97,
      "Pandas": 7.27,
      "PyTorch": 17.9,
      "NumPy": 6.15,
      "Spring": 0.28,
      "Matplotlib": 0.56
      },
      "cloud_services": {
      "AWS": 33.44,
      "Azure": 26.27,
      "Google Cloud": 5.34,
      "Snowflake": 6.09,
      "Databricks": 6.92,
      "Oracle": 2.67,
      "Redshift": 0.58,
      "GCP": 18.68
      }
  },
};

const App = () => {
  const [selectedSkill, setSelectedSkill] = useState('languages');
  const [selectedJob, setSelectedJob] = useState('Software Engineer');

  return (
    <div className="app-container">
      <h1>Skills Statistics</h1>
      <JobSelector selectedJob={selectedJob} setSelectedJob={setSelectedJob} />
      <SkillSelector selectedSkill={selectedSkill} setSelectedSkill={setSelectedSkill} />
      <StatisticsDisplay selectedSkill={selectedSkill} selectedJob={selectedJob} />
    </div>
  );
};

const JobSelector = ({ selectedJob, setSelectedJob }) => {
  const jobs = ['Software Engineer', 'Data Scientist', 'Machine Learning Engineer', 'Cloud Engineer', 'Cybersecurity Specialist', 'All'];

  return (
    <div className="job-selector">
      {jobs.map(job => (
        <button
          key={job}
          onClick={() => setSelectedJob(job)}
          className={selectedJob === job ? 'selected' : ''}
        >
          {job}
        </button>
      ))}
    </div>
  );
};

const SkillSelector = ({ selectedSkill, setSelectedSkill }) => {
  const skills = ['languages', 'databases', 'frameworks', 'tools', 'libraries', 'cloud_services'];

  return (
    <div className="skill-selector">
      {skills.map(skill => (
        <button
          key={skill}
          onClick={() => setSelectedSkill(skill)}
          className={selectedSkill === skill ? 'selected' : ''}
        >
          {skill}
        </button>
      ))}
    </div>
  );
};

export default App;
