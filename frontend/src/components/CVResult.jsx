import React from "react";
import './UploadCV.css'

export default function CVResult({ data }) {
  console.log("=============Données reçues dans CVResult:================", data);
  return (
    <div className="upload-container" style={{textAlign:"left"}}>
      <h2 style={{textAlign:"center"}}>CV Text Extraction Result</h2>
      
      <p><strong>Name:</strong> {data.name}</p>
      <p><strong>Email:</strong> {data.email}</p>
      <p><strong>Phone:</strong> {data.phone}</p>
      
      <p><strong>Education:</strong></p>
      <ul>
        {data.education?.map((edu, index) => (
          <li key={index}>{edu}</li>
        ))}
      </ul>

      <p><strong>Skills:</strong></p>
      <ul>
        {data.skills?.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>

      <p><strong>Experience:</strong></p>
      <ul>
        {data.experience?.map((exp, index) => (
          <li key={index}>{exp}</li>
        ))}
      </ul>
    </div>
  );
}
