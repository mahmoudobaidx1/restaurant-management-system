# 🍽️ Restaurant Management System (CLI)

A lightweight Command-Line Interface (CLI) application built with **Python** and **SQLite3** to manage customer ordering and kitchen workflow in a restaurant setting.

---

## 📌 Overview

This application simulates the interactive process between customers and the restaurant kitchen:
* **Customer Module (`costumer` class):** Displays the restaurant menu from the database, handles item selection, calculates prices, and places orders tied to a specific table number.
* **Kitchen Module (`kitchen` class):** Lists all pending orders for the kitchen staff and allows marking completed orders as prepared (deleting them from the queue).

---

## 🛠️ Features

- 📜 **Interactive Menu Display:** Retrieves and displays current menu items and prices directly from SQLite.
- 📥 **Order Placement:** Validates user order inputs against available menu items and links orders to table numbers.
- 👨‍🍳 **Kitchen Queue Tracking:** Fetches live orders and allows kitchen staff to clear processed orders.
- 💾 **Persistent Storage:** Uses `SQLite3` (`rest.db`) to handle database persistence for both menu items and active orders.

---

## 🗄️ Database Structure

The project relies on an SQLite database named **`rest.db`** with two primary tables:

1. **`menu`**
   - `type` (TEXT): Name/type of the menu item.
   - `price` (REAL/INTEGER): Cost of the item.

2. **`orders`**
   - `type` (TEXT): Ordered item name.
   - `table_num` (TEXT/INTEGER): Table number associated with the order.

---

## 💻 Getting Started

### Prerequisites

* Python 3.x installed on your machine.
* An SQLite database file named `rest.db` in the project root directory with `menu` and `orders` tables initialized.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/restaurant-management-system.git](https://github.com/your-username/restaurant-management-system.git)
   cd restaurant-management-system```
