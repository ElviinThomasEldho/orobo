# Orobo

A Django-based inventory and supply chain management system designed to help businesses manage their materials, transactions, quotations, and delivery operations efficiently.

## Description

Orobo is a comprehensive web application for managing inventory, tracking transactions, generating quotations, and handling delivery operations. The system provides a dashboard for overview, detailed inventory management, transaction tracking, and quotation generation capabilities. It includes a mapping algorithm for optimizing delivery routes and logistics.

## Technologies Used

- **Backend Framework**: Django 4.2.7
- **Database**: SQLite (development)
- **Image Processing**: Pillow 10.1.0
- **Python Version**: Python 3.x
- **Template Engine**: Django Templates
- **Static Files**: Django Static Files
- **Authentication**: Django Authentication System
- **Admin Panel**: Django Admin Interface

## Features

- User authentication (login/signup)
- Dashboard with overview statistics
- Inventory management
- Transaction tracking
- Quotation generation
- Delivery management
- Material management
- Mapping algorithm for route optimization

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd orobo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure

```
orobo/
├── app/                    # Main application
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── forms.py           # Form definitions
│   ├── urls.py            # URL routing
│   └── templates/         # HTML templates
├── orobo/                 # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── mapping algorithm/     # Route optimization algorithms
├── static/                # Static files (CSS, images)
└── manage.py              # Django management script
```

## Usage

1. **Sign Up**: Create a new account
2. **Login**: Access your dashboard
3. **Manage Inventory**: Add, edit, and track materials
4. **Track Transactions**: Monitor all business transactions
5. **Generate Quotations**: Create and manage quotations
6. **Manage Deliveries**: Track and optimize delivery routes

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

