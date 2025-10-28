# ARKA ENERGY 
Greetings to whoever is reading this.
I am **Garimella Chandrasekhar** an aspiring **Information Science Engineer** for **BMS College of engineering**
The solutions to the tasks given in the form for the role of **Backend Inter**n are labelled as follows 
## TASK 1
**TASK1.py** - Write a Python function that takes a list of user dictionaries (name, age) and returns a list of names of users older than 18.
## TASK 2
**TASK2** - Build a Django project with an app named 'students' having model Student (name, age, email) and API endpoint /api/students/ supporting GET and POST methods. 
## BONUS TASK
Add endpoint /api/students/adults/ returning students aged > 18. 
## Setup Instructions

1. **Clone the Repository**
    ```
    git clone <https://github.com/chandemoniumm/arkaenergytask>
    python3 TASK1.py
    cd TASK2
    ```

2. **(Optional but Recommended) Create and Activate a Virtual Environment**
    ```
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Requirements**
    ```
    pip install django djangorestframework
    ```

4. **Run Database Migrations**
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

5. **Start the Django Development Server**
    ```
    python3 manage.py runserver
    ```
## API Usage

### Add a Student

**POST**  http://127.0.0.1:8000/

*Body (JSON):*
```
{
"name": "Alice Johnson",
"age": 22,
"email": "alice.johnson@example.com"
}
```

### List All Students

**GET** http://127.0.0.1:8000/

### List Adult Students (Bonus)

**GET**  http://127.0.0.1:8000/adults 
Returns all students with `age > 18`.
