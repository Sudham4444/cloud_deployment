# Cloud Deployment of Django-Based Survey Application

## Overview
This repository contains a Django-based survey application designed to collect and manage customer feedback. The application dynamically handles various question types like text, big text, radio buttons, and checkboxes.

Deployment Site Link -> [here](https://web-production-2a4f.up.railway.app/)

## Features
- Dynamic question and response handling
- Supports multiple question types
- CSRF protection enabled
- Deployed on Railway.app

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Sudham4444/cloud_deployment.git
   cd cloud_deployment
   
2. Install the required dependencies:
   ```bash
    pip install -r requirements.txt

3. Apply migrations:
   ```bash
    python manage.py migrate

4. Run the server locally:
    ```bash
    python manage.py runserver

## Deployment
  The application is deployed on Railway.app. Ensure to set the environment variables for production before deployment.

## Live Site
  You can access the live application at:  https://web-production-2a4f.up.railway.app/

## Usage
  - Access the application on your local server or the live site URL.
  
  - Navigate through the survey questions and submit your responses.

## Troubleshooting
  - CSRF Errors: If you encounter a 403 Forbidden error related to CSRF verification, ensure that the CSRF token is properly included in your form submissions.

## License
  This project is licensed under the MIT License.

## Contact
  For any questions or issues, please contact at sudhamsingh2412@gmail.com.
