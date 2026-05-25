"""
╔══════════════════════════════════════════════════════════╗
║        HOTEL MANAGEMENT SYSTEM - Python Project          ║
║        Features: Booking, Customer, Billing, Rooms       ║
╚══════════════════════════════════════════════════════════╝
"""

import os
import datetime

# ─────────────────────────────────────────────
#  DATA STORAGE (in-memory dictionaries)
# ─────────────────────────────────────────────

rooms = {
    101: {"type": "Single",  "price": 1000, "status": "Available"},
    102: {"type": "Single",  "price": 1000, "status": "Available"},
    103: {"type": "Double",  "price": 1800, "status": "Available"},
    104: {"type": "Double",  "price": 1800, "status": "Available"},
    105: {"type": "Suite",   "price": 3500, "status": "Available"},
    106: {"type": "Suite",   "price": 3500, "status": "Available"},
}

customers = {}   # customer_id -> customer info dict
bookings  = {}   # booking_id  -> booking info dict
bills     = {}   # booking_id  -> bill info dict

booking_counter  = 1000
customer_counter = 200


# ─────────────────────────────────────────────
#  UTILITY HELPERS
# ─────────────────────────────────────────────

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def line(char="─", width=56):
    print(char * width)

def header(title):
    clear()
    line("═")
    print(f"  🏨 The Sun-Shine 5* Hotel |  {title}")
    line("═")
    print()

def pause():
    input("\n  Press Enter to continue...")

def today():
    return datetime.date.today()

def date_diff(d1, d2):
    """Return number of nights between two date strings YYYY-MM-DD."""
    fmt = "%Y-%m-%d"
    return (datetime.datetime.strptime(d2, fmt).date() -
            datetime.datetime.strptime(d1, fmt).date()).days


# ─────────────────────────────────────────────
#  1. ROOM MANAGEMENT
# ─────────────────────────────────────────────

def show_all_rooms():
    header("Room Availability")
    print(f"  {'Room No':<10} {'Type':<12} {'Price/Night':<15} {'Status'}")
    line()
    for rno, info in rooms.items():
        status_icon = "✅ Available" if info["status"] == "Available" else "❌ Booked"
        print(f"  {rno:<10} {info['type']:<12} ₹{info['price']:<14} {status_icon}")
    line()
    pause()

def room_menu():
    while True:
        header("Room Management")
        print("  1. View All Rooms")
        print("  2. View Available Rooms Only")
        print("  3. View Booked Rooms Only")
        print("  0. Back to Main Menu")
        line()
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            show_all_rooms()
        elif choice == "2":
            header("Available Rooms")
            found = False
            for rno, info in rooms.items():
                if info["status"] == "Available":
                    print(f"  Room {rno} | {info['type']} | ₹{info['price']}/night")
                    found = True
            if not found:
                print("  No rooms available at the moment.")
            pause()
        elif choice == "3":
            header("Booked Rooms")
            found = False
            for rno, info in rooms.items():
                if info["status"] == "Booked":
                    print(f"  Room {rno} | {info['type']} | ₹{info['price']}/night")
                    found = True
            if not found:
                print("  All rooms are currently available.")
            pause()
        elif choice == "0":
            break
        else:
            print("  ⚠  Invalid choice!")
            pause()


# ─────────────────────────────────────────────
#  2. CUSTOMER MANAGEMENT
# ─────────────────────────────────────────────

def add_customer():
    global customer_counter
    header("Add New Customer")
    name    = input("  Customer Name    : ").strip()
    phone   = input("  Phone Number     : ").strip()
    email   = input("  Email Address    : ").strip()
    address = input("  Address          : ").strip()
    id_proof= input("  ID Proof (Aadhar/PAN): ").strip()

    if not name or not phone:
        print("\n  ⚠  Name and Phone are required!")
        pause()
        return

    customer_counter += 1
    cid = customer_counter
    customers[cid] = {
        "name"    : name,
        "phone"   : phone,
        "email"   : email,
        "address" : address,
        "id_proof": id_proof,
        "added_on": str(today()),
    }
    print(f"\n  ✅ Customer added! Customer ID: C{cid}")
    pause()
    return cid

def view_customers():
    header("All Customers")
    if not customers:
        print("  No customers registered yet.")
    else:
        for cid, info in customers.items():
            print(f"  ID: C{cid} | {info['name']} | 📞 {info['phone']} | {info['email']}")
    pause()

def search_customer():
    header("Search Customer")
    query = input("  Enter Customer ID / Name / Phone: ").strip().lower()
    found = False
    for cid, info in customers.items():
        if (query == str(cid) or
            query in info["name"].lower() or
            query in info["phone"]):
            found = True
            line()
            print(f"  Customer ID  : C{cid}")
            print(f"  Name         : {info['name']}")
            print(f"  Phone        : {info['phone']}")
            print(f"  Email        : {info['email']}")
            print(f"  Address      : {info['address']}")
            print(f"  ID Proof     : {info['id_proof']}")
            print(f"  Registered   : {info['added_on']}")
            line()
    if not found:
        print("  ⚠  No customer found.")
    pause()

def customer_menu():
    while True:
        header("Customer Management")
        print("  1. Add New Customer")
        print("  2. View All Customers")
        print("  3. Search Customer")
        print("  0. Back to Main Menu")
        line()
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            search_customer()
        elif choice == "0":
            break
        else:
            print("  ⚠  Invalid choice!")
            pause()


# ─────────────────────────────────────────────
#  3. BOOKING / CHECK-IN
# ─────────────────────────────────────────────

def make_booking():
    global booking_counter
    header("New Booking / Check-In")

    # ── Customer ──
    cid_input = input("  Enter Customer ID (or press N to add new): ").strip()
    if cid_input.upper() == "N":
        add_customer()
        cid_input = input("  Enter the new Customer ID: ").strip()

    try:
        cid = int(cid_input.replace("C","").replace("c",""))
    except ValueError:
        print("  ⚠  Invalid Customer ID.")
        pause()
        return

    if cid not in customers:
        print("  ⚠  Customer not found. Please register first.")
        pause()
        return

    # ── Room ──
    print("\n  Available Rooms:")
    for rno, info in rooms.items():
        if info["status"] == "Available":
            print(f"    Room {rno} | {info['type']} | ₹{info['price']}/night")

    try:
        rno = int(input("\n  Enter Room Number: ").strip())
    except ValueError:
        print("  ⚠  Invalid room number.")
        pause()
        return

    if rno not in rooms:
        print("  ⚠  Room does not exist.")
        pause()
        return
    if rooms[rno]["status"] == "Booked":
        print("  ⚠  Room is already booked.")
        pause()
        return

    # ── Dates ──
    checkin  = input(f"  Check-In  Date (YYYY-MM-DD) [Today: {today()}]: ").strip()
    checkout = input(f"  Check-Out Date (YYYY-MM-DD): ").strip()

    if not checkin:
        checkin = str(today())

    try:
        nights = date_diff(checkin, checkout)
        if nights <= 0:
            raise ValueError
    except Exception:
        print("  ⚠  Invalid dates. Check-out must be after check-in.")
        pause()
        return

    # ── Confirm ──
    total = rooms[rno]["price"] * nights
    print(f"\n  ── Booking Summary ────────────────────────")
    print(f"  Customer : {customers[cid]['name']}  (C{cid})")
    print(f"  Room     : {rno} ({rooms[rno]['type']})")
    print(f"  Check-In : {checkin}  |  Check-Out: {checkout}")
    print(f"  Nights   : {nights}   |  Rate: ₹{rooms[rno]['price']}/night")
    print(f"  Total    : ₹{total}")
    print(f"  ───────────────────────────────────────────")
    confirm = input("  Confirm Booking? (Y/N): ").strip().upper()

    if confirm != "Y":
        print("  Booking cancelled.")
        pause()
        return

    booking_counter += 1
    bid = booking_counter
    bookings[bid] = {
        "customer_id" : cid,
        "room_no"     : rno,
        "checkin"     : checkin,
        "checkout"    : checkout,
        "nights"      : nights,
        "total_amount": total,
        "status"      : "Checked-In",
        "booked_on"   : str(today()),
    }
    rooms[rno]["status"] = "Booked"

    print(f"\n  ✅ Booking Confirmed! Booking ID: B{bid}")
    pause()

def view_bookings():
    header("All Bookings")
    if not bookings:
        print("  No bookings found.")
    else:
        print(f"  {'BID':<8} {'Customer':<18} {'Room':<6} {'Check-In':<12} {'Check-Out':<12} {'Status'}")
        line()
        for bid, b in bookings.items():
            cname = customers.get(b["customer_id"], {}).get("name", "Unknown")
            print(f"  B{bid:<7} {cname:<18} {b['room_no']:<6} {b['checkin']:<12} {b['checkout']:<12} {b['status']}")
    pause()

def checkout_booking():
    header("Check-Out")
    try:
        bid = int(input("  Enter Booking ID (number only): ").strip())
    except ValueError:
        print("  ⚠  Invalid Booking ID.")
        pause()
        return

    if bid not in bookings:
        print("  ⚠  Booking not found.")
        pause()
        return

    b = bookings[bid]
    if b["status"] == "Checked-Out":
        print("  ℹ  This booking is already checked out.")
        pause()
        return

    # Generate bill
    generate_bill(bid)

    bookings[bid]["status"]     = "Checked-Out"
    rooms[b["room_no"]]["status"] = "Available"
    print(f"\n  ✅ Check-Out successful. Room {b['room_no']} is now available.")
    pause()

def booking_menu():
    while True:
        header("Booking & Check-In/Out")
        print("  1. New Booking / Check-In")
        print("  2. View All Bookings")
        print("  3. Check-Out")
        print("  0. Back to Main Menu")
        line()
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            make_booking()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            checkout_booking()
        elif choice == "0":
            break
        else:
            print("  ⚠  Invalid choice!")
            pause()


# ─────────────────────────────────────────────
#  4. BILLING & INVOICE
# ─────────────────────────────────────────────

def generate_bill(bid):
    if bid not in bookings:
        print("  ⚠  Booking not found.")
        return

    b    = bookings[bid]
    cid  = b["customer_id"]
    cust = customers.get(cid, {})
    room = rooms.get(b["room_no"], {})

    room_charge   = room.get("price", 0) * b["nights"]
    gst           = round(room_charge * 0.12, 2)   # 12% GST
    total         = room_charge + gst

    bills[bid] = {
        "room_charge": room_charge,
        "gst"        : gst,
        "total"      : total,
        "paid"       : False,
    }

    print()
    line("═")
    print("          🧾  HOTEL BILL / INVOICE")
    line("═")
    print(f"  Booking ID   : B{bid}")
    print(f"  Date         : {today()}")
    line()
    print(f"  Guest Name   : {cust.get('name','N/A')}")
    print(f"  Phone        : {cust.get('phone','N/A')}")
    print(f"  Room No      : {b['room_no']}  ({room.get('type','N/A')})")
    print(f"  Check-In     : {b['checkin']}")
    print(f"  Check-Out    : {b['checkout']}")
    print(f"  Nights       : {b['nights']}")
    line()
    print(f"  Room Charges : ₹{room.get('price',0)} x {b['nights']} nights = ₹{room_charge}")
    print(f"  GST (12%)    : ₹{gst}")
    line()
    print(f"  TOTAL AMOUNT : ₹{total}")
    line("═")

    pay = input("\n  Mark as Paid? (Y/N): ").strip().upper()
    if pay == "Y":
        bills[bid]["paid"] = True
        print("  ✅ Payment received. Thank you!")
    else:
        print("  ℹ  Bill saved. Payment pending.")

def billing_menu():
    while True:
        header("Billing & Invoice")
        print("  1. Generate Bill for a Booking")
        print("  2. View Bill Summary")
        print("  0. Back to Main Menu")
        line()
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            try:
                bid = int(input("  Enter Booking ID (number only): ").strip())
            except ValueError:
                print("  ⚠  Invalid ID.")
                pause()
                continue
            generate_bill(bid)
            pause()
        elif choice == "2":
            header("Bill Summary")
            if not bills:
                print("  No bills generated yet.")
            else:
                print(f"  {'BID':<8} {'Room Charge':<15} {'GST':<10} {'Total':<12} {'Status'}")
                line()
                for bid, bill in bills.items():
                    status = "✅ Paid" if bill["paid"] else "⏳ Pending"
                    print(f"  B{bid:<7} ₹{bill['room_charge']:<14} ₹{bill['gst']:<9} ₹{bill['total']:<11} {status}")
            pause()
        elif choice == "0":
            break
        else:
            print("  ⚠  Invalid choice!")
            pause()


# ─────────────────────────────────────────────
#  5. REPORTS / DASHBOARD
# ─────────────────────────────────────────────

def dashboard():
    header("Dashboard & Reports")
    total_rooms     = len(rooms)
    available_rooms = sum(1 for r in rooms.values() if r["status"] == "Available")
    booked_rooms    = total_rooms - available_rooms
    total_customers = len(customers)
    active_bookings = sum(1 for b in bookings.values() if b["status"] == "Checked-In")
    total_revenue   = sum(bill["total"] for bill in bills.values() if bill["paid"])
    pending_revenue = sum(bill["total"] for bill in bills.values() if not bill["paid"])

    print(f"  🏠  Total Rooms       : {total_rooms}")
    print(f"  ✅  Available Rooms   : {available_rooms}")
    print(f"  ❌  Booked Rooms      : {booked_rooms}")
    line()
    print(f"  👥  Total Customers   : {total_customers}")
    print(f"  📋  Active Bookings   : {active_bookings}")
    print(f"  📁  Total Bookings    : {len(bookings)}")
    line()
    print(f"  💰  Revenue Collected : ₹{total_revenue}")
    print(f"  ⏳  Pending Payment   : ₹{pending_revenue}")
    line()
    pause()


# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────

def main():
    while True:
        header("Main Menu")
        print("  1. 🏠  Room Management")
        print("  2. 👤  Customer Management")
        print("  3. 📋  Booking & Check-In/Out")
        print("  4. 🧾  Billing & Invoice")
        print("  5. 📊  Dashboard & Reports")
        print("  0. 🚪  Exit")
        line()
        choice = input("  Enter your choice: ").strip()

        if   choice == "1": room_menu()
        elif choice == "2": customer_menu()
        elif choice == "3": booking_menu()
        elif choice == "4": billing_menu()
        elif choice == "5": dashboard()
        elif choice == "0":
            clear()
            print("\n  Thank you for using Hotel Management System! 🏨\n")
            break
        else:
            print("  ⚠  Invalid choice! Please try again.")
            pause()

if __name__ == "__main__":
    main()