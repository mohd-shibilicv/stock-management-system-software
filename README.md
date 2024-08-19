# Stock Management System Documentation

## Overview
This documentation provides a comprehensive guide to setting up, running, and understanding the features of the Stock Management System. The project is built using Django for the backend and React (Vite, JSX) for the frontend, with TailwindCSS for styling, Shadcn UI for components, and Redux Toolkit for state management.

## Table of Contents
1. [Project Features](#project-features)
2. [Project Structure](#project-structure)
3. [Setup Instructions](#setup-instructions)
   - [Backend Setup (Django)](#backend-setup-django)
   - [Frontend Setup (React)](#frontend-setup-react)
4. [Environment Variables](#environment-variables)
5. [User Roles & Permissions](#user-roles--permissions)
6. [Database Configuration](#database-configuration)
7. [Running the Project](#running-the-project)
8. [Key Features](#key-features)
   - [User Management](#user-management)
   - [Product Management](#product-management)
   - [Supplier Management](#supplier-management)
   - [Branch Management](#branch-management)
   - [Quantity Management](#quantity-management)
   - [Reports](#reports)

## Project Features
The Stock Management System is designed to handle product management, supplier management, inventory tracking, and branch management across multiple locations. It supports the following key features:
- **User Roles**: Admin users and branch managers.
- **Product Management**: Tracking product inflows, outflows, and damaged products.
- **Supplier Management**: Recording and managing supplier transactions.
- **Branch Management**: Managing branch details and product requests.
- **Reports**: Generating various reports, such as daily transactions, product details, and inventory levels.

## Project Structure
A brief overview of the directory structure:
```
product_management_system/
│
├── backend/
│   ├── config/                 # Django project settings and urls
│   ├── apps/                   # Django apps (users, products, suppliers, branches, reports)
│   ├── media/                  # Project media files
│   ├── manage.py               # Django management script
│   ├── poetry.lock             # Poetry lock file
│   ├── pyproject.toml          # Poetry configuration file
│   |── .env.example            # Environment variables example
│   └── .gitignore              # Gitignore file
│
├── frontend/
│   ├── public/                 # Static files
│   ├── src/                    # React source files (components, pages, redux, services)
│   ├── tests/                  
│   ├── index.html              # Main HTML file
│   ├── vite.config.js          # Vite configuration
│   ├── package.json            # Frontend dependencies
│   └── .env.example            # Frontend environment variables example
│
└── README.md                   # Project overview
```

## Setup Instructions

### Backend Setup (Django)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NasscriptSoftware/stock-management-system-software.git
   cd product_management_system/backend
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```
   - [Poetry Documentation](https://python-poetry.org/docs/)

3. **Configure the environment variables**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Update the `.env` file with your settings.

4. **Run database migrations**:
   ```bash
   poetry run python manage.py migrate
   ```

5. **Create a superuser** (admin account):
   ```bash
   poetry run python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   poetry run python manage.py runserver
   ```

### Frontend Setup (React)

1. **Navigate to the frontend directory**:
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure the environment variables**:
   - Copy `.env.example` to `.env.local`:
     ```bash
     cp .env.example .env
     ```
   - Update the `.env.local` file with your settings.

4. **Start the development server**:
   ```bash
   npm run dev
   ```

## Environment Variables
Environment variables are required for both the backend and frontend. Refer to the `.env.example` files in the respective directories to configure these variables correctly.

## User Roles & Permissions
- **Admin**: Full control over the system, including user management, branch management, supplier management, and report generation.
- **Branch Manager**: Manage branch-specific operations, request products from the central store, and view branch reports.

## Database Configuration
The default configuration uses PostgreSQL, but for local development, SQLite3 is supported. To switch databases, update the `DATABASES` setting in `settings.py`.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

## Running the Project
After setting up both the backend and frontend, run the following commands simultaneously:
```bash
# Backend
cd backend
poetry run python manage.py runserver

# Frontend
cd frontend
npm run dev
```

## Key Features

### User Management
- Admin users can manage other users, branches, and suppliers.
- Branch managers handle branch-specific tasks and product requests.

### Product Management
- Record and track product inflows, outflows, and damages.

### Supplier Management
- Manage supplier details and track product deliveries from suppliers.

### Branch Management
- Create and manage branch details, including product requests.

### Quantity Management
- Monitor inventory levels with alerts for low and out-of-stock items.

### Reports
- Generate various reports on inventory, product usage, and more.

## Screenshots

1. Login
![Login](/documentation/screenshots/login.png)

2. Store Products
![Store Products](/documentation/screenshots/store_products.png)

3. Product Requests
![Product Requests](/documentation/screenshots/product_requests.png)

4. Store Reports
![Store Reports](/documentation/screenshots/store_reports.png)

5. Branch Inventory
![Branch Inventory](/documentation/screenshots/branch_inventory.png)

6. Branch Profile
![Branch Profile](/documentation/screenshots/branch_profile.png)
