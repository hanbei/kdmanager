from django.contrib import admin

# Register your models here.
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name','birth_date','gender','grade','email','zekken','jacket','active')

admin.site.register(Member, MemberAdmin)
