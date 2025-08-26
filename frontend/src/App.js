import { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, useLocation } from "react-router-dom";
import UploadCV from "./components/UploadCV";
import CVResult from "./components/CVResult";
import AddJobForm from "./components/AddJobOffer";
import JobDetails from "./components/JobDetails";
import JobList from "./components/JobList";
import Navbar from "./components/Navbar";

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <Router>
      <Navbar />
      <AppRoutes result={result} setResult={setResult} loading={loading} setLoading={setLoading} />
    </Router>
  );
}


function AppRoutes({ result, setResult, loading, setLoading }) {
  const location = useLocation();

  useEffect(() => {
    if (location.pathname !== "/upload") {
      setResult(null); // reset quand on quitte /upload
    }
  }, [location, setResult]);

  return (
    <Routes>
      <Route
        path="/upload"
        element={
          <div>
            <UploadCV setResult={setResult} setLoading={setLoading} />
            {loading && <p style={{ textAlign: "center" }}>Loading...</p>}
            {!loading && result && <CVResult data={result} />}
          </div>
        }
      />
      <Route path="/addoffer" element={<AddJobForm />} />
      <Route path="/" element={<JobList />} />
      <Route path="/jobdetails/:jobId" element={<JobDetails />} />
    </Routes>
  );
}

export default App;
