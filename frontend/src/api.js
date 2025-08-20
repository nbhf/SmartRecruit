import axios from "axios";

const API_URL="http://localhost:5000/api"

export const uploadCV = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const res = await axios.post(`${API_URL}/cvUpload`, formData);
  console.log("===================Réponse brute Axios :=================", res);
  return res.data;
};


export const addJobOffer = async (jobData) => {
  const response = await axios.post(`${API_URL}/jobs`, jobData);
  return response.data;
};

export const getAllJobs = async () => {
  const res = await axios.get(`${API_URL}/jobs/all`);
  return res.data;
};

export const getJobDetails = async (jobId) => {
  const res = await axios.get(`${API_URL}/jobs/${jobId}`);
  return res.data;
};

export const getJobMatches = async (jobId) => {
  const res = await axios.get(`${API_URL}/jobs/${jobId}/match`);
  return res.data;  // liste de matches triée côté backend
};
