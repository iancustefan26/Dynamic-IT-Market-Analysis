import React, { useState } from 'react';
import StatisticsDisplay from './StatisticsDisplay';
import './index.css';

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
