# Netflix Clone (Capstone) 🎥

A "boiled down" version of a popular streaming platform, developed as part of the Web Development Capstone Course. This project demonstrates a fully integrated full-stack application featuring a dynamic movie discovery interface and a personalized user experience.

## 👥 Contributors
- **Aayush** - [AayushCode24-7](https://github.com/AayushCode24-7)
- **Aditya** - [adityasyntaxerror](https://github.com/adityasyntaxerror)

## 🚀 Features
- **CRUD Operations:** Create, view, update, and delete items in your personal "Watchlist".
- **Search and Filter:** Dynamic search bar and genre-based filtering to navigate the movie library.
- **Data Validation:** Secure handling of user inputs and API requests to ensure data integrity.
- **Responsive Design:** Mobile-first UI that adapts across all screen sizes.
- **Full Stack Integration:** Seamless connection between the frontend UI and backend database.

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript
* **Backend:** Flask, Json
* **Database:**[]

## 🌐 Architecture & Flow

<h1><b>Project Title: Netflix Clone (Capstone)🎥 </b></h1>

Project Overview: This project is a "boiled down" version of a popular streaming platform, developed as part of the Web Development Capstone Course. Our goal is to demonstrate a fully integrated full-stack application featuring a dynamic movie discovery interface and a personalized user experience.

<h1><b>🚀 Features (Core Requirements)</b></h1>

<h3><b>This project includes:</b></h3>

CRUD Operations: Users can create, view, update, and delete items in their personal "Watchlist".<br>
Search and Filter: A dynamic search bar and genre-based filtering system to navigate the movie library.<br>
Data Validation: Secure handling of user inputs and API requests to ensure data integrity.<br>
Responsive Design: A mobile-first UI that adapts across all screen sizes.<br>
Full Stack Integration: A seamless connection between the frontend UI and backend database.<br>

<h1>🛠️ Tech Stack</h1>
Frontend: HTML5, CSS3, JavaScript

<h1>🌐 Live Demo/Flow Chart </h1>
<ul>
    <li>FrontEnd:</li>
    <li>BackEnd:</li>
</ul>
<h1>Flow Chart</h1><br>

```mermaid 
graph LR
    A[User UI] -- Search Query --> B(Backend API)
    B -- Query Request --> C[(Database)]
    C -- Movie Data --> B
    B -- JSON Response --> A
    A -- CRUD: Add to List --> B
    B -- Save Data --> C
    C -- Confirmation --> B
    B -- Update UI --> A
```
## 📂 Project Structure
```netflix-clone/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── Storage/
|   ├── Thumbnail
├── README.md
└── .gitignore
```
