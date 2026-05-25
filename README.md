# Hotel Management System

A comprehensive command-line based Hotel Management System developed in Python to manage hotel operations such as room management, customer registration, bookings, billing, and dashboard reporting.

This project simulates a real-world hotel management workflow and is designed for learning Python programming, modular system design, and management application development.

---

## Project Overview

The Hotel Management System is a terminal-based application that automates core hotel operations.

It helps hotel staff manage:

- Room availability
- Customer records
- New bookings
- Check-in / Check-out
- Billing and invoice generation
- Payment tracking
- Revenue reporting
- Dashboard analytics

The project follows a menu-driven architecture and demonstrates practical implementation of Python concepts in a real-world management system.

---

## Features

### Room Management
- View all hotel rooms
- View available rooms
- View booked rooms
- Room categories:
  - Single Room
  - Double Room
  - Suite Room
- Price per night display
- Real-time room availability updates

---

### Customer Management
- Add new customer
- Store customer details:
  - Name
  - Phone number
  - Email
  - Address
  - ID proof
- View all customers
- Search customer by:
  - Customer ID
  - Name
  - Phone number

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
