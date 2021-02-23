# Spaces Python Backend

1. Framework -> Flask (python) 
2. DB -> MongoDB 
3. Cloud Provider -> Heroku (Master from this repo is deployed - not automatically, reach out to admin)


---

# API Documentation
User CRUD
Path: /user
* GET - Gets user by email id. Request body should be structured as a JSON with the parameter "email".
* POST - Posts user object. User object is a JSON that aligns with user schema. For schema info, scroll down to schema section. 
* UPDATE - updates user object. Send a JSON object with param "email" as well as the other key value pairs that you want to update in the user object. 
* DELETE - Delete user by email id. Request body should be structured as a JSON with the parameter "email".

Lister CRUD
Path: /lister
* GET - Gets lister by email id. Request body should be structured as a JSON with the parameter "email".
* POST - Posts lister object. lister object is a JSON that aligns with lister schema. For schema info, scroll down to schema section. 
* UPDATE - updates lister object. Send a JSON object with param "email" as well as the other key value pairs that you want to update in the lister object. 
* DELETE - Delete lister by email id. Request body should be structured as a JSON with the parameter "email".

Space CRUD
Path: /space
* GET - Gets space by space_id. Request body should be structured as a JSON with the parameter "space_id".
* POST - Posts space object. Space object is a JSON that aligns with user schema. For schema info, scroll down to schema section. 
* UPDATE - updates space object. Send a JSON object with param "email" as well as the other key value pairs that you want to update in the user object. 
* DELETE - Delete space by space_id. Request body should be structured as a JSON with the parameter "space_id".

Search 
All search calls are GET methods. Body must contain a JSON object representing filter conditions. Response is a JSON array containing objects that match the JSON filter. Path for search calls follow the paradigm: /search/{object db you want to search} 
* Space - Most Common - /search/space
* User - /search/user
* Lister - /search/lister

