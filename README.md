django-admin startproject multi_tenant_project
cd multi_tenant_project
python manage.py startapp core
pip install django-tenants


python manage.py makemigrations
python manage.py migrate_schemas --shared
python manage.py migrate_schemas --tenant
