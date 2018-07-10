# edNews

Finding news articles about your favorite congressman

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Tested on mac os
Python3
Brew
```

### Installing

A step by step series of examples that tell you how to get a development env running

API installation

```
$ pip3 install newsapi-python
```

Library installation

```
$ pip3 install newspaper3k
```


## Example usage

```
$ Hi welcome to edNews- news all about Ed!
$ Please enter your start date in this format: MM/DD/YYYY eg. 07/04/2018
$ 07/06/2018
$ How many days from 2018-07-06?
$ 1
$ Assuming endate: 2018-07-07T00:00:00
Folder generated: 2018-07-06_to_2018-07-07
Files generated: news articles, FINAL.txt, LINKS.html
```


## Built With

* newsapi (newsapi.org)
* codelucas - newspaper (https://github.com/codelucas/newspaper)

## Known issues

* API restricts requests to 6 pages and back 1 month
* API retrieves articles from local news stations that run the same content 
* Multilanguage support for article conversion
* library can't parse all links
* unicode conversions for links to webpages (works fine with Preview on mac os)

## Authors

Lawrence 
