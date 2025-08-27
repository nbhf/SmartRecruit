#  My Project AI + Flask + React
This project is a web application with:
- Frontend : React
- Backend : Flask + AI (Gemini + LangChain)
- Data Base : PostgreSQL

## ⚙️ Prérequis
- Python 3.10+
- Node.js 18+
- PostgreSQL locally installed

## 📥 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/nbhf/SmartRecruit.git
cd SmartRecruit
```

### 2. Configurer la base de données
```bash
createdb -U postgres SmartRecruit
psql -U postgres -d SmartRecruit -f db/init.sql
```

### 3. Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate   # (ou venv\Scripts\activate sous Windows)
pip install -r requirements.txt
cp .env.example .env       # puis modifier avec vos clés
python app.py
```

### 4. Frontend
```bash
cd frontend
npm install
npm start
```
