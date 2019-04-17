# ph4youtube

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Cloning 
To clone the project onto your local machine, do:
```
git clone https://github.com/karthikkashyap98/ph4youtube
```
## Installing
- Create a virtual environment:
  ```
  mkvirtualenv name-of-env
  ```
- Navigate to the project folder in the terminal and do:
  ```
  pip install -r requirements.txt
  ```
- This project uses a postgreSQL database, which can be downloaded [here](https://www.openscg.com/postgresql/installers.jsp/).

## End Points

  ###  /discovery/
  `GET` request to this endpoint will provide JSON of catalog or list view of all discoveries as shown below:
  
  `POST` request to this endpoint with the following JSON, will create a new Discovery:
  
  
  ### /discovery/id/
  `GET` request to this endpoint will provide JSON of Discovery with that 'id'. 
  
  ### /category/    
  `GET` request to this endpoint will provide JSON list of all the categories.
  
  `POST` request to this endpoint with the following JSON, will create a new Category.
  
  (detail page can be found at `/category/id/`).
  
  ### /comments/
  `POST` request to this endpoint with the following JSON can add a new comment. 
  
  
  ### /upvote/id/
  `GET` request to this endpoint will add a vote to the Discovery with that 'id'.
  
  ### /downvote/id/
  `GET` request to this endpoint will remove a vote in the Discovery with that 'id'.
  
  
  
  
  
