CREATE TABLE IF NOT EXISTS job_offers (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    company VARCHAR(255),
    location VARCHAR(100),
    salary VARCHAR(50)
);

INSERT INTO job_offers (title, description, company, location, salary) VALUES
('Backend Developer', 'Develop REST APIs, work with Node.js, Express, and PostgreSQL.', 'TechSolutions', 'Sousse', '3500 TND'),
('Frontend Developer', 'Build responsive UIs with React, TypeScript, and TailwindCSS.', 'Webify', 'Tunis', '3200 TND'),
('DevOps Engineer', 'Manage CI/CD pipelines, Docker, Kubernetes, and cloud infrastructure.', 'CloudOps', 'Sfax', '4000 TND'),
('Cybersecurity Analyst', 'Monitor systems, perform penetration testing, and ensure security compliance.', 'SecureNet', 'Tunis', '3800 TND'),
('AI Engineer', 'Design deep learning models with TensorFlow and PyTorch for NLP and CV.', 'AI Tunisia', 'Ariana', '4200 TND'),
('Business Analyst', 'Bridge IT and business, create reports, and define project requirements.', 'BizTech', 'Sousse', '3100 TND'),
('Project Manager', 'Lead projects using Agile/Scrum, manage teams, and track KPIs.', 'PM Experts', 'Tunis', '4500 TND'),
('Cloud Architect', 'Design cloud-native solutions on AWS, Azure, and GCP.', 'Cloudify', 'Sfax', '5000 TND'),
('Mobile Developer', 'Build mobile apps using Flutter and React Native.', 'AppLab', 'Monastir', '3300 TND'),
('UI/UX Designer', 'Design wireframes, prototypes, and user-friendly interfaces.', 'CreativeStudio', 'Tunis', '2800 TND'),
('QA Engineer', 'Write automated tests with Selenium and ensure software quality.', 'QualityFirst', 'Sousse', '2900 TND'),
('Data Engineer', 'Build ETL pipelines and manage big data with Spark and Hadoop.', 'DataWorks', 'Ariana', '3700 TND'),
('System Administrator', 'Maintain Linux/Windows servers, networks, and backups.', 'InfraCare', 'Tunis', '3000 TND'),
('Full Stack Developer', 'Work on frontend (React) and backend (NestJS, PostgreSQL).', 'CodeFactory', 'Sfax', '3600 TND'),
('AI Research Intern', 'Assist in R&D projects involving computer vision and NLP.', 'DeepLab', 'Tunis', '1200 TND'),
('Marketing Specialist', 'Develop campaigns, manage SEO/SEM, and analyze engagement.', 'MarketPro', 'Nabeul', '2500 TND'),
('Technical Support Engineer', 'Assist clients with troubleshooting software and hardware issues.', 'HelpDesk', 'Sousse', '2200 TND'),
('Blockchain Developer', 'Build smart contracts on Ethereum and work with Solidity.', 'CryptoTech', 'Tunis', '4500 TND'),
('HR Specialist', 'Manage recruitment, onboarding, and employee performance reviews.', 'PeopleFirst', 'Sfax', '2700 TND'),
('Network Engineer', 'Configure routers, switches, and ensure network security.', 'NetSolutions', 'Tunis', '3400 TND');
