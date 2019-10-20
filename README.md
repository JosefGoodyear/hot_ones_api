# Hot Ones API
*** Up-to-date as of 10/20/2019 ***

![Hot Ones](https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Hot_Ones_by_First_We_Feast_logo.svg/500px-Hot_Ones_by_First_We_Feast_logo.svg.png)
##### An API for the youtube show Hot Ones. This project is deployed [here](https://hotonesapi.herokuapp.com/). 
### Overview
The Hot Ones API is written in Python with the Django and Django-REST frameworks. Data is stored in a PostgreSQL database, and the API is hosted by heroku. 
### How to Use
This API only supports GET requests. All API calls must be prepended with: ```https://hotonesapi.herokuapp.com```.

There are 3 endpoints for the API:
  * /seasons/
  * /episodes/
  * /hotsauces/
  
These endpoints can be further filtered by appending episode number, season number, or hotsauce id to your request. Additionally, search is enabled for guest names and hot sauce names:

```https://hotonesapi.herokuapp.com/episodes/?search=Tony```

```https://hotonesapi.herokuapp.com/hotsauces/?search=Louisiana```

Interactive documentation (with Swagger) can be found [here](https://hotonesapi.herokuapp.com/documentation).
### Resources
The endpoints have the following resources:
* /seasons/:
  * season_id
  * number_of_episodes
* /episodes/:
  * episode_id 
  * guest
  * episode_in_season
  * title
  * link
  * completed (Did the guest complete the Hot Ones challenge?)
  * dab (Did the guest "dab" the last wing?)
  * vegan (Were the wings vegan?)
  * season (a foreign key from seasons)
* /hotsauces/:
  * hotsauce_id
  * name
  * [scoville_units](https://en.wikipedia.org/wiki/Scoville_scale)
  * seasons (a many-to-many relationship with seasons)
  
If there are any other datapoints you'd like included, let me know!


### Authorization and Authentication
Neither authorization nor authentication are required to use this API. If you use this API in a project, please consider utilizing a cache to limit API requests and conserve bandwith.
### Disclaimer
I am not affiliated with Hot Ones or First We Feast. I just enjoy hot wings. Most of this data is taken from wikipedia. If you find any errors in the data, please send me a message and I can either fix it or give you admin privileges.
### Author
[Josef Goodyear](https://github.com/JosefGoodyear/)
