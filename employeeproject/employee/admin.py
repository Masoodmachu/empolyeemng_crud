from django.contrib import admin
from employee.models import Company,Department,Employee,CustomUser
# Register your models here.

admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(CustomUser)