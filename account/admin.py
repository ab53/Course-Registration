from django.contrib import admin

# Register your models here.
from .models import Course, CourseDetail

@admin.register(Course)				# or admin.site.register(Course)
class RegisteredCourseAdmin(admin.ModelAdmin):
	list_display = ['title','owner']

@admin.register(CourseDetail)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['coursecode','coursetitle']	


