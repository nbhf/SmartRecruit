import React, { useState } from "react";
import { addJobOffer } from "../api";
import './AddJobOffer.css';

const AddJobOffer = () => {
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    company: "",
    location: "",
    salary: ""
  });

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await addJobOffer(formData);
    alert("Job offer added successfully!");
    setFormData({ title: "", description: "", company: "", location: "", salary: "" });
  };

  return (
    <div className="form-container">
    <form onSubmit={handleSubmit} className="job-form">
      <h2>Add Job Offer</h2>
      <input type="text" name="title" placeholder="Job Title" value={formData.title} onChange={handleChange} required />
      <textarea name="description" placeholder="Job Description" value={formData.description} onChange={handleChange} required />
      <input type="text" name="company" placeholder="Company" value={formData.company} onChange={handleChange} required />
      <input type="text" name="location" placeholder="Location" value={formData.location} onChange={handleChange} required />
      <input type="text" name="salary" placeholder="Salary" value={formData.salary} onChange={handleChange} /> 
      <button type="submit">Add Job</button>
    </form>
    </div>
  );
};

export default AddJobOffer;
