from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.home, name="home"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('login/', views.login_page, name="login_page"),
    #FAQS
    path('about_us/', views.about_us, name="about_us"),
    path('services_page/', views.services_page, name="services_page"),
    
    path('logout/', views.logout_page, name='logout_page'),
    path('create_project/', views.create_project, name="create_project"),
    path('create_project/<int:project_id>/add_collaborators/', views.add_collaborators, name='add_collaborators'),
    path('create_project/<int:project_id>/upload_files/', views.upload_files, name='upload_files'),
    path('project/', views.project_page, name='project_page'),
    path('projects/<int:researcher_id>/', views.filtered_projects, name='filtered_projects'),
    
    path('profile/', views.profile_page, name='profile_page'),
    path('myProject/', views.myProject_page, name='myProject_page'),
    path('myProject/<str:status>/', views.myProject_page, name='myProject_page_status'),
    path('collaborated-projects/', views.collaborated_projects, name='collaborated_projects'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/cancel/', views.cancel_project, name='cancel_project'),
    path('details/<int:project_id>/', views.details_page, name='details_page'),
    
    path('project/<int:project_id>/update/', views.update_project, name='update_project'),
    path('files/<int:project_id>/update/', views.update_files, name='update_files'),

    path('complete/<int:project_id>/complete/', views.complete_project, name='complete_project'),
    
    #paypal intergrations
    path('subscribe/', views.subscribe, name='subscribe'),
    path('paypal-return/',views.paypal_return, name='paypal_return'),
    path('paypal-cancel/', views.paypal_cancel, name='paypal_cancel'),
    path('subscription_status/', views.subscription_status, name='subscription_status'),

    path('invalid_email/', views.invalid_email, name='invalid_email'),
    
    #terms,billing and privacy urls
    path('billing/', views.billing, name='billing'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact_us_page/', views.contact_us_page, name='contact_us_page'),
    
    path('unsubscribe/<str:email>/', views.unsubscribe, name='unsubscribe'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
