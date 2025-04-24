import tkinter as tk
from tkinter import messagebox
import mysql.connector

# --The Data Base Configuration -- #
DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Mfraza01!',
    'database': 'TourismAgencyDBMS'
}

# -- Data Base Connection -- #
def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# -- App Window -- #
root = tk.Tk()
root.title("Tourism Agency Booking System")
root.geometry("750x900")

# -- Customer Section -- #
tk.Label(root, text="Customer ID").grid(row=0, column=0)
tk.Label(root, text="First Name").grid(row=1, column=0)
tk.Label(root, text="Last Name").grid(row=2, column=0)
tk.Label(root, text="Email").grid(row=3, column=0)
tk.Label(root, text="Phone").grid(row=4, column=0)
tk.Label(root, text="Address").grid(row=5, column=0)

cust_id = tk.Entry(root)
first_name = tk.Entry(root)
last_name = tk.Entry(root)
email = tk.Entry(root)
phone = tk.Entry(root)
address = tk.Entry(root)

cust_id.grid(row=0, column=1)
first_name.grid(row=1, column=1)
last_name.grid(row=2, column=1)
email.grid(row=3, column=1)
phone.grid(row=4, column=1)
address.grid(row=5, column=1)

def add_customer():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Customer (customer_id, first_name, last_name, email, phone, address) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (cust_id.get(), first_name.get(), last_name.get(), email.get(), phone.get(), address.get())
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Customer added!")
    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", str(err))
    finally:
        conn.close()

def view_customers():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer")
        records = cursor.fetchall()
        output.delete(1.0, tk.END)
        for row in records:
            output.insert(tk.END, str(row) + "\n")
    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", str(err))
    finally:
        conn.close()

def delete_customer():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Customer WHERE customer_id = %s"
        cursor.execute(query, (cust_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Customer deleted!")
    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", str(err))
    finally:
        conn.close()

btn_add_cust = tk.Button(root, text="Add Customer", command=add_customer)
btn_view_cust = tk.Button(root, text="View Customers", command=view_customers)
btn_delete_cust = tk.Button(root, text="Delete Customer", command=delete_customer)
btn_add_cust.grid(row=6, column=0)
btn_view_cust.grid(row=6, column=1)
btn_delete_cust.grid(row=6, column=2)

# -- Booking Section -- #
tk.Label(root, text="Booking ID").grid(row=7, column=0)
tk.Label(root, text="Customer ID").grid(row=8, column=0)
tk.Label(root, text="Package ID").grid(row=9, column=0)
tk.Label(root, text="Booking Date").grid(row=10, column=0)
tk.Label(root, text="People").grid(row=11, column=0)
tk.Label(root, text="Total Cost").grid(row=12, column=0)

booking_id = tk.Entry(root)
b_cust_id = tk.Entry(root)
package_id = tk.Entry(root)
booking_date = tk.Entry(root)
num_people = tk.Entry(root)
total_cost = tk.Entry(root)

booking_id.grid(row=7, column=1)
b_cust_id.grid(row=8, column=1)
package_id.grid(row=9, column=1)
booking_date.grid(row=10, column=1)
num_people.grid(row=11, column=1)
total_cost.grid(row=12, column=1)

def add_booking():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Booking (booking_id, booking_date, customer_id, package_id, number_of_people, total_cost) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (booking_id.get(), booking_date.get(), b_cust_id.get(), package_id.get(), num_people.get(), total_cost.get())
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Booking added!")
    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", str(err))
    finally:
        conn.close()

def view_bookings():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Booking")
        records = cursor.fetchall()
        output.delete(1.0, tk.END)
        for row in records:
            output.insert(tk.END, str(row) + "\n")
    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", str(err))
    finally:
        conn.close()

def delete_booking():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Booking WHERE booking_id = %s"
        cursor.execute(query, (booking_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Booking deleted!")
    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", str(err))
    finally:
        conn.close()

btn_add_booking = tk.Button(root, text="Add Booking", command=add_booking)
btn_view_booking = tk.Button(root, text="View Bookings", command=view_bookings)
btn_delete_booking = tk.Button(root, text="Delete Booking", command=delete_booking)
btn_add_booking.grid(row=13, column=0)
btn_view_booking.grid(row=13, column=1)
btn_delete_booking.grid(row=13, column=2)

# -- Payment Section -- #
tk.Label(root, text="Booking ID").grid(row=14, column=0)
tk.Label(root, text="Payment Date").grid(row=15, column=0)
tk.Label(root, text="Amount").grid(row=16, column=0)
tk.Label(root, text="Mode").grid(row=17, column=0)

pay_booking_id = tk.Entry(root)
payment_date = tk.Entry(root)
payment_amount = tk.Entry(root)
payment_mode = tk.Entry(root)

pay_booking_id.grid(row=14, column=1)
payment_date.grid(row=15, column=1)
payment_amount.grid(row=16, column=1)
payment_mode.grid(row=17, column=1)

def add_payment():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Payment (booking_id, payment_date, payment_amount, payment_mode) VALUES (%s, %s, %s, %s)"
        values = (pay_booking_id.get(), payment_date.get(), payment_amount.get(), payment_mode.get())
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Payment added!")
    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", str(err))
    finally:
        conn.close()

def view_payments():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Payment")
        records = cursor.fetchall()
        output.delete(1.0, tk.END)
        for row in records:
            output.insert(tk.END, str(row) + "\n")
    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", str(err))
    finally:
        conn.close()

def delete_payment():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Payment WHERE booking_id = %s"
        cursor.execute(query, (pay_booking_id.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Payment deleted!")
    except mysql.connector.Error as err:
        messagebox.showerror("DB Error", str(err))
    finally:
        conn.close()

btn_add_payment = tk.Button(root, text="Add Payment", command=add_payment)
btn_view_payment = tk.Button(root, text="View Payments", command=view_payments)
btn_delete_payment = tk.Button(root, text="Delete Payment", command=delete_payment)
btn_add_payment.grid(row=18, column=0)
btn_view_payment.grid(row=18, column=1)
btn_delete_payment.grid(row=18, column=2)

# -- Output -- #
output = tk.Text(root, height=15, width=80)
output.grid(row=19, column=0, columnspan=3, pady=10)

root.mainloop()
