Grievance Portal

![s1](https://github.com/sumit-mall/grievance_portal/assets/70622737/26ee9775-06c3-4616-a9c7-1d87bd9bd682)

![s2](https://github.com/sumit-mall/grievance_portal/assets/70622737/28d4893c-4107-4ad1-9351-f738ecab84fe)

![s3](https://github.com/sumit-mall/grievance_portal/assets/70622737/00759963-ca4b-4c82-bc8f-881e331a9f35)

![s4](https://github.com/sumit-mall/grievance_portal/assets/70622737/7956cb1b-a199-4139-9e50-25b13c8286f2)

![s5](https://github.com/sumit-mall/grievance_portal/assets/70622737/9686a809-0d89-4f57-8451-2073d19532c3)

![s6](https://github.com/sumit-mall/grievance_portal/assets/70622737/8bbecb36-2798-41d1-8bd1-efd79eac4c97)


This project is a Django-based Grievance Portal designed to handle complaints efficiently. It features a form for adding complaints, a section for tracking complaint status, and a contact form. The portal also includes an admin panel with access to all tables and records, and uses Google OAuth for authentication. This system can be implemented in various settings such as schools, colleges, workplaces, and offices.

Features

- *Add Complaint Form*: Users can submit their grievances through a straightforward form.
- *Track Complaint Status*: Users can check the status of their complaints.
- *Contact Form*: Users can reach out for further assistance or inquiries.
- *Admin Panel*: Administrators can manage all records and tables through a secure admin interface.
- *Google OAuth Authentication*: Secure login using Google accounts.

Requirements

- Python 3.x
- Django 3.x or higher
- Django OAuth Toolkit
- Google API Client Library for Python

## Installation

1. *Clone the Repository*
    ```bash
    git clone https://github.com/sumit-mall/grievance-portal.git
    cd grievance-portal
    ```

2. *Create a Virtual Environment*
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. *Install Dependencies*
    ```bash
    pip install -r requirements.txt
    ```

4. *Setup Google OAuth**
    - Create a project on the [Google Developer Console](https://console.developers.google.com/).
    - Configure OAuth consent screen and create OAuth credentials.
    - Add your project's redirect URI, typically `http://localhost:8000/oauth/complete/google/`.
    - Save the client ID and client secret.

5. *Update Settings*
    - Open `settings.py` and add the following configurations:
    ```python
    SECRET_KEY = 'your_secret_key'
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

    # Google OAuth
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your_google_client_id'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your_google_client_secret'
    ```

6. *Run Migrations*
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. *Create Superuser*
    ```bash
    python manage.py createsuperuser
    ```

8. *Run the Server*
    ```bash
    python manage.py runserver
    ```

Usage

User Functionality

1. **Add Complaint**
    - Navigate to the "Add Complaint" section.
    - Fill in the complaint form and submit.

2. **Track Complaint**
    - Go to the "Track Complaint" section.
    - Enter the complaint ID to view the status.

3. **Contact Form**
    - Use the "Contact Us" form to send queries or requests for further assistance.

### Admin Functionality

1. **Login to Admin Panel**
    - Access the admin panel at `http://localhost:8000/admin/`.
    - Use the superuser credentials created during setup.

2. **Manage Records**
    - View, edit, and delete complaint records.
    - Manage user submissions and contact inquiries.

Contributing

1. Fork the repository.
2. Create a new branch.
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them.
    ```bash
    git commit -m "Description of your changes"
    ```
4. Push to your forked repository.
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.

License

This project is licensed under the MIT License. See the `LICENSE` file for details.

Contact

For any questions or support, please reach out through the contact form on the portal or open an issue on GitHub.
