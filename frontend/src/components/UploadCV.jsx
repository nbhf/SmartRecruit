import React, { useState, useRef } from "react";
import { uploadCV } from "../api";
import './UploadCV.css';

export default function UploadCV({ setResult, setLoading }) {
  const [file, setFile] = useState(null);
  const fileInputRef = useRef();

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return alert("Please select a file.");

    setLoading(true); // démarre le loading
    try {
      const data = await uploadCV(file);
      console.log("==========Réponse du backend :=================", data);

      if (data && data.analysis) {
        setResult(data.analysis);
      } else {
        console.error("Données d'analyse manquantes dans la réponse");
      }
    } catch (error) {
      console.error("Erreur lors de l'upload:", error);
      alert("Erreur lors de l'analyse du CV");
    } finally {
      setLoading(false); // stoppe le loading
    }
  };

  return (
    <div className="upload-container">
      <h1>Upload New CV</h1>
      <input
        type="file"
        onChange={handleFileChange}
        ref={fileInputRef}
        accept=".pdf"
        style={{ fontSize:"20px"}}
      />
      <button onClick={handleUpload}>Upload CV</button>
    </div>
  );
}
