# Hello,today we're going to make a web site with django.

#### **STEP 1 :** 
**Create a project:**
Move to the specific folder and open **cmd** to create anew project.


#### ```django-admin startproject project_name```


Once the project is created django will create a list of files on it's own for us.

i.e por_1




#### **STEP 2 :**
Check weather the server is running.

#### ```python manage.py runserver```




#### **STEP 3 :**
Time to create projects within a big project.


#### ```python manage.py startapp app_name```



Here,the files in the before main folder copies to this app folder.

i.e newyear in this project



#### **STEP 4 :**
Open the **settings.py** in the main folder ,move to the **INSTALLED_APPS** add that newly added app name.


