# dyte_sdeIntern_assignment


- This project was made using Django-4.1
- OS Used while creating project: Ubuntu 22.

## Features Of Project:

- Homepage displays logs avilable in database.
- Can add log entries through django admin panel.
- JSON file is generated containing newly added entries through admin panel.
- log_search page allows to search for a specific log entry through the database.

## Demo Of Project: 

https://drive.google.com/file/d/1C-f3GLI_2cTaXu6BLx2ZhDxegLUc1aGQ/view?usp=sharing

## Proof Of Submitted Application For SDE Intern Position At Dyte:

https://drive.google.com/file/d/1V4YphDiZa3WgzDNJXm-5tBSRFRyb8ImA/view?usp=sharing
https://drive.google.com/file/d/1cFwSfCETDk6xE5KE0WO_Hhw1YCrJC0tM/view?usp=sharing

## Commands To Run Project:

- Install Django on your device
- Fork repo
- To run server on port 3000
  
```bash
python3 manage.py runserver 3000

```
- Navigate to log_search page to search for a specific entry

```bash
http://127.0.0.1:3000/log_search
```
- To insert new log_entry, navigate to admin panel
- username: admin, password: admin

```bash
http://127.0.0.1:3000/admin
```

### Tech-Stack:

- Framework: Django-python
- Database: postgresql,django-admin-panel
- To run filters and queries through database and to make it smooth and fast: django-filter
- Additionally for large databases we can implement message queue.To implement a message queue for log ingestion in Django, we can use Celery as a task queue and RabbitMQ as a message broker. 
