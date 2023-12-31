# Task_NextGrowthLabs
# Django Evaluation

This repository contains my solution for the Django evaluation, which consists of three problem sets. Each problem set is described below along with additional submission details.

## Problem Set 1 - Working with Regex

### Task
Write a regular expression to extract all the numbers with an orange color background from the given JSON-like text.

### Solution
The regex to extract numbers with an orange color background is as follows:

   ```python
   import re

   text = [t.text for t in text_elements]
   s=""
   for i in text:
       s+=i

   numbers = re.findall(r'(?<=color: orange">)(\d+)', s)

   print(numbers)
   ```


## Problem Set 2 - Functional Web App with API

### Task
Create a web application with API endpoints for admin-facing and user-facing functionalities.

### Solution
The web app consists of two components: admin-facing and user-facing.

#### Admin-Facing
- Admin users can add Android apps and assign points to them.

#### User-Facing
- Users can view the apps added by the admin and check their earned points.
- Users can sign up, log in, and upload screenshots to verify completed tasks.

### API Documentation
Please refer to the following API documentation for detailed information about the endpoints: [API Documentation](link_to_api_docs)

## Problem Set 3 - Additional Questions

### Task
Answer the following questions:

A. Write a note about your choice of system to schedule periodic tasks and its scalability.

### Solution
For scheduling periodic tasks in a Python and Django environment, I have chosen Celery as the preferred system. Celery is a distributed task queue framework that allows for efficient and reliable task scheduling and execution.

Reasons for Choosing Celery:
1. Reliability: Celery is known for its reliability and fault-tolerance. It has built-in mechanisms to handle task failures and retries, ensuring that scheduled tasks are executed consistently and reliably.
2. Scalability: Celery is designed to handle large-scale distributed task processing. It supports distributed task queues and can easily scale horizontally by adding more worker nodes as the workload increases.
3. Task Prioritization: Celery provides the flexibility to prioritize tasks based on their importance or urgency. This feature ensures that critical tasks are executed promptly, while less time-sensitive tasks are processed accordingly.
4. Integration with Django: Celery integrates seamlessly with Django, making it an ideal choice for scheduling periodic tasks in Django applications. It leverages Django's database and ORM to store task results and track task progress.
Possible Challenges and Solutions

By adopting Celery for scheduling periodic tasks in Python and Django, you can benefit from its reliability, scalability, and seamless integration with Django, providing a robust foundation for efficient task execution in production environments.

B. Explain the circumstances in which you would use Flask instead of Django, and vice versa.
### Solution
Flask and Django are both popular web frameworks in Python, but they have different strengths and are suitable for different circumstances. Here are some scenarios where you would choose one over the other:

Use Flask:
1. Lightweight and Flexibility: If you have a small-scale project or need a lightweight framework with minimal dependencies, Flask is a good choice. It allows for more flexibility in terms of choosing components and libraries, making it easier to customize and tailor to specific project requirements.
2. Microservices and APIs: Flask is well-suited for building microservices and APIs. Its minimalistic nature and modular design make it efficient for creating lightweight and fast API endpoints.
3. Learning and Simplicity: If you are new to web development or prefer a simpler framework, Flask's minimalistic approach and straightforward design make it easier to grasp and learn.

Use Django:
1. Rapid Development: Django is known for its "batteries included" philosophy, providing a comprehensive set of tools and features out of the box. It excels in rapid development scenarios, where you need to quickly build and deploy complex web applications with built-in functionality for authentication, database management, admin interface, and more.
2. Large-Scale Projects: When working on large-scale projects that require extensive functionality, Django's opinionated structure and conventions help maintain organization and consistency. It provides a robust ORM, authentication system, form handling, and powerful templating engine, reducing the need for manual configuration.
3. Content Management Systems (CMS): If your project involves building a CMS or requires content management capabilities, Django's admin interface provides an intuitive and powerful administration tool to manage content models and user permissions.

The decision should be based on the specific requirements of the project, the development team's familiarity with the frameworks, and the desired trade-offs between simplicity, flexibility, and built-in functionality.

## Deployment

The application has been deployed to [deployment_link].

## Repository Structure

> problem_set_2/ # Solution for Problem Set 2
> README.md # Documentation and submission details
> requirements.txt # Required packages and dependencies


## Installation and Setup

To run the project locally, please follow these steps:

1. Clone the repository:

   git clone [repository_url]
   
3. Install the required dependencies:
   
    pip install -r requirements.txt
   
4. Configure the database settings in `settings.py`.

5. Run the database migrations:

    python manage.py migrate
   
7. Start the development server:

   python manage.py runserver



