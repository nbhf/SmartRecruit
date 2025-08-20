import React, { useEffect, useState } from "react";
import { getAllJobs } from "../api";
import { useNavigate } from "react-router-dom";
import './JobList.css';

const JobList = () => {
  const [jobs, setJobs] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchJobs() {
      const data = await getAllJobs();
      setJobs(data);
    }
    fetchJobs();
  }, []);

  const viewMatches = (jobId) => {
    navigate(`/jobdetails/${jobId}`);
  };

  return (
    <div>

      <div className="job-list-container">
        <h2>Job Offers</h2>
        <ul>
          {jobs.map((job) => (
            <li className="job-item" key={job.id} style={{ marginBottom: "1rem" }}>
              <strong>{job.title}</strong> at {job.company}
              <button style={{ marginLeft: "1rem" }} onClick={() => viewMatches(job.id)}>
                View Matches
              </button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default JobList;
