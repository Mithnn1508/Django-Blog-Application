# DJANGO-BLOG-APPLICATION

## Setup

## 1 Create a Virtual Environment:

Execute the following command to create a virtual environment:

python -m venv env
Activate the virtual environment:

For Windows:

env\Scripts\activate

For Linux:
source env/bin/activate

## 2 Clone the Repository or Download ZIP:

2 Clone the repository from GitHub or download the ZIP file.
Navigate to the blog application directory using the terminal.

## 3 Install Requirements:

Run the following command to install the required dependencies:

pip install -r requirements.txt

## 4 Run Migrations:

Apply database migrations by executing:

python manage.py migrate

## Project Overview
The project consists of two primary apps:

1 userProfile: This app handles user authentication and profile management.

2 blogApp: Contains models for Posts and Comments.

Authentication is implemented using JWT token-based authentication.


## userProfile APIs
1 Register (POST):

Endpoint: http://127.0.0.1:8000/api/profile/register

2 Login:
Endpoint: http://127.0.0.1:8000/api/profile/login
Output: Upon successful login, it provides an access token and a refresh token. The access token is required to access other APIs.

3 Refresh Token:
Endpoint for token refresh.

## blogApp APIs
1 Fetching Posts and Creating New Posts (GET and POST):

Endpoint: http://127.0.0.1:8000/api/blog/posts/?page=2
Pagination: Utilize the page parameter for pagination.
Output: Provides post details along with likes and like counts.

2 Fetching Comments of a Post (GET and POST):

Endpoint: http://127.0.0.1:8000/api/blog/post/<post_id>/comments

3 Update, Delete, and Get Single Post (GET, PUT, DELETE):

Endpoint: http://127.0.0.1:8000/api/blog/post/<post_id>
Update, Delete, and Get Single Comment (GET, PUT, DELETE):

Endpoint: http://127.0.0.1:8000/api/blog/comment/<comment_id>

5 Like on Posts (POST):

Endpoint: http://127.0.0.1:8000/api/blog/post/<post_id>/like

Output: Returns like counts and an array containing user IDs.

For testing purposes, you can use the provided cURL commands in "test_curl.txt" or directly import the Postman collection file "Django-Blog-Application.postman_collection.json" into Postman.
