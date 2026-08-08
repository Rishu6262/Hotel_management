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

### Booking Management
- New room booking
- Customer verification before booking
- Add new customer during booking
- Room selection
- Check-in date management
- Check-out date management
- Automatic stay duration calculation
- Booking summary preview
- Booking confirmation

---

### Check-Out Management
- Check-out customer
- Auto room release after checkout
- Update room status automatically

---

### Billing & Invoice
- Generate invoice for booking
- Automatic room charge calculation
- GST calculation
- Total amount calculation
- Payment status:
  - Paid
  - Pending

---

### Dashboard & Reports
- Total rooms
- Available rooms
- Booked rooms
- Total customers
- Active bookings
- Total bookings
- Revenue collected
- Pending payments

---

## Technologies Used

### Programming Language
- Python 3

### Python Modules
- os
- datetime

---

## Python Concepts Used

This project demonstrates:

- Functions
- Dictionaries
- Nested dictionaries
- Conditional statements
- Loops
- Input handling
- String formatting
- Data validation
- Date calculations
- Modular programming
- Menu-driven architecture
- State management
- CRUD-style operations

---

## Project Architecture

```bash
hotel_management_system/
│
├── hotel_management.py
└── README.md

