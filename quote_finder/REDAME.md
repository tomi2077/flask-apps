Quote Finder App
A simple Flask web application that lets users view and submit their favourite quotes. The app reads from and writes to a local JSON file, serving as a lightweight database.

Features
Display a random quote on each page load.

Add new quotes through a user-friendly form.

Flash messages to indicate successful or invalid submissions.

Simple, minimalistic UI with server-side data handling.

Data is stored in a local quotes.json file.

Project Structure
graphql
Copy
Edit
quote_finder/
│
├── app.py              # Main Flask app
├── quotes.json         # Local JSON database for quotes
├── templates/
│   ├── index.html      # Main page template
│   └── layout.html     # Base layout template
└── venv/               # Python virtual environment (optional)
▶️ Getting Started
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/quote_finder.git
cd quote_finder
Create and activate a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
# On Windows PowerShell
.\venv\Scripts\Activate.ps1
# On macOS/Linux
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install flask
Run the app

bash
Copy
Edit
python app.py
The app will be available at http://127.0.0.1:5000/.

💡 Future Improvements
Store quotes in a real database (e.g., SQLite or PostgreSQL).

Add user authentication to manage personal quotes.

Enable search/filter functionality.

API support for external access to quotes.

🛠️ Tech Stack
Python 3.x

Flask

HTML (Jinja2 templating)

JSON (for data storage)