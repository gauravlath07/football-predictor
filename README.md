# Team-up

### About

Team-up is an angular, node, express website which uses statistics from English Premier League to predict the outcome of football games. 

The outcome of a game is decided on using a combination of individual player statistics and team statistics - 
Player stats analyzed - 
* bookings
* fantasy points per game
* fantasy teams selected percentage
* fantasy dreamteam count
* fantasy cost change
* EA Influence score
* minutes played
* player creativity
* current form
* goals
* assists
* player threat

Team statistics analyzed - 
* Total shot ratio - A ratio to explain how teams fare against their average competition in the shots battle. Ex: If United have 20 shots in a match and Newcastle have 10, United's shot ratio for that match will be 67% and Newcastle's will be 33%.
* Shots on target ratio - The ratio of shots that are on target for a team
* Score percentage - The ratio of shots on target that are goals
* Save percentage - The ratio of shots on target of the opposing team that have been saved.

### Data Model
To predict the result Team-up makes use of Python's scikit-learn library's Random Forest Classifier with 16 sample splits and a minimum of 4 leaves in its decision trees to compute the possible outcome.

The data is cleaned and normalized using Pandas and NumPy.

Currently the data model consists of all English Premier League games from March 1st, 2017 onwards. Once the the data model exceeds 100 observations for training possible feature additions could include - 
* Exact score prediction
* Predicting number of bookings 
* Predicting the exact shots on target
* Predicting possession

The opportunities are literally endless...

### Important Links
Website link - http://football.gauravlath.xyz <br />
Front end repository - https://github.com/chenleishen/football-predictor-frontend <br />
Back end repository - https://github.com/gauravlath07/football-predictor

## Want to contribute ??

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Start off by cloning both the front end and back end repositories to your local machine. 

### Prerequisites

For just running the app you will need:
* npm (oh look, npm wrote [something](http://blog.npmjs.org/post/85484771375/how-to-install-npm) about how to get npm, handy)

For Testing and Developing you will need:
* Gulp Command Line Tool (globally)

```
npm install gulp-cli --global
```

### Installing Dependancies

Make sure you have npm and Gulp Command Line Tool

Then enter the front end repo using comamnd line and install npm modules by 

```
npm install
```

Then start the application using -

```
npm start
```

you should probably see a message from console that says listening on localhost:3000

Type in localhost:3000 in browser and the website will be up and running. 

Time to get the the supporting Python API running. Enter the Python repo on command line and type - 

```
pip install -r requirements.txt
```

and you'll have all the dependancies started.

### Developing

The app is using gulp and browserify, run gulp browserify after every single change OR simply run gulp watch before you make any change

```
gulp watch
```
```
gulp browserify
```
Make sure you have gulp command line tool though.

The only thing missing to get your app running is the database. Contact [me](mailto:glath@uwaterloo.ca) to get a CSV copy of the training dataset and you are good to go :)))

## Built With

* [Angular & Node, or MEAN without MongoDB](http://mean.io/) - The web framework used
* [elasticsearch](https://www.elastic.co/products/elasticsearch) - Database
* [npm](https://www.npmjs.com/) - Dependency Management

## Authors

This is a collaboration between [Chenlei Shen](https://github.com/chenleishen) and [Gaurav Lath](https://github.com/gauravlath07)

## Acknowledgments

* Hat tip to anyone who's code was used
* Stack Overflow
