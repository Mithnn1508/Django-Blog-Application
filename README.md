# BLOG APPLICATION USING DJANGO REST FRAMEWORK 

### SETUP ###
    -  CREATE VIRTUAL ENVIROMENT USING - 
            python -m venv env
            activate virtualenv- Scripts/activate (for windows)
                                 source bin/activate(Linux)

    STEP2 - 
        CLONE FROM GITHUB OR DOWNLOAD ZIP
        - NAVIGATE TO BLOG APPLICATION USING TERMINAL
        - RUN COMMAND TO INSTALL REQUIREMENTS
                pip install -r requirements.txt
    
### RUN MIGRATIONS ###
    run command to migrate database
        - python manage.py migrate

### DETAILS AND API DESCRIPTIONS ###

    -- PROJECT CONTAIN TWO APP 
        1 - userProfile - for authentication and profile 
        2-  blogApp - contains Posts and Comments model 

    -- Authentications is done using jwt token based authentications

## APP1 - userProfile api's

    -- REGISTER:(POST REQUEST)
        http://127.0.0.1:8000/api/profile/register 
    
    -- LOGIN:
        http://127.0.0.1:8000/api/profile/login

        OUTPUT- IT GIVES TWO VALUES ONE IS ACCESS TOKEN AND ANOTHER IS REFERESH TOKEN
        // WITHOUT ACCESS TOKEN USER NOT ABLE TO ACCESS ANY API'S

    -- REFERESH : 

## APP2 : blogApp api's

    1- Fetching Posts and create new posts(GET and POST requests)
     # page parameter is used for pagination (applicatble in GET request)
        
        http://127.0.0.1:8000/api/blog/posts/?page=2

     #output contains details with likes and likes count

    2- for fetching comments of given post(GET and POST request)

        http://127.0.0.1:8000/api/blog/post/<post_id>/comments
    
    3 - for update ,delete and getting single POST api url 

        http://127.0.0.1:8000/api/blog/post/<post_id>

    4 - for update ,delete and getting single "COMMENT" api url

        http://127.0.0.1:8000/api/blog/comment/<comment_id>

    5 - LIKE ON POSTS 

        http://127.0.0.1:8000/api/blog/post/<post_id>/like

        OUTPUT - returns like_counts and like arrays contains user's id


### FOR TESTING THE CURL IS PROVIDED IN "test_curl.txt" ###

### OR USER CAN DIRECTLY IMPORT DJANGO-BLOG APP.postman_collection.json in Postman ###

# Django-Blog-Application
