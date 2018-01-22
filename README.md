
# Att_coding_v2
Returns open Issues from ATT public repository along with the comments, if any exists.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system using Heroku.

### Prerequisites

Python
Pip
Virtualenv

### Installing
Clone the repository into your local system 

Windows:

Install Python from python.org
Add Python and Pip to system global namespace
Install Virtualenv using following command:

```
Pip install virtualenv
```

Choose directory for virtualenv and create a virtual environment using following command

```
virtualenv <project name>
```
Navigate to the virtualenv directory and activate the environment using following command 
```
.\<project_name>\Scripts\activate
```
Navigate to the local repository where code lives and install the requirements using following command:
```
pip install -r requirements.txt
```
Run the app using following command
```
python app.py
```
Linux:
Install Virtualenv using following command:

```
Pip install virtualenv
```

Choose directory for virtualenv and create a virtual environment using following command

```
virtualenv <project name>
```
Navigate to the virtualenv directory and activate the environment using following command 
```
source <project_name>/bin/activate
```
Navigate to the local repository where code lives and install the requirements using following command:
```
pip install -r requirements.txt
```
Run the app using following command
```
python app.py
```

At this point your application should run on development server. Hit the server in bowser to get the response
And repeat

### Coading Standards
```
PEP8 
```
## Deployment

You can find the documentation on Flask app deployment using Heroku.

## Built With

* [Heroku](http://www.Heroku.org) 

## Versioning
Utilized [Swagger](http://swagger.org/) for API versioning. 

## Authors

* **Santosh Kesireddy** - *Initial work* - [Santosh9991](https://github.com/santosh9991)

## Acknowledgments

* Special thanks to Yogi for suggestions 
