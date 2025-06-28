# Mnemos

🎓 *Mnemos* is an open-source intelligent revision platform that combines:

✅ A Markdown-based flashcard system  
✅ A learning schedule powered by the forgetting curve (*SuperMemo 2*)  
✅ AI feedback (GPT) to help you memorize efficiently  
✅ An open science mindset to contribute to memory research

---

## 🚀 Main Features

- Create and edit revision flashcards
- Automatic optimized revision planning
- AI-powered answer analysis and feedback
- React SPA frontend
- Django REST backend with PostgreSQL
- PWA support planned

---

## 📂 Project Structure

mnemos/
├── mnemos_project/ # Django backend
├── mnemos-frontend/ # React frontend
├── venv/ # Python virtual environment (not versioned)
└── README.md


---

## 🛠️ Installation

### Prerequisites

- Python 3.10+
- Node.js 14+
- PostgreSQL
- npm
- (Optional) Docker

---

### Backend

```bash
cd mnemos/mnemos_project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
---

### Frontend

cd mnemos/mnemos-frontend
npm install
npm start

🔒 Security

For now, the API requires you to be authenticated through the Django Admin interface.
Token-based authentication is planned soon.

🌱 Vision

Mnemos is more than an app:

It is a living platform that helps advance the science of learning.
🤝 Contributions

This project is open source under the MIT license.
Contributions are welcome!
Please open an issue or pull request if you’d like to help improve it.

🧑‍💻 Author

Antoine Jeannin
Ordajeannin on GitHub
