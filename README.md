# django-guess  

Django Libraries for enabling data-driven user-experiences on the web inspired by [guess-js/guess: Libraries & tools for enabling Machine Learning driven user-experiences on the web](https://github.com/guess-js/guess)      

-------------------------------------------------
## Motivation

On regular pages, you can use Guess.js to prefetch pages based on Google Analytics access results.
It seems possible to prefetch from ButServiceWorker even on AMP page.
But You can add `<link rel =" prefetch ">` for each page of AMP without using ServiceWorker using Django Command and Template tags.    
If good old web site , I think that it is better to output the preload tag on the server side.    

-------------------------------------------------
## Getting started     

* **Installation**   
```console
pip install git+https://github.com/kemsakurai/django-guess      
```
* **Edit INSTALLED_APPS in settings.py**        
Please add the following setting to INSTALLED_APPS.    
```python
INSTALLED_APPS = (
    ....
    "guess",
    ...
)
```    

* **Add VIEWID of Google Analytics and location of credentials.json**     
Please add VIEWID and   credentials.json location in settings.py     
```python
GUESS_SETTINGS = {      
    "VIEW_ID" : "103185238",
    "CREDENTIALS" : "/home/user_name/credentials.json"
}
```

* **Migration execution**
Running migrate creates a `guess_guessresult` table.
This will be the table that stores the data analysis results of Google Analytics.
```console
python3.6 manage.py migrate
```    

* **Execute command**
When you run `store_ga`, you will register the data analysis result of Google Analytics.
```console
python3.6 manage.py store_ga       
```

* **Schedule execution**
If you are using [kraiz / django-crontab: dead simple crontab powered job scheduling for django.] (https://github.com/kraiz/django-crontab), schedule execution will be can setted as follows I can do it.    
```python
CRONJOBS = [
	('30 01 * * *', 'django.core.management.call_command', ['store_ga'], {}, '>> /var/log/store_ga.log'),
]
```
Of course, schedule execution is also possible by defining it to crontab.     

* **Add a template tag**
Add the following tag in the head tag of the template.
This adds `<link rel =" prefetch ">` based on the data analysis result of Google Analytics.    
```html
{% load guess %}       
{% ifinstalled guess %}
	{% prefetch request.path %}
{% endifinstalled %}
```

------------------------------------------
## How to determine the page to prefetch
It is not faithful to the implementation of Guess.js, but we decide the page to prefetch with the following logic.

1. Acquire Google Analytics data for 180 days from the command execution date. When acquiring data Specifing the following dimensions and metrics.
* Dimensions
	* ga: pagePath
	* ga: previousPagePath
* Metrics
	* ga: pageviews
	* ga: exits

2. previousPagePath excludes the data of `(entrance)` and computes the total pageview of pagePath per previousPagePath.
3. Page view Extracts the top 20% of the top page.
[1]: As a result of analyzing the number of accesses of this site, it seemed to be in accordance with Pareto's law, so we set it as the top 20%.
4. From the extraction result of `3.`, extract only the page where the transition occurred with a probability of 10% or more.
5. Register the extraction result of `4.` in the table.

------------------------------------------
## TODO        
* Enable to control the acquisition period and threshold of analysis data.
* Make it possible to identify the prefetching target page by another calculation method.     

