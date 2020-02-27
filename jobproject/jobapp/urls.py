from django.urls import path
from jobapp import views

app_name = "jobapp"

urlpatterns = [
    path("about/", views.AboutView.as_view(), name='about'),
    path("job/lists/", views.ListJobView.as_view(), name='job_list'),
    path('job/<int:pk>/', views.DetailJobView.as_view(), name='job_detail'),
    path("jobapply/", views.CreateJobView.as_view(), name="jobapply"),
    path('job/<int:pk>/edit', views.UpdateJobView.as_view(), name='job_edit'),
    path('job/<int:pk>/remove/', views.DeleteJobView.as_view(), name='job_remove'),
    path("review/lists/", views.ListReviewView.as_view(), name='review_list'),
    path('review/<int:pk>/', views.DetailReviewView.as_view(), name='review_detail'),
    path("review/", views.CreateReviewView.as_view(), name="review"),
    path('review/<int:pk>/edit', views.UpdateReviewView.as_view(), name='review_edit'),
    path('review/<int:pk>/remove/', views.DeleteReviewView.as_view(), name='review_remove'),
    path("jobapply/thankyou", views.thankyou, name="thankyou"),
    path("register/jobseeker", views.register, name="register"),
    path("login/jobseeker", views.user_login, name="user_login"),
    path("register/manager", views.manager_register, name="manager_register"),
    path("login/manager", views.manager_login, name="manager_login"),
]
