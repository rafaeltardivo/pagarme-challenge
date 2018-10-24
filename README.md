# gastarme
A credit card hub "wallet" service, designed to improve the customer payment experience.

## Table of Contents

- [How it works](#how-it-works)
- [Technology](#technology)
- [Developing](#developing)
	- [First Install](#first-install)
	- [Running the tests](#running-the-tests)
	- [Reseting your environment](#running-the-tests)
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


## How it works

### Wallet and cards
You'll need to create a **wallet** and add your **credit cards** to it. After the registration proccess, you will be able to make **purchases** without worrying about which card will be used, our [card management criteria](#card-management-criteria) will take care of it for you.

### Card management criteria

#### Billing date
Let's say you have a wallet with these two cards:

|   |  Number |  Limit |  Billing Day |
|---|---|---|---|
|  *Card One* | 4291749290818600  | 900.00  |  9 |
|  *Card Two*  | 4291749290818622  | 800.00  | 8  |

The **first priority** is the later billing date, so the card chosen is the one who bills later, which is the **Card One**.

#### Limit
Let's say you have a wallet with these two cards:

|   |  Number |  Limit |  Billing Day |
|---|---|---|---|
|  *Card One* | 4291749290818600  | 900.00  |  8 |
|  *Card Two*  | 4291749290818622  | 800.00  | 8  |

The **second priority** is the lower limit. Since they are billed on the same day, **Card Two** will be chosen for having the lower credit limit.

#### Using more than one card

If your purchase exceeds the chosen card limit, the next one will be used considering the same criteria.

### Billing

You'll be billed for each card used, always considering the next month expiration day. Wanna know more about our project, please check our [API documentation](#api-documentation)

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

### Running the tests
```
make test  
```
### Reseting your environment
If eventually you want to reset your environment, execute:
```
make destroy
```
After that, in order to run the application you'll need repeat the [First Install](#first-install) proccess.

## API Documentation
 https://rafaeltardivo.github.io/gastarme/

## Acknowledgement
To the open-source community for providing us such a rich set of tools to work with.

