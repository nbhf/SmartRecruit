import React, { useEffect, useState } from "react";
import { getJobDetails, getJobMatches } from "../api";
import "./JobDetails.css";
import { useParams } from "react-router-dom";
import UploadCV from "./UploadCV";

const JobDetails = () => {
  const { jobId } = useParams(); // Récupère jobId depuis l'URL
  console.log("JobId:",jobId);
  const [job, setJob] = useState(null);
  const [matches, setMatches] = useState([]);
  const [loading, setLoading] = useState(true);
  const [result, setResult] = useState(null);
  const [loading1, setLoading1] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const jobData = await getJobDetails(jobId);
        setJob(jobData);

        const matchData = await getJobMatches(jobId);
        matchData.sort((a, b) => b.score - a.score);
        setMatches(matchData);
      } catch (error) {
        console.error("Error fetching job or matches:", error);
      } finally {
        setLoading(false);
      }
    };

    if (jobId) fetchData(); 
  }, [jobId]);

  if (loading && job) return( 
    <div className="job-details-container">
      <h2>{job.title} @ {job.company}</h2>
      <p><strong>Location:</strong> {job.location}</p>
      {job.salary && (<p><strong>Salary:</strong> {job.salary}  </p> )}
      <p><strong>Description:</strong></p>
      <p>{job.description}</p>
        <h3 style={{textAlign:"center"}}>Reloading Candidate Matches...</h3>
        </div>);

  if (!job) return <p>Job not found</p>;

  return (
    <div className="job-details-container">
      <h2>{job.title} @ {job.company}</h2>
      <p><strong>Location:</strong> {job.location}</p>
      {job.salary && (<p><strong>Salary:</strong> {job.salary}  </p> )}
      <p><strong>Description:</strong></p>
      <p>{job.description}</p>


      <h3 className="job-title">Candidate Matches: 
      <div className="upload-inline">
            <UploadCV   setResult={setResult} setLoading={setLoading1}/>
                  {loading1 && <p style={{ textAlign: "center" }}>Uploading...</p>}
                  {!loading1 && result && <p> CV Uploaded Successfully </p> && window.location.reload()} 
      </div>
      </h3>
      {matches.length === 0 ? (
        <p>No candidates matched yet.</p>
      ) : (
        <table className="matches-table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Score</th>
              <th>Skills Match</th>
              <th>Experience Match</th>
              <th>Education Match</th>
              <th>Justification</th>
            </tr>
          </thead>
          <tbody>
            {matches.map((m) => (
              <tr key={m.cv_id}>
                <td>{m.cv_name}</td>
                <td>{m.score}</td>
                <td>{m.skills_match}</td>
                <td>{m.experience_match}</td>
                <td>{m.education_match}</td>
                <td>{m.justification}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default JobDetails;
