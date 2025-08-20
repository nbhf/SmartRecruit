import {  Link } from "react-router-dom";

import './Navbar.css'

export default function Navbar() {

return( 

    <nav className="navbar">
        <ul>
          <li><strong><Link to="/">SmartRecruit</Link></strong></li>
          <li><Link to="/">Job Offers List</Link></li>
          <li><Link to="/addoffer">Add New Job Offer</Link></li>
          <li><Link to="/upload">Upload New Cv</Link></li>
        </ul>
      </nav>
    
    );
}