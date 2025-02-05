CRUD application for incident management. 


Incident fields:
- title
- latitude
- longitude
- created_at
- status("active" or "closed")

Deployment:
- git clone https://github.com/djangorepos/incidents.git
- cd crud
- docker-compose up --build -d
- docker ps (to see all containers)
- docker exec -it  </your container web/> python manage.py makemigrations
- docker exec -it  </your container web/> python manage.py migrate
- docker exec -it  </your container web/> python manage.py collectstatic --noinput
- docker-compose up