from django.contrib import admin

# Register your models here.
from .models import Member, Attendance


class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name', 'birth_date', 'gender', 'grade', 'email', 'zekken', 'jacket', 'active')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date',)


admin.site.register(Member, MemberAdmin)
admin.site.register(Attendance, AttendanceAdmin)
