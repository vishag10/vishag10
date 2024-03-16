"""
URL configuration for Find_My_Worker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about', views.about, name='about'),
    path('jobs', views.jobs, name="jobs"),
    path('contact', views.contact, name="contact"),
    path('Worker_register', views.worker_register, name="Worker_register"),
    path('employer_register', views.employer_register, name="employer_register"),
    path('Login', views.Login, name="Login"),
    path('Logout',views.Logout, name="Logout"),
    path('view_jobs',views.view_jobs, name="view_jobs"),

    ##############################################################################################
    path('job_details/<int:id>',views.job_details, name="job_details"),
    path('employer_home', views.employer_home, name="employer_home"),
    path('employer_profile', views.employer_profile, name="employer_profile"),
    path('employer_history', views.employer_history, name="employer_history"),
    path('employer_applications', views.employer_applications, name="employer_applications"),
    path('search_jobs', views.search_jobs, name="search_jobs"),
    path('job_apply/<int:id>', views.job_apply, name="job_apply"),
    path('employer_edit_profile', views.employer_edit_profile,name="employer_edit_profile"),
    path('payments/<int:id>', views.payments,name="payments"),
    path('add_review/<int:id>', views.add_review,name="add_review"),

###################################################################################################

    path('worker_home', views.worker_home, name="worker_home"),
    path('worker_profile', views.worker_profile, name="worker_profile"),
    path('worker_edit_profile', views.worker_edit_profile, name="worker_edit_profile"),
    path('add_jobs', views.add_jobs, name="add_jobs"),
    path('view_request', views.view_request, name="view_request"),
    path('view_bookings', views.view_bookings, name="view_bookings"),
    path('payment_request/<int:id>', views.payment_request, name="payment_request"),
    path('edit_applicationstatus/<int:id>', views.edit_applicationstatus, name="edit_applicationstatus"),
    path('edit_job/<int:id>', views.edit_job, name="edit_job"),
    path('delete_job/<int:id>', views.delete_job, name="delete_job"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
