#RESTful webservice using Docker

Created a RESTful Web service that displays data of movies in JSON format using two get routes: 
    
Steps to run RESTful web service:

* Create the project with myapp.py and JSON file in a single folder.
  The templates folder consists of the page.html file which displays the json result on the webpage

* A Docker Image is created by running the following command: -
 "docker build -t movies-image:latest ."

* Run the created movies-image image inside a container using the following command
  "docker run -d -p 5000:5000 --name movies-container movies-image" 

* Check running docker container by "docker ps".

Then open the browser run it with
#localhost:5000

#localhost:5000/movies

#localhost:5000/movies/year
