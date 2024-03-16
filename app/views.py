from django.shortcuts import render,redirect
from .models import CustomUser,Job,  JobApplications,JobCategory
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from .forms import WorkerEditForm, EmployerEditForm

# Create your views here.

def home(request):
    jobs = JobCategory.objects.all()
    return render(request, 'Home/index.html', {'jobs': jobs})


def about(request):
    return render(request, 'Home/about.html')

def jobs(request):
    jobs = JobCategory.objects.all()
    return render(request, 'Home/jobs.html', {'jobs':jobs})



def contact(request):
    return render(request, 'Home/contact.html')

def employer_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        phone_number = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        description = request.POST['about_me']
        pic = request.FILES['image']

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'Home/employer-register.html', {'message': "Username already exists"})
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'Home/employer-register.html', {'message': "Email already exists"})
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            return render(request, 'Home/employer-register.html', {'message': "Phone number already exists"})

        data = CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            email=email,
            description=description,
            pic=pic,
            username=username,
            password=password,
            user_type="employer"
        )
        data.save()
        return redirect(Login)

    else:    
        return render(request, 'Home/employer-register.html')

def worker_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        phone_number = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        description = request.POST['about_me']
        pic = request.FILES['image']

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'Home/worker-register.html', {'message': "Username already exists"})
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'Home/worker-register.html', {'message': "Email already exists"})
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            return render(request, 'Home/worker-register.html', {'message': "Phone number already exists"})

        data = CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            email=email,
            description=description,
            pic=pic,
            username=username,
            password=password,
            user_type="worker"
        )
        data.save()
        return redirect(Login)
    else:    
        return render (request, 'Home/worker-register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
         # Authenticate superusers (admins)
        admin_user = authenticate(request, username=username, password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request, admin_user)
            return redirect(reverse('admin:index'))  # Redirect to the admin dashboard
        elif user is not None:
            # If not an admin, check regular users            
            login(request, user)
            if user.user_type == "worker":     #worker profile
                return redirect(worker_home)
            elif user.user_type == "employer":   #Employer profile
                return redirect(employer_home)  
        else:
            context = {
                'message': "*Invalid credentials"
            }
            return render(request, 'Home/login.html', context)
    else:
        return render(request, 'Home/login.html')
    
def Logout(request):
    logout(request)
    return redirect(Login)



###########################################    EMPLOYER      ##############################################



def employer_home(request):
    data = CustomUser.objects.get(id=request.user.id)
    jobs = JobCategory.objects.all()

    context = {
        'user': data,
        'jobs':jobs
    }
    return render(request, 'Employer/employer-home.html', context)

def employer_profile(request):
    data = CustomUser.objects.get(id=request.user.id)
    print(data)
    context = {
        'user': data
    }
    return render(request, 'Employer/profile.html', context)

def employer_edit_profile(request):
    User = CustomUser.objects.get(id = request.user.id) 
    if request.method == 'POST':
        User.first_name = request.POST['first_name']
        User.last_name = request.POST['last_name']
        User.address = request.POST['address']
        User.phone_number = request.POST['contact']
        User.email = request.POST['email']
        User.username = request.POST['username']
        User.description = request.POST['about_me']
        if 'image' in request.FILES:
            User.pic = request.FILES['image']
        User.save()
        return redirect(employer_profile)
    else:
         context = {
             'User':User
         }
         return render(request, 'Employer/edit-profile.html',context)

def view_jobs(request):
    employer = CustomUser.objects.get(id=request.user.id)
    job_ids_with_applications = JobApplications.objects.filter(employer_id=employer).values_list('job_id', flat=True)
    jobs_without_applications = Job.objects.exclude(id__in=job_ids_with_applications).order_by('-id')

    return render(request, 'Employer/jobs.html', {'jobs':jobs_without_applications})

def job_details(request,id):
    job = Job.objects.get(id=id)
    applications = JobApplications.objects.filter(job_id=job)
    print(applications)
    context = {
        'applications':applications,
        'job':job
    }
    return render(request, 'Employer/job-details.html',context)

def search_jobs(request):
    User = CustomUser.objects.get(id=request.user.id)
    if request.method == 'GET':
        search_query = request.GET.get('search')
        if search_query:
            jobs = Job.objects.filter(jobcategory_id__job_name__icontains=search_query)
            return render(request, 'Employer/jobs.html', {'jobs':jobs, 'User':User})

def job_apply(request,id):
    jobs = Job.objects.all()
    employer = CustomUser.objects.get(id=request.user.id)
    job = Job.objects.get(id=id)
    if JobApplications.objects.filter(employer_id=employer,job_id=job).exists():
        return redirect(view_jobs)
    
    JobApplications.objects.create(employer_id=employer,job_id=job)
    return redirect(employer_applications)



def employer_history(request):
    employer = CustomUser.objects.get(id=request.user.id)
    applications = JobApplications.objects.filter(employer_id=employer)
    print(applications)
    return render(request, 'Employer/history.html', {'applications':applications})


def employer_applications(request):
    employer = CustomUser.objects.get(id=request.user.id)
    applications = JobApplications.objects.filter(employer_id=employer)
    print(applications)
    return render(request, 'Employer/job-applications.html', {'applications':applications})

def payments(request,id):
    applications = JobApplications.objects.get(id=id)
    if request.method == 'POST':
        payment_status = request.POST['status']
        applications.status = payment_status
        applications.save()
        return redirect(employer_applications)
    else:
        return render(request, 'Employer/payments.html', {'application':applications})
    
def add_review(request,id):
    applications = JobApplications.objects.get(id=id)

    user = request.user  
    if request.method == 'POST':
        rating = request.POST['rate']
        review_text = request.POST['review']
        

        applications.rating = rating
        applications.review = review_text
        applications.save()
        return redirect(employer_applications) 


#################################################      WORKER    ######################################################





def worker_profile(request):
    data = CustomUser.objects.get(id=request.user.id)
    print(data)
    context = {
        'user': data
    }
    return render(request, 'Worker/profile.html', context)

def worker_edit_profile(request):
    User = CustomUser.objects.get(id = request.user.id) 
    if request.method == 'POST':
        User.first_name = request.POST['first_name']
        User.last_name = request.POST['last_name']
        User.address = request.POST['address']
        User.phone_number = request.POST['contact']
        User.email = request.POST['email']
        User.username = request.POST['username']
        User.description = request.POST['about_me']
        if 'image' in request.FILES:
            User.pic = request.FILES['image']
        User.save()
        return redirect(worker_profile)
    else:
         context = {
             'User':User
         }
         return render(request, 'Worker/edit-profile.html', context)



def worker_home(request):
    worker = CustomUser.objects.get(id=request.user.id)
    jobscategory = JobCategory.objects.all()
    jobs = Job.objects.filter(worker_id=worker)
    print(jobs)
    context = {
        'worker':worker,
        'jobs':jobs,
        'jobscategory':jobscategory
        }
    return render(request, 'Worker/worker-home.html', context)


def add_jobs(request):
    worker = CustomUser.objects.get(id=request.user.id)
    jobcategory = JobCategory.objects.all()
    jobs = Job.objects.filter(worker_id=worker)
    if request.method == 'POST':
        JOBcategory_id = request.POST['jobcategory']
        price = request.POST['price']
        description = request.POST['description']
        jobcategory_id = JobCategory.objects.get(id=JOBcategory_id)
        job = Job.objects.create(worker_id=worker, jobcategory_id=jobcategory_id, Price=price, description=description)
        job.save()
        return redirect(worker_home)
    else:
        context = {
        'worker':worker,
        'jobs':jobs,
        'jobscategory':jobcategory
        }
    return render(request, 'Worker/worker-home.html', context)
    
def edit_job(request,id):
    jobs = Job.objects.get(id=id)
    print(jobs)
    if request.method == 'POST':
        jobs.Price = request.POST['price']
        jobs.description = request.POST['description']
        jobs.save()
        return redirect(employer_home)
    context = {
        'jobs':jobs,
        }
    return render(request, 'Worker/edit_job.html', context)

def delete_job(request,id):
    data = Job.objects.get(id=id)
    data.delete()
    return redirect(worker_home)

def view_request(request):
    worker = CustomUser.objects.get(id=request.user.id)
    applications = JobApplications.objects.filter(job_id__worker_id=worker)
    return render(request, 'Worker/history.html', {'applications':applications})

def edit_applicationstatus(request,id):
    applications = JobApplications.objects.get(id=id)
    if request.method == 'POST':
        status = request.POST['status']
        if status == 'approve':
            applications.status = 'Approved'
        elif status == 'reject':
            applications.status = 'Rejected'
        elif status == 'complete':
            applications.status = 'Completed'
        applications.save()
        return redirect(view_request)
    
def payment_request(request,id):
    worker = CustomUser.objects.get(id=request.user.id)
    applications = JobApplications.objects.get(id=id)
    job = Job.objects.get(id=applications.job_id.id)
    if request.method == 'POST':
        no_of_hours = int(request.POST['no_of_hours'])
        applications.total_amount = no_of_hours * job.Price

        applications.save()
        return redirect(view_request)
    
def view_bookings(request):
    worker = CustomUser.objects.get(id=request.user.id)
    applications = JobApplications.objects.filter(job_id__worker_id=worker)
    return render(request, 'Worker/bookings.html', {'applications':applications})


    