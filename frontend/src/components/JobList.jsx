import React, { useEffect, useState } from "react";
import { getAllJobs } from "../api";
import { useNavigate } from "react-router-dom";
import './JobList.css';
import { deleteJob } from "../api"; // ajouter deleteJob

const JobList = () => {
  const [jobs, setJobs] = useState([]);
  const navigate = useNavigate();
  const [filter, setFilter] = useState("");


  useEffect(() => {
    fetchJobs();
  }, []);

  const fetchJobs = async () => {
    const data = await getAllJobs();
    setJobs(data);
  };

  const viewMatches = (jobId) => {
    navigate(`/jobdetails/${jobId}`);
  };

  const handleDelete = async (jobId) => {
    if (window.confirm("Are you sure you want to delete this job?")) {
      try {
        await deleteJob(jobId); // API call
        setJobs(jobs.filter(job => job.id !== jobId)); // update state
      } catch (error) {
        console.error("Error deleting job:", error);
      }
    }
  };



  return (
    <div className="job-list-container">
      <h1>Job Offers</h1>
      <input
        type="text"
        placeholder="Filter by Title, Company or Location"
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
        className="filter-input"
      />

      <ul>
        {jobs  
        .filter(
            (job) =>
              job.title.toLowerCase().includes(filter.toLowerCase()) ||
              job.company.toLowerCase().includes(filter.toLowerCase()) ||
              job.location.toLowerCase().includes(filter.toLowerCase())
          )
        .map((job) => (
        <li className="job-item" key={job.id}>
          <strong>{job.title}</strong> @{job.company}  ,<strong style={{marginLeft:"10px"}}><i>{job.location}</i></strong>
          <div className="buttons-container">
            <button className="delete-btn" onClick={() => handleDelete(job.id)}>Delete</button>
            <button onClick={() => viewMatches(job.id)}>View Matches</button>
          </div>
        </li>

        ))}
      </ul>
    </div>
  );
};


export default JobList;
