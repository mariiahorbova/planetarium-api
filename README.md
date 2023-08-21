# Planetarium API Service 
Planetarium  API Service is a Django-based RESTful API for managing planetarium shows, themes, reservations and more. It provides endpoints for creating, updating, and retrieving show-related data, as well as user registration and order useful things. 
## Table of Contents  
- [Features](#features)
- [Prerequisites](#prerequisites) 
- [Getting Started](#getting-started) 
- [API right away](#api-right-away)
- [Endpoints](#endpoints) 
- [Customization](#customization)
- [Contributing](#contributing)
- [Licence](#license)
- [Schema](#schema)
- [Screenshots](#screenshots)

## Features:  
- CRUD operations for planetarium shows, domes, themes and reservations. 
- Add images for shows
- Ticket validation based on seat availability.

## Prerequisites

Before you begin, ensure you have the following installed:

-   Docker: [Install Docker](https://docs.docker.com/get-docker/)
-   PostgreSQL: [Install PostgreSQL](https://www.postgresql.org/download/) (Optional - if you want to make changes in db before accessing API)
## Getting Started

Follow these steps to set up and run the Planetarium API project using 
local project and Docker:

1.  Clone this repository to your local machine:
    
    `https://github.com/mariiahorbova/planetarium-api-mate.git`
2. Navigate to the project directory: `cd planetarium-api-mate` 
3. Create `.env` file and define environmental variables by following `.env_example`: 
```
SECRET_KEY = your_secret_key  
DEBUG = your_debug_value  
POSTGRES_NAME=your_db_name  
POSTGRES_USER=your_db_user  
POSTGRES_PASSWORD=your_db_password  
POSTGRES_HOST=your_db_host
```
4.  Build the Docker container using Docker Compose:

    `docker-compose build`
5. Access list of containers:

	`docker ps -a`
6.  Create a superuser for accessing the Django admin panel and API:

    `docker exec -it <container_id here> python manage.py createsuperuser`
7.  Start the Docker container:

    `docker-compose up` 
8.  To stop the container, use:

    `docker-compose down` 

## API right away
If you would like to test API right away, these are the steps:
1. Go to cmd on Windows or terminal on Linux/Mac and pull docker image of the project:

    `docker pull mariiahorbova/planetarium-api`
2. Access list of containers:

	`docker ps -a`
3.  Create a superuser for accessing the Django admin panel and API:
    
    `docker exec -it <container_id here> python manage.py createsuperuser`
4.  Start the Docker container:

    `docker-compose up` 
5.  To stop the containers, use:

    `docker-compose down` 

## Endpoints  
```
	"themes":	 "http://127.0.0.1:8000/api/planetarium/themes/"
	"planetariums":  "http://127.0.0.1:8000/api/planetarium/planetariums/"
	"shows":	 "http://127.0.0.1:8000/api/planetarium/shows/"
	"show_sessions": "http://127.0.0.1:8000/api/planetarium/show_sessions/",  
	"reservations":  "http://127.0.0.1:8000/api/planetarium/reservations/" 

	"registration"	 "http://127.0.0.1:8000/api/user/register/"
	"access token"	 "http://127.0.0.1:8000/api/user/token/"
	"regain token"	 "http://127.0.0.1:8000/api/user/token/refresh/"
	"verify token"	 "http://127.0.0.1:8000/api/user/token/verify/"

	"documentatoin": "http://127.0.0.1:8000/api/schema/" 
			 "http://127.0.0.1:8000/api/schema/swagger-ui/" 
			 "http://127.0.0.1:8000/api/schema/redoc/ "
```

## Customization

You can customize this setup to fit your project's needs:

-   Modify the `Dockerfile` to include additional dependencies or configurations.
-   Adjust the `docker-compose.yml` file to change container names, ports, or other settings.
-   Extend the Django application by adding new models, views, and serializers in the `planetarium/` or `user/` directory.
-   Implement your own API endpoints and business logic in the Django views.

## Contributing

Contributions are welcome! If you find any issues or want to add enhancements, feel free to open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/mariiahorbova/planetarium-api-mate/blob/main/LICENSE) file for details.

## Schema
![schema](https://github.com/mariiahorbova/planetarium-api-mate/assets/44654425/040eade1-05fa-42f7-92ea-a342ad68e46a)


## Screenshots
![image_2023-08-10_21-28-04](https://github.com/mariiahorbova/planetarium-api-mate/assets/44654425/89dc935c-6b68-4b18-815e-876edb78da64)
![image_2023-08-10_21-28-18](https://github.com/mariiahorbova/planetarium-api-mate/assets/44654425/bcc664a8-9285-4083-bee3-58142730f410)
![image_2023-08-10_21-28-55](https://github.com/mariiahorbova/planetarium-api-mate/assets/44654425/fb4de9a7-f882-439b-b39a-108d45b3d288)
![image_2023-08-10_21-30-54](https://github.com/mariiahorbova/planetarium-api-mate/assets/44654425/95a11424-fe87-49a5-be35-d6e3093a3474)
![image_2023-08-10_21-31-47](https://github.com/mariiahorbova/planetarium-api-mate/assets/44654425/d9a3b1e0-056a-445e-a1d8-65cbc7d96f84)
![image_2023-08-10_21-32-47](https://github.com/mariiahorbova/planetarium-api-mate/assets/44654425/417747b7-63cc-4f17-ba81-aa4f85e337ed)
