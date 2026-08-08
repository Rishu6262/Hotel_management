# 🏨 Hotel Management System

The **Hotel Management System** is a comprehensive **command-line based Python application** designed to simplify and manage essential hotel operations through a structured, menu-driven interface.

The system provides functionality for managing **hotel rooms, customer records, room bookings, check-in/check-out, billing, payments, and dashboard reporting**. It simulates a practical hotel workflow, allowing users to perform day-to-day management tasks directly from the terminal.

This project was developed as a **real-world Python practice application** to strengthen programming fundamentals and understand how different modules of a management system work together. It demonstrates practical implementation of **functions, dictionaries, data validation, date handling, CRUD-style operations, state management, and menu-driven programming**.

### ✨ Key Highlights

- 🛏️ **Room Management** – Track room categories, pricing, and availability.
- 👤 **Customer Management** – Register, search, and manage customer information.
- 📅 **Booking Management** – Create and manage customer room bookings.
- 🔑 **Check-In / Check-Out** – Manage the complete customer stay workflow.
- 🧾 **Billing & Payments** – Calculate room charges, GST, and payment status.
- 📊 **Dashboard Reporting** – View important hotel statistics and revenue information.
- 🐍 **Python-Based** – Built using Python and its standard libraries.
- 💻 **Command-Line Interface** – Simple and easy-to-use terminal-based interaction.

Overall, this project provides hands-on experience in building a **practical management system with Python**, while creating a strong foundation for developing future **database-driven, GUI-based, or web-based applications**.
---

## 📌 Project Overview

The **Hotel Management System** is a terminal-based Python application designed to simplify and automate essential hotel operations through a **menu-driven interface**.

The system helps hotel staff efficiently manage the complete hotel workflow, including:

- 🛏️ **Room Availability** – View available and booked rooms.
- 👤 **Customer Records** – Add, view, and search customer information.
- 📅 **Room Bookings** – Create and manage new customer bookings.
- 🔑 **Check-In / Check-Out** – Manage the complete guest stay process.
- 🧾 **Billing & Invoice Generation** – Calculate room charges and generate billing details.
- 💳 **Payment Tracking** – Maintain paid and pending payment records.
- 💰 **Revenue Reporting** – Track collected revenue and pending amounts.
- 📊 **Dashboard Analytics** – Display important hotel statistics in one place.

The project follows a **menu-driven architecture** and demonstrates the practical application of Python concepts such as **functions, dictionaries, loops, conditional statements, data validation, date calculations, CRUD-style operations, and state management**.

Overall, this project provides a practical foundation for understanding how a **real-world hotel management workflow** can be implemented using Python and can later be extended into a **GUI, database-driven, or web-based application**.

# ✨ Features

The Hotel Management System provides a set of practical features designed to simplify day-to-day hotel operations.

---

## 🛏️ Room Management

The Room Management module helps hotel staff monitor and manage room availability efficiently.

### Key Features

- 🏨 View all hotel rooms
- 🟢 View currently available rooms
- 🔴 View booked rooms
- 🏷️ Support multiple room categories:
  - 🛏️ Single Room
  - 🛌 Double Room
  - 👑 Suite Room
- 💰 Display room price per night
- 🔄 Automatically update room availability based on booking and checkout status
- 📊 Quickly identify the current room occupancy status

---

## 👤 Customer Management

The Customer Management module maintains essential guest information and provides quick access to customer records.

### Customer Information

The system stores:

- 🆔 Customer ID
- 👤 Customer Name
- 📱 Phone Number
- 📧 Email Address
- 🏠 Address
- 🪪 ID Proof

### Customer Operations

- ➕ Add new customer
- 📋 View all registered customers
- 🔎 Search customer by:
  - Customer ID
  - Customer Name
  - Phone Number
- 📝 Maintain customer information for booking and billing operations

---
---

## 📅 Booking Management

The Booking Management module handles the complete room reservation workflow, from customer verification to booking confirmation.

### Key Features

- 🆕 Create new room bookings
- 🔐 Verify customer details before booking
- 👤 Register a new customer directly during the booking process
- 🛏️ Select an available room
- 📅 Manage check-in date
- 📅 Manage check-out date
- 🧮 Automatically calculate total stay duration
- 💰 Calculate booking cost based on room price and stay duration
- 📋 Preview complete booking summary
- ✅ Confirm and store the booking

---

## 🔑 Check-Out Management

The Check-Out module manages the completion of a customer's stay and automatically updates the room status.

### Key Features

- 🚪 Process customer check-out
- 🔍 Verify active booking before checkout
- 🧾 Calculate final payable amount
- 🔄 Automatically release the occupied room
- 🟢 Update room status to **Available**
- 📊 Keep booking and room information synchronized

---

## 🧾 Billing & Invoice Management

The Billing module automatically calculates the customer's final bill based on room charges and applicable GST.

### Key Features

- 🧾 Generate invoice for completed bookings
- 🛏️ Calculate room charges based on price per night
- 🌙 Calculate total cost according to stay duration
- 🧮 Automatically calculate GST
- 💰 Calculate final payable amount
- 💳 Maintain payment status
- ✅ **Paid** payment status
- ⏳ **Pending** payment status
- 📋 Provide a clear billing summary to the customer

### 💰 Billing Flow

```text
Room Price / Night
        ↓
Stay Duration
        ↓
Room Charges
        ↓
GST Calculation
        ↓
Total Amount
        ↓
Payment Status
(Paid / Pending)
---

## 📊 Dashboard & Reports

The Dashboard provides a quick overview of the hotel's current operational and financial status.

### Key Statistics

- 🏨 **Total Rooms** – Displays the total number of hotel rooms.
- 🟢 **Available Rooms** – Shows rooms currently available for booking.
- 🔴 **Booked Rooms** – Displays currently occupied/booked rooms.
- 👥 **Total Customers** – Shows the number of registered customers.
- 📅 **Active Bookings** – Displays currently active reservations.
- 📋 **Total Bookings** – Shows the total number of bookings.
- 💰 **Revenue Collected** – Tracks successfully collected payments.
- ⏳ **Pending Payments** – Displays outstanding customer payments.

---

# 🛠️ Technologies Used

## 💻 Programming Language

- 🐍 Python 3

## 📦 Python Modules

- `os` – File and directory-related operations
- `datetime` – Date handling and stay-duration calculations

---

# 🧠 Python Concepts Used

This project demonstrates practical implementation of the following Python concepts:

- 🧩 Functions
- 📚 Dictionaries
- 🗂️ Nested Dictionaries
- 🔀 Conditional Statements
- 🔁 Loops
- ⌨️ User Input Handling
- 📝 String Formatting
- ✅ Data Validation
- 📅 Date & Time Calculations
- 🧱 Modular Programming
- 📋 Menu-Driven Architecture
- 🔄 State Management
- 🗃️ CRUD-Style Operations

---

# 🏗️ Project Architecture

```bash
hotel_management_system/
│
├── hotel_management.py    # Main application
└── README.md              # Project documentation
```

---

# 🚀 Future Improvements

The current command-line application can be extended into a more advanced hotel management platform.

- 🗄️ Database integration using MySQL or PostgreSQL
- 🔐 User authentication and role-based access
- 🖥️ GUI using Tkinter or PyQt
- 🌐 Web application using Flask or FastAPI
- 💳 Online payment integration
- 📧 Automated booking confirmation emails
- 🧾 PDF invoice generation
- 📊 Advanced analytics dashboard
- 📱 Online room reservation system
- ☁️ Cloud deployment

---

# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Python Application Development
- Menu-Driven Programming
- CRUD Operations
- Customer & Booking Management
- Room Availability Management
- Billing & Payment Logic
- Date and Time Handling
- Data Validation
- State Management
- Modular Programming
- Real-World Problem Solving

---

# 📜 Disclaimer

This project has been developed for **educational, learning, and portfolio purposes**.

The system is a simplified simulation of hotel management operations and is not intended to replace a production-level Hotel Management System (HMS) or Property Management System (PMS).

---

# ✅ Conclusion

The **Hotel Management System** demonstrates how Python can be used to develop a practical application for managing essential hotel operations such as **rooms, customers, bookings, check-in/check-out, billing, payments, and reporting**.

By implementing a **menu-driven architecture**, data validation, date calculations, state management, and CRUD-style operations, this project provides hands-on experience in developing a real-world management application.

The project also creates a strong foundation for future development. It can be extended with **database integration, user authentication, GUI interfaces, web APIs, online booking, payment systems, and cloud deployment**.

Overall, this project helped strengthen my understanding of **Python programming, application logic, modular design, data management, and real-world problem solving**.

---

# 👨‍💻 Author

## Rishu Gurjar

🎓 **B.Tech Computer Science Engineering Student**

💻 **Python Developer | Data Analyst | Machine Learning Enthusiast | Deep Learning Learner | Generative AI Enthusiast**

I am passionate about building practical software and AI solutions using **Python, Machine Learning, Deep Learning, NLP, Generative AI, and Data Analytics**. I enjoy developing real-world projects that combine programming, automation, data, and intelligent systems.

### 🚀 Technical Skills

- 🐍 Python
- 🤖 Machine Learning
- 🧠 Deep Learning
- 📊 Data Analysis
- 📚 NLP
- 🌐 Streamlit
- 🗄️ SQL
- 🔗 Git & GitHub

### 📬 Connect With Me

- 💻 **GitHub:** https://github.com/Rishu6262
- 💼 **LinkedIn:** https://www.linkedin.com/in/rishu-gurjar-58072a333/

---

# ⭐ Support

If you found this project useful:

⭐ **Star** the repository  
🍴 **Fork** the project  
💡 **Share** your feedback  

Your support and feedback are greatly appreciated! 🚀
