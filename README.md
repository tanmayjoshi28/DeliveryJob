# DeliveryJob
### MULTIPLE USER TYPE IMPLMENTATION 
##### 1 - MANAGER
#### 2 - OPERATOR
  
### MANAGERS CAN MAKE:
##### 1-) DIFFERENT AREAS AVAILABLE 
##### 2-) CAN SEE DETAILS THE APPLICATION' FROM DIFFERENT AREA'S
##### 3-) CAN EITHER DELETE OR CONTACT THE PERSON FOR FURTHER VERIFICATION
                 
### OPERATOR 
##### 1-) FOR THE APPLICANT TO APPLY FOR JOB HE HAS TO SUBMIT HIS DETAILS TO THE OPERATOR
##### 2-) THOSE DETAILS AFTER SUBMISSION ARE VISIBLE TO MANAGERS ACORDINGLY
         
    BOTH MANAGERS AND OPERATOR'S ARE CREATED BY ADMIN 
    BUT FOR LEARNING PURPOSE I HAVE ADDED OPERATOR REGISTRATION FORM BUT NOT THE FORM FOR REGISTRATION OF OPERATORS.
         
 ### Install [Django](https://docs.djangoproject.com/en/3.0/intro/install/) and [BeautifullSoup](https://pypi.org/project/beautifulsoup4/)
#### To Run open Terminal :
##### Go to directory in which manage.py is located :
ENTER the follwing stepwise
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### If it is showing error python not defined :
Refer [This](https://geek-university.com/python/add-python-to-the-windows-path/) Article

## To access Admin :
### First create a superuser:
#### Open Terminal :
#### Go to directory in which manage.py is located :
```
python manage.py createsuperuser
```
Follow the prompts and runserver again , add '/admin' to the url       
