from django.contrib import admin
from curdapp.models import Employee


class employeeadmin(admin.ModelAdmin):
    list_display = ['eid','ename','eemail','econtact']


admin.site.register(Employee, employeeadmin)
