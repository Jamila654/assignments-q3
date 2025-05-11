# Inventory System
Inventory Management System – Project Summary
This project is a terminal-based Inventory Management System built with Python, designed to help manage various types of products in a small retail or warehouse setting. It provides functionality for storing, modifying, and retrieving product information efficiently, while also maintaining persistent data through a JSON file.

Core Mechanism
The system is structured using object-oriented programming with clear separation of concerns. At the heart of the design is an abstract Product class, which provides a base for different product categories: Electronics, Grocery, and Clothing. Each subclass includes its own specific attributes (like brand for Electronics or expiration_date for Grocery), and implements methods for restocking and selling items.

An Inventory class acts as the central controller, managing a list of products. It supports operations such as:

Adding new products (with duplicate ID prevention)

Removing products by ID

Searching by name or type

Selling and restocking inventory

Calculating total inventory value

Automatically removing expired grocery items

To persist data, the system uses a JSON file (inventory.json) that stores the full product list between sessions. On startup, the system loads data from this file, and it saves updates automatically after each operation. This ensures continuity without requiring a database.

Key Features
Product Abstraction: Clean hierarchy with common and type-specific behaviors.

Type-Specific Handling:

Expiration checks for groceries.

Size and material for clothing.

Warranty and brand for electronics.

Data Persistence: All inventory data is stored and retrieved from a file.

Validation: Prevents duplicate product IDs for integrity.

User-Friendly Console UI: Menu-driven flow for managing products interactively.

Ideal Use Case
This system is ideal for educational purposes, basic inventory tracking for small businesses, or as a foundation for more advanced inventory applications (e.g., adding GUI, database integration, or cloud support).

## Installation
```bash
pip install jam-inventory-managemnet-system

run using this commad inventory