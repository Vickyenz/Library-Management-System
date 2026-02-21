📚 Library Management Web App
A full-stack Library Management System built with Python and Gradio.
This web application allows users to add, remove, and manage books in a library catalog through a clean, mobile-friendly interface.
🔗 Designed for deployment as a live web app using Render.
🚀 Live Demo
👉 Deploy this project on Render to get your public URL.
✨ Features
➕ Add new books to the catalog
🗑 Remove books by ID
🔁 Check books in and out
📖 View complete library catalog
💾 Persistent storage using SQLite database
📱 Mobile-friendly interface
⚡ Fast, lightweight Python backend
🧠 Tech Stack
Python 3
Gradio — Web UI framework
SQLite — Lightweight database
Render — Cloud hosting
Git & GitHub — Version control
📁 Project Structure
library-web-app/ │ ├── app.py                # Main application entry point ├── library/ │   ├── models.py         # OOP data models │   └── service.py        # Business logic + database layer │ ├── requirements.txt      # Python dependencies ├── render.yaml           # Render deployment configuration ├── README.md             # Project documentation └── .gitignore            # Ignored files
⚙️ Installation (Run Locally)
1️⃣ Clone the repository
git clone https://github.com/your-username/library-web-app.git�
cd library-web-app
2️⃣ Create a virtual environment (recommended)
python -m venv venv
Activate it:
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the application
python app.py
Open your browser and go to:
http://localhost:7860�
🌐 Deployment on Render
This project is configured for one-click deployment on Render.
Steps:
Push this repository to GitHub
Create a Render account
Click New → Web Service
Connect your GitHub repository
Deploy
Render will automatically:
✔ Install dependencies
✔ Start the application
✔ Provide a public URL
💡 How It Works
The application follows a simple layered architecture:
📌 Models Layer
Defines the core data structures (Book, LibraryItem).
📌 Service Layer
Handles:
Database operations
Business logic
State management
📌 Presentation Layer
Built using Gradio, providing an interactive web interface.
🧪 Example Use Cases
This project can be used as:
A beginner full-stack portfolio project
A teaching tool for OOP concepts
A prototype for library systems
Practice for deploying Python web apps
A foundation for larger applications
🔮 Possible Future Improvements
🔐 User authentication (login/signup)
☁ Cloud database (PostgreSQL)
📊 Admin dashboard
🔍 Search and filtering
📦 REST API for external clients
🎨 Custom frontend (React/Vue)
📱 Progressive Web App (PWA)
🤝 Contributing
Contributions are welcome!
If you'd like to improve this project:
Fork the repository
Create a new branch
Make your changes
Submit a pull request
📄 License
This project is open source and available under the MIT License.
👨‍💻 Author
Victor Ese
Built as a learning project for full-stack web development and cloud deployment.
⭐ If you found this project helpful, consider giving it a star!# Library-Management-System
