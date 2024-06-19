# Django Campaign Management System

This Django project is a basic implementation of a campaign management system where companies can create templates, manage customers, and launch campaigns with personalized messages.

## Features

### Template Management:

- Users can create templates with dynamic placeholders (e.g., `%first_name%`, `%Company’s name%`).
- Templates can be updated, deleted, and viewed.

### Customer Management:

- Customers are stored with basic information such as first name, last name, creation date, and modification date.
- Customers are associated with campaigns to personalize messages.

### Campaign Management:

- Companies can create campaigns using a selected template.
- Campaigns are associated with a list of customers to personalize the message for each customer.

## Setup Instructions

### Prerequisites

- Python (version 3 recommended)
- Django (version 3.2 recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ahmedazhar2299/Campaign_Manager.git
   cd Campaign_Manager

2. **Clone the repository:**

   ```bash
   git clone https://github.com/ahmedazhar2299/Campaign_Manager.git
   cd Campaign_Manager

3. **Setup Virtual Environment:**

   ```bash
   python -m venv env
   source env/scripts/activate

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

5. **Apply database migrations:**

   ```bash
   python manage.py migrate

6. **Start the development server:**

   ```bash
   python manage.py runserver 8000

7. **Access the application at http://localhost:8000/ in your web browser.**
