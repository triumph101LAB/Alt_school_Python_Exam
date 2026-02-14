## THE REST API SYSTEM FOR AN ENROLLMENT SYSTEM

# Student Enrollment System API 🎓

A RESTful API built with **FastAPI** for managing a simple school enrollment system. It handles Users (Students/Admins), Courses, and Enrollments using an in-memory dictionary database.

## 📋 Features
* **Users:** Register and retrieve students and administrators.
* **Courses:** Admins can create and delete courses. Everyone can view them.
* **Enrollments:** Students can enroll in courses and deregister. Admins can view enrollments and force deregistration.
* **Security:** Role-based access control (Admin vs. Student).
* **Storage:** In-memory dictionary database (resets on server restart).

---

## 🛠️ Installation & Setup

1.  **Clone or Download** this project folder.
2.  **Open your terminal** in the project root folder.
3.  **Install the dependencies:**
    ```bash
    pip install fastapi uvicorn pytest httpx
    ```

---

## How to Run the API

1.  Start the server using Uvicorn:
    ```terminal
    uvicorn main:app --reload
    or fastapi dev main.py
    ```
2.  Open your browser and visit the interactive documentation:
    * **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    

### Default Test Data
When the server starts, the database is automatically seeded with:
* **Admin User:** ID `1` (Username: `admin_user`)
* **Student User:** ID `2` (Username: `student_user`)

---

##  How to Run the Tests

This project includes a comprehensive test suite using **pytest**. The tests cover users, courses, and complex enrollment logic.

1.  Ensure you are in the **root directory** of the project.
2.  Run the following command:
    ```bash
    pytest
    ```
    *(Note: The `pytest.ini` file handles the python path configuration automatically.)*

### Test Structure
* `test/test_users.py`: Verifies user creation and retrieval.
* `test/test_course.py`: Checks that only Admins can create courses.
* `test/test_enrollment.py`: Validates enrollment rules, including preventing duplicates and ensuring students can only delete their own courses.

---
## 📂 Project Structure
```text
├── main.py               # Application entry point
├── pytest.ini            # Test configuration
├── core/
│   └── db.py             # In-memory database (dictionaries)
├── routers/              # API Endpoints
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
├── schemas/              # Pydantic Models (Data Validation)
├── services/             # Business Logic
└── test/                 # Test Suite
    ├── conftest.py       # Test fixtures
    ├── test_users.py
    ├── test_course.py
    └── test_enrollment.py
