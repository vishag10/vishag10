from django.contrib import admin
from .models import CustomUser, Job, JobApplications, JobCategory
from django.contrib.auth.models import Group
# Register your models here.

class UserDetails(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["username", "user_type"]}),
        ("More information", {"fields": ["phone_number", "email"]}),
    ]

    list_display = ["username", "user_type"]    
    list_filter = ["user_type", ]                           #filtering
    search_fields = ["username"]                                    #search
    list_per_page = 10 


class JobDetails(admin.ModelAdmin):
    list_display = ["user_username", "get_jobcategory_name", "Price"]
    list_filter = ["Price"]
    search_fields = ["worker_id__username", "jobcategory_id__job_name"]  # Update to use jobcategory_id__job_name
    list_per_page = 10
    readonly_fields = ('worker_id','jobcategory_id', 'Price','date', 'description')
    # Define a method to get related fields
    def user_username(self, obj):
        return obj.worker_id.username
    
    def get_jobcategory_name(self, obj):
        return obj.jobcategory_id.job_name


    # Customize the column headers
    user_username.short_description = "Username"
    get_jobcategory_name.short_description = "Job Category"



class JobCategoryDetails(admin.ModelAdmin):
    readonly_fields = ('job_name', 'image', 'job_details')  

class JobApplicationsAdmin(admin.ModelAdmin):
    list_display = ('employer_id', 'job_id', 'status')
    list_filter = ('status', 'booked_date')
    search_fields = ('employer_id__username', 'job_id__jobcategory_id__job_name')
    readonly_fields = ('employer_id', 'job_id', 'status','booked_date', 'total_amount', 'rating','review')
    list_per_page = 10

    def get_actions(self, request):
        # Remove the delete action for certain conditions
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions




admin.site.register(CustomUser, UserDetails)
admin.site.register(Job, JobDetails)
admin.site.register(JobCategory,JobCategoryDetails)
admin.site.register(JobApplications, JobApplicationsAdmin)

admin.site.unregister(Group)

admin.site.site_header= 'Find My Worker'