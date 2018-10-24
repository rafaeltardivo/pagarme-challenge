# gastarme
A credit card hub "wallet" service, designed to improve the customer payment experience

## Table of Contents

- [Technology](#technology)
- [Developing](#developing)
	- [First Install](#first-install)
	- [Running the tests](#running-the-tests)
- [API Documentation](#testing)
- [Acknowledgement](#acknowledgement)       


## Technology
- [Python](https://www.python.org/) 3.6.5
- [Python Decouple](https://github.com/henriquebastos/python-decouple) 3.1
- [Django](https://www.djangoproject.com/) 2.0
- [Django REST Framework](https://www.django-rest-framework.org/) 3.8.2
- [Django Filter](https://django-filter.readthedocs.io/en/master/) 2.0.0
- [Factory Boy](https://factoryboy.readthedocs.io/en/latest/) 2.11.1  
- [FreezeGun](https://github.com/spulec/freezegun) 0.3.10
- [Coverage](https://coverage.readthedocs.io/en/v4.5.x/) 4.5.1
- [Docker](https://www.docker.com/) 18.06.1-ce, build e68fc7a
- [Docker Compose](https://docs.docker.com/compose/) 1.17.1
- [Mkdocs](https://www.mkdocs.org/)

## Developing
### First Install
1 - Build the application:  
```
make build
```  
2 - Run the application:  
```  
make up-detached
```  
3 - Execute the migrations  
```  
make migrations
```  
**OBS**: If eventually you want to set the project up from scratch again, just execute:
```
make destroy
```
After that, in order to run the application you'll need to repeat steps 1, 2 and 3 again.

### Running the tests
```
make test  
```

## API Documentation
 - [API Documentation](https://rafaeltardivo.github.io/gastarme/)

## Acknowledgement

