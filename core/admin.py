from django.contrib import admin
from .models import *


admin.site.register(Autor)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Loan)