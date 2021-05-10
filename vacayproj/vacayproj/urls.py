from django.conf.urls import url,include
from django.contrib import admin
from vacay.views import *
from django.conf.urls.static import static
from django.conf import settings
from vacay import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vacay/', include('vacay.urls')),
    url(r'^$',views.login_user_view,  name='login_user_view'),
    # url(r'^$',views.search,  name='search'),
    url(r'^registerAdmin',views.register_admin,  name='register_admin'),
    url(r'^uploadadminpicture',views.upload_adminpicture,  name='upload_adminpicture'),
    url(r'^registerEmployer',views.register_company_admin,  name='register_company_admin'),
    url(r'^uploadAdminImage',views.upload__admin_image,  name='upload__admin_image'),
    url(r'^uploadAdminLogoImage',views.upload__broadmoor_image,  name='upload__broadmoor_image'),
    url(r'^getAdminData/(?P<admin_id>[0-9]+)',views.get_admin_data,  name='get_admin_data'),
    url(r'^loginAdmin',views.login_admin_from_app,  name='login_admin_from_app'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^editservice/(?P<service_id>[0-9]+)/(?P<provider_id>[0-9]+)', views.edit_service_view, name='edit_service_view'),
    url(r'^edit/(?P<service_id>[0-9]+)/(?P<provider_id>[0-9]+)/service/', views.edit_service, name='edit_service'),
    url(r'^editservicepictures/(?P<service_id>[0-9]+)/(?P<provider_id>[0-9]+)/service/', views.editservicepictures, name='editservicepictures'),
    url(r'^addservice/', views.add_service_view, name='add_service_view'),
    url(r'^service/added/', views.add_service, name='add_service'),
    url(r'^addproduct', views.add_product_view, name='add_product_view'),
    url(r'^product/added/', views.add_product, name='add_product'),
    url(r'^edit/product/(?P<product_id>[0-9]+)', views.edit_product_view, name='edit_product_view'),
    url(r'^edit/(?P<product_id>[0-9]+)/product/', views.edit_product, name='edit_product'),
    url(r'^editproductpictures/(?P<product_id>[0-9]+)/product/', views.editproductpictures, name='editproductpictures'),
    url(r'^retail_products_1/$', views.get_broadmoor_products, name='get_broadmoor_products'),
    url(r'^add_retail_products_1/$', views.add_broadmoor, name='add_broadmoor'),
    url(r'^export_xlsx_provider/$', views.export_xlsx_provider, name='export_xlsx_provider'),
    url(r'^import_view_provider/$', views.import_view_provider, name='import_view_provider'),
    url(r'^import/$', views.import_provider_data, name='import_provider_data'),
    url(r'^export_xlsx_service/$', views.export_xlsx_service, name='export_xlsx_service'),
    url(r'^import_view/service/$', views.import_view_service, name='import_view_service'),
    url(r'^import_service/$', views.import_service_data, name='import_service_data'),
    url(r'^export_xlsx_product/$', views.export_xlsx_product, name='export_xlsx_product'),
    url(r'^import_view/product/$', views.import_view_product, name='import_view_product'),
    url(r'^import_product/$', views.import_product_data, name='import_product_data'),
    url(r'^export_xlsx_broadmoor/$', views.export_xlsx_broadmoor, name='export_xlsx_broadmoor'),
    url(r'^import_view/broadmoor/$', views.import_view_broadmoor, name='import_view_broadmoor'),
    url(r'^import_broadmoor/$', views.import_broadmoor_data, name='import_broadmoor_data'),
    url(r'^export_xlsx_employee/$', views.export_xlsx_employee, name='export_xlsx_employee'),
    url(r'^import_view/employee/$', views.import_view_employee, name='import_view_employee'),
    url(r'^import_employee/$', views.import_employee_data, name='import_employee_data'),
    url(r'^export_xlsx_job/$', views.export_xlsx_job, name='export_xlsx_job'),
    url(r'^import_view/job/$', views.import_view_job, name='import_view_job'),
    url(r'^import_job/$', views.import_job_data, name='import_job_data'),
    url(r'^export_xlsx_announce/$', views.export_xlsx_announce, name='export_xlsx_announce'),
    url(r'^import_view/announce/$', views.import_view_announce, name='import_view_announce'),
    url(r'^import_announce/$', views.import_announce_data, name='import_announce_data'),
    url(r'^edit/admin/$', views.edit_admin, name='edit_admin'),
    url(r'^update/(?P<admin_id>[0-9]+)/admin/$', views.update_admin, name='update_admin'),
    url(r'^goto_back/$', views.goto_back, name='goto_back'),
    url(r'^getServiceProviderInfo', views.get_service_provider_info, name='get_service_provider_info'),
    url(r'^getProviderAvailable', views.get_provider_schedule, name='get_provider_schedule'),
    url(r'^getProductInfo', views.get_product_info, name='get_product_info'),
    url(r'^getProviderByAdminID', views.get_providers_by_adminID, name='get_providers_by_adminID'),
    url(r'^addEmInteraction', views.increase_interaction, name='increase_interaction'),
    url(r'^updateProviderToken', views.update_provider_token, name='update_provider_token'),
    url(r'^getBroadmoorInfo', views.get_broadmoor_info, name='get_broadmoor_info'),
    url(r'^getBroadmoorDetailInfo', views.get_broadmoor_detail, name='get_broadmoor_detail'),
    url(r'^getAllEmployeeByAdminID', views.get_employees_by_adminID, name='get_employees_by_adminID'),
    url(r'^updateEmStatus', views.update_employee_status, name='update_employee_status'),
    url(r'^getAllCompanyNames', views.get_companies, name='get_companies'),
    url(r'^getAllJobByAdminID', views.get_jobs, name='get_jobs'),
    url(r'^getAllAnnounceByAdminID', views.get_announces, name='get_announces'),
    url(r'^updateCount', views.update_announce_view, name='update_announce_view'),
    url(r'^getEmployeeForAnnounce', views.get_employees_for_announce, name='get_employees_for_announce'),
    url(r'^getProviderByProEmail', views.login_provider, name='login_provider'),
    url(r'^getServiceByProviderId', views.get_services_from_provider, name='get_services_from_provider'),
    url(r'^getProductInfo', views.get_products_from_provider, name='get_products_from_provider'),
    url(r'^updateProviderAvailable', views.update_provider_schedule, name='update_provider_schedule'),
    url(r'^deleteProviderAvailable', views.delete_provider_schedule, name='delete_provider_schedule'),
    url(r'^getEmployeeByEmail', views.login_employee, name='login_employee'),
    url(r'^send_email/(?P<employee_id>[0-9]+)', views.sendSimpleEmail, name='sendSimpleEmail'),
    url(r'^nearby_services', views.nearby_services, name='nearby_services'),
    url(r'^mylocation', views.get_my_location, name='get_my_location'),
    url(r'^uploadMultipleSchedule', views.add_provider_multiple_schedule, name='add_provider_multiple_schedule'),
    url(r'^updateAllProviderSchedules', views.update_all_providerSchedules, name='update_all_providerSchedules'),
    url(r'^getVaCayBucksInfo/(?P<employee_id>[0-9]+)',views.get_bucks_data,  name='get_bucks_data'),
    url(r'^addEmUsedBuck', views.increase_usedbuck, name='increase_usedbuck'),
    url(r'^updateGivenBuck', views.update_givenbuck, name='update_givenbuck'),
    url(r'^account_create', views.add_account, name='add_account'),
    url(r'^account_details', views.get_account_detail, name='get_account_detail'),
    url(r'^account_update_required', views.update_account, name='update_account'),
    url(r'^savePaySendMail', views.sendPaymentEmail, name='sendPaymentEmail'),
    url(r'^getAdminPaymentAccountId', views.get_admin_accountid, name='get_admin_accountid'),
    url(r'^registerUser', views.register_common_user, name='register_common_user'),
    url(r'^getUserProfile', views.get_user_profile, name='get_user_profile'),
    url(r'^getAllUsers', views.get_all_users, name='get_all_users'),
    url(r'^getMail', views.get_mail_message, name='get_mail_message'),
    url(r'^allSentMail', views.get_sent_message, name='get_sent_message'),
    url(r'^makeMail', views.send_message, name='send_message'),
    url(r'^uploadMailPhoto', views.upload_mail_image, name='upload_mail_image'),
    url(r'^sendMailMessage', views.sendEmailMessage, name='sendEmailMessage'),
    url(r'^sendMailMes', views.sendEmailMes, name='sendEmailMes'),
    url(r'^deleteSentMail', views.delete_sentMail, name='delete_sentMail'),
    url(r'^update_request_message', views.update_request_message, name='update_request_message'),
    url(r'^get_media', views.get_media, name='get_media'),
    url(r'^get_job_media', views.get_job_media, name='get_job_media'),
    url(r'^upload_watercooler', views.add_watercooler, name='add_watercooler'),
    url(r'^updatewatercooler', views.updatewatercooler, name='updatewatercooler'),
    url(r'^get_watercooler', views.get_watercooler, name='get_watercooler'),
    url(r'^delwatercooler', views.delwatercooler, name='delwatercooler'),
    url(r'^delcomment', views.delcomment, name='delcomment'),
    url(r'^upload_comment', views.add_comment, name='add_comment'),
    url(r'^get_comment', views.get_comment, name='get_comment'),
    url(r'^get_all_jobs_for_sharing', views.get_all_jobs_for_sharing, name='get_all_jobs_for_sharing'),
    url(r'^sendEmEmailfromApp', views.sendEmEmailfromApp, name='sendEmEmailfromApp'),
    url(r'^allmailsforserviceprovideracceptordecline', views.allmailsforserviceprovideracceptordecline, name='allmailsforserviceprovideracceptordecline'),
    url(r'^loadphotofromcaysees', views.loadphotofromcaysees, name='loadphotofromcaysees'),
    url(r'^amazon', views.amazon, name='amazon'),
    url(r'^postAdminPhoto', views.postAdminPhoto, name='postAdminPhoto'),
    url(r'^editUserPhoto', views.editUserPhoto, name='editUserPhoto'),
    url(r'^editProviderProfilePhoto', views.editProviderProfilePhoto, name='editProviderProfilePhoto'),
    url(r'^employeewatercoolers', views.employeewatercoolers, name='employeewatercoolers'),
    url(r'^wcdetail/(?P<wc_id>[0-9]+)',views.wcdetail,  name='wcdetail'),
    url(r'^delemwc/(?P<wc_id>[0-9]+)',views.delwc,  name='delwc'),
    url(r'^delemcomment/(?P<comment_id>[0-9]+)/(?P<wc_id>[0-9]+)',views.delemcomment,  name='delemcomment'),
    url(r'^emprofile/(?P<wc_id>[0-9]+)',views.emprofile,  name='emprofile'),
    url(r'^delmultiwcs', views.delmultiwcs, name='delmultiwcs'),
    url(r'^delmultiemcomments', views.delmultiemcomments, name='delmultiemcomments'),
    url(r'^tomessageoptions', views.tomessageoptions, name='tomessageoptions'),
    url(r'^emsignedupforan',views.emsignedupforan,  name='emsignedupforan'),
    url(r'^messagebygrouping',views.messagebygrouping,  name='messagebygrouping'),
    url(r'^tochat',views.tochat,  name='tochat'),
    url(r'^get_notifications',views.get_notifications,  name='get_notifications'),
    url(r'^employees/2/', views.get_employees, name='get_employees'),
    url(r'^chat_page',views.chat_page,  name='chat_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





































