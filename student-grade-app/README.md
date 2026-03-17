# 🎓 Student Grade Manager App

## 🚀 Project Overview

The **Student Grade Manager App** is a Python-based application designed to manage student records and calculate their grades efficiently.

This project follows a structured software design approach using:

* 📊 Class Diagram (StudentManager, Student, Grade)
* 🔄 Flowchart (Program execution flow)

It demonstrates core concepts of **Object-Oriented Programming (OOP)**, clean architecture, and modular programming.

---

## 🛠 Tech Stack

* Python
* Object-Oriented Programming (OOP)
* Pytest *(for future testing)*

---

## ✨ Features

* ➕ Add new student
* 📋 List all students
* 🔍 Search student by ID
* ❌ Delete student
* 🧮 Calculate student average
* 🏆 Generate grades from marks

---

## 🧠 System Design

### 📊 Class Diagram Overview

The system is built using three main classes:

### 1️⃣ StudentManager

Manages all student records.

**Attributes:**

* `students : List`

**Methods:**

* `addStudent()`
* `listStudent()`
* `searchStudent()`
* `deleteStudent()`

---

### 2️⃣ Student

Represents individual student data.

**Attributes:**

* `student_id : int`
* `name : str`
* `section : str`
* `marks : int`

**Methods:**

* `cal_Average()`
* `cal_Grades()`

---

### 3️⃣ Grade

Handles grade calculation logic.

**Methods:**

* `grade_calculator()`

---

### 🔗 Relationships

* `StudentManager` manages `Student`
* `StudentManager` uses `Grade` for grade calculation

---

## 🔄 Application Flow (Flowchart)

### ▶️ Program Execution Steps

1. Start Program
2. Load student data
3. Display menu options

   * Add Student
   * List Student
   * Search Student
   * Delete Student
4. Perform selected operation
5. Return to menu
6. Exit

---

### 🔽 Flow Summary

```
Start
 ↓
Load Data
 ↓
Show Menu
 ↓
User Choice
 ├── Add Student → Save Record
 ├── List Student → Display Data
 ├── Search Student → Show Details
 ├── Delete Student → Remove Record
 └── Exit 
 ↓
Return to Menu
```

---

## 📁 Project Structure

```
student-grade-manager/
│── main.py
│── manager.py
│── student.py
│── grade.py
|── test_app.py
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/student-grade-manager.git
cd student-grade-manager
```

---

## ▶️ Usage

```bash
python main.py
```

Follow the on-screen menu to perform operations like adding, searching, or deleting students.

---

## 🧪 Example

```
Enter Choice: Add Student
ID: 101
Name: Nigam
Section: A
Marks: 88

✅ Student added successfully!
```

---

## 🔁 Logic Flow Mapping

| Flowchart Step  | Class/Method Used              |
| --------------- | ------------------------------ |
| Add Student     | StudentManager.addStudent()    |
| List Student    | StudentManager.listStudent()   |
| Search Student  | StudentManager.searchStudent() |
| Delete Student  | StudentManager.deleteStudent() |
| Calculate Grade | Grade.grade_calculator()       |

---

## 🔮 Future Improvements

* 🖥 GUI version (Tkinter / Web)
* ✅ Input validation
* 🗄 Export data to CSV/JSON

---

## 🎯 Learning Outcomes

By completing this project, you will learn:

* 📌 Project planning before coding
* 📊 Designing class diagrams
* 🔄 Flowchart-based development
* 🧠 Object-Oriented Programming (OOP)
* 🧹 Writing clean and maintainable Python code

---

## 🤝 Contributing
Contributions are welcome!
Feel free to fork this repo and submit a pull request.
 
---

## 📄 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Nigam**
