from django.conf.urls import url
from . import views

app_name = 'vacay'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/$', views.login_admin_from_web, name='login_admin_from_web'),
    url(r'providers/$', views.get_all_providers, name='get_all_providers'),
    url(r'services/(?P<provider_id>[0-9]+)/$', views.get_services, name='get_services'),
    url(r'allservices/$', views.get_all_services, name='get_all_services'),
    url(r'products/(?P<provider_id>[0-9]+)/$', views.get_products, name='get_products'),
    url(r'allproducts/$', views.get_all_products, name='get_all_products'),
    url(r'setup/(?P<provider_id>[0-9]+)/$', views.get_setup, name='get_setup'),
    url(r'edit_provider/(?P<provider_id>[0-9]+)/$', views.edit_provider_view, name='edit_provider_view'),
    url(r'edit/(?P<provider_id>[0-9]+)/provider/$', views.edit_provider, name='edit_provider'),
    url(r'delete/(?P<provider_id>[0-9]+)/provider/$', views.delete_provider, name='delete_provider'),
    url(r'addprovider/$', views.add_provider, name='add_provider'),
    url(r'providersetups/$', views.get_setups, name='get_setups'),
    url(r'edit/(?P<provider_id>[0-9]+)/setup/$', views.edit_setup_view, name='edit_setup_view'),
    url(r'(?P<provider_id>[0-9]+)/edit_setup/$', views.edit_setup, name='edit_setup'),
    url(r'addretailproduct/1/$', views.add_broadmoor_product, name='add_broadmoor_product'),
    url(r'editretailproduct/(?P<broadmoorproduct_id>[0-9]+)/$', views.edit_broadmoor_product, name='edit_broadmoor_product'),
    url(r'update/(?P<broadmoorproduct_id>[0-9]+)/retailproduct/$', views.update_broadmoor_product, name='update_broadmoor_product'),
    url(r'updatebroadmoorpictures/(?P<broadmoorproduct_id>[0-9]+)/retailproduct/$', views.updatebroadmoorpictures, name='updatebroadmoorpictures'),
    url(r'detailretailproduct/(?P<broadmoorproduct_id>[0-9]+)/$', views.detail_broadmoor_product, name='detail_broadmoor_product'),
    url(r'addretaildetail/(?P<broadmoorproduct_id>[0-9]+)/$', views.add_detail_broadmoor, name='add_detail_broadmoor'),
    url(r'addretail/(?P<broadmoorproduct_id>[0-9]+)/detail/$', views.add_broadmoor_detail, name='add_broadmoor_detail'),
    url(r'editretaildetail/(?P<broadmoorproductdetail_id>[0-9]+)/(?P<broadmoorproduct_id>[0-9]+)/$', views.edit_detail_broadmoor, name='edit_detail_broadmoor'),
    url(r'edit/retaildetail/(?P<broadmoorproduct_id>[0-9]+)/(?P<broadmoorproductdetail_id>[0-9]+)/$', views.edit_detail_broadmoor_product, name='edit_detail_broadmoor_product'),
    url(r'employees/2/$', views.get_employees, name='get_employees'),
    url(r'editemployee/(?P<employee_id>[0-9]+)/$', views.edit_employee, name='edit_employee'),
    url(r'update_employee/(?P<employee_id>[0-9]+)/$', views.update_employee, name='update_employee'),
    url(r'delete_employee/(?P<employee_id>[0-9]+)/$', views.delete_employee, name='delete_employee'),
    url(r'addemployee/2/$', views.add_employee, name='add_employee'),
    url(r'2/add_employee/$', views.add_employee_process, name='add_employee_process'),
    url(r'jobs/3/$', views.show_jobs, name='show_jobs'),
    url(r'addjob/3/$', views.add_job, name='add_job'),
    url(r'add/job/$', views.add_job_process, name='add_job_process'),
    url(r'editjob/(?P<job_id>[0-9]+)/$', views.edit_job, name='edit_job'),
    url(r'updatejob/(?P<job_id>[0-9]+)/$', views.update_job, name='update_job'),
    url(r'deletejob/(?P<job_id>[0-9]+)/$', views.delete_job, name='delete_job'),
    url(r'announcements/3/$', views.show_announcements, name='show_announcements'),
    url(r'editannouncement/(?P<announce_id>[0-9]+)/$', views.edit_announcement, name='edit_announcement'),
    url(r'update_announcement/(?P<announce_id>[0-9]+)/$', views.update_announcement, name='update_announcement'),
    url(r'updateannouncementpictures/(?P<announce_id>[0-9]+)/$', views.updateannouncementpictures, name='updateannouncementpictures'),
    url(r'delete_announcement/(?P<announce_id>[0-9]+)/$', views.delete_announcement, name='delete_announcement'),
    url(r'addannouncement/3/$', views.add_announcement, name='add_announcement'),
    url(r'add/announcement/$', views.add_announcement_process, name='add_announcement_process'),
    url(r'addproviderview/$', views.add_provider_view, name='add_provider_view'),
    url(r'delete/(?P<service_id>[0-9]+)//(?P<provider_id>[0-9]+)/service/$', views.delete_service, name='delete_service'),
    url(r'(?P<product_id>[0-9]+)/delete/product/$', views.delete_product, name='delete_product'),
    url(r'delete/(?P<broadmoorproductdetail_id>[0-9]+)/(?P<broadmoorproduct_id>[0-9]+)/retail_product/$', views.delete_detail_broadmoor, name='delete_detail_broadmoor'),
    url(r'delete/(?P<broadmoorproduct_id>[0-9]+)/broadmoorproduct/$', views.delete_broadmoor_product, name='delete_broadmoor_product'),
    url(r'search_provider/$', views.search_provider, name='search_provider'),
    url(r'search_service/$', views.search_service, name='search_service'),
    url(r'search_product/$', views.search_product, name='search_product'),
    url(r'search_provider_setup/$', views.search_provider_setup, name='search_provider_setup'),
    url(r'search_job/$', views.search_job, name='search_job'),
    url(r'search_employee/$', views.search_employee, name='search_employee'),
    url(r'search_announce/$', views.search_announce, name='search_announce'),
    url(r'search_broadmoor_product/$', views.search_broadmoor_product, name='search_broadmoor_product'),
    url(r'on_map/(?P<provider_id>[0-9]+)/$', views.show_on_map, name='show_on_map'),
    url(r'on_map/my_loc/$', views.show_my_loc, name='show_my_loc'),
    url(r'get_all_provider_schedules/$', views.get_all_providerSchedules, name='get_all_providerSchedules'),
    url(r'select_provider_service/$', views.select_provider_service, name='select_provider_service'),
    url(r'select_provider_product/$', views.select_provider_product, name='select_provider_product'),
    url(r'delete_multiple_provider/$', views.delete_multiple_provider, name='delete_multiple_provider'),
    url(r'delete_multiple_service/$', views.delete_multiple_service, name='delete_multiple_service'),
    url(r'delete_multiple_product/$', views.delete_multiple_product, name='delete_multiple_product'),
    url(r'delete_multiple_retail/$', views.delete_multiple_retail, name='delete_multiple_retail'),
    url(r'delete_multiple_employee/$', views.delete_multiple_employee, name='delete_multiple_employee'),
    url(r'delete_multiple_job/$', views.delete_multiple_job, name='delete_multiple_job'),
    url(r'delete_multiple_announce/$', views.delete_multiple_announce, name='delete_multiple_announce'),
    url(r'get_all_service_breakdown/$', views.get_all_service_breakdown, name='get_all_service_breakdown'),
    url(r'get_all_product_breakdown/$', views.get_all_product_breakdown, name='get_all_product_breakdown'),
    url(r'service_multiple/(?P<service_id>[0-9]+)/$', views.service_multiple, name='service_multiple'),
    url(r'product_multiple/(?P<product_id>[0-9]+)/$', views.product_multiple, name='product_multiple'),
    url(r'retail_multiple/(?P<broadmoorproduct_id>[0-9]+)/$', views.retail_multiple, name='retail_multiple'),
    url(r'announce_multiple/(?P<announce_id>[0-9]+)/$', views.announce_multiple, name='announce_multiple'),
    url(r'provider_picture/(?P<provider_id>[0-9]+)/$', views.provider_picture, name='provider_picture'),
    url(r'announce_picture/(?P<announce_id>[0-9]+)/$', views.announce_picture, name='announce_picture'),
    url(r'service_picture/(?P<service_id>[0-9]+)/$', views.service_picture, name='service_picture'),
    url(r'product_picture/(?P<product_id>[0-9]+)/$', views.product_picture, name='product_picture'),
    url(r'retail_picture/(?P<broadmoorproduct_id>[0-9]+)/$', views.retail_picture, name='retail_picture'),
    url(r'employee_picture/(?P<employee_id>[0-9]+)/$', views.employee_picture, name='employee_picture'),
    url(r'show_tips_tricks/$', views.show_tips_tricks, name='show_tips_tricks'),
    url(r'add_tips_tricks/$', views.add_tips_tricks, name='add_tips_tricks'),
    url(r'add_tiptrick_process/$', views.add_tiptrick_process, name='add_tiptrick_process'),
    url(r'edit_tiptrick_process/(?P<tiptrick_id>[0-9]+)/$', views.edit_tiptrick_process, name='edit_tiptrick_process'),
    url(r'edit_tiptrick/(?P<tiptrick_id>[0-9]+)/$', views.edit_tiptrick, name='edit_tiptrick'),
    url(r'edittiptrickpictures/(?P<tiptrick_id>[0-9]+)/$', views.edittiptrickpictures, name='edittiptrickpictures'),
    url(r'delete_tiptrick/(?P<tiptrick_id>[0-9]+)/$', views.delete_tiptrick, name='delete_tiptrick'),
    url(r'tiptrick_picture/(?P<tiptrick_id>[0-9]+)/$', views.tiptrick_picture, name='tiptrick_picture'),
    url(r'tipstricks_multiple/(?P<tiptrick_id>[0-9]+)/$', views.tipstricks_multiple, name='tipstricks_multiple'),
    url(r'delete_multiple_tipstricks/$', views.delete_multiple_tipstricks, name='delete_multiple_tipstricks'),
]




























