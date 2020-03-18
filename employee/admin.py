from django.contrib import admin
from employee.models import Role,Department,Nationality,Religion,Employee,Bank,Emergency,Relationship, Profile


admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Nationality)
admin.site.register(Religion)
admin.site.register(Employee)
admin.site.register(Bank)
admin.site.register(Emergency)
admin.site.register(Relationship)