from rest_framework import serializers
from .models import AdminUser, Service, Provider, ProviderSchedule, Product, BroadmoorProduct, BroadmoorProductDetail, \
    Employee, CommonUser, MailBox, Watercooler, Comment


class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminUser
        fields = ('adminID', 'adminEmail', 'adminName', 'adminPassword', 'adminImageUrl', 'adminBroadmoor', 'adminLogoImageUrl', 'adminCompany')

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('proid', 'adminID', 'proProfileImageUrl', 'proFirstName', 'proLastName', 'proEmail', 'proPassword', 'proPhone', 'proCity', 'proAddress', 'proCompany', 'proToken','proServicePercent', 'proSalary', 'proProductSalePercent', 'proAvailable')

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ('serviceid', 'proid', 'adminID', 'proServicePictureUrl', 'proBeautyCategory', 'proBeautySubCategory', 'proServicePrice', 'proServiceDescription', 'providerTakeHome', 'managerTakeHome')

class ProviderScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProviderSchedule
        fields = ('availableid', 'proid', 'availableStart', 'availableEnd', 'availableComment')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('itemid', 'proid', 'itemPictureUrl', 'itemBrand', 'itemProduct', 'itemName', 'itemSize', 'itemPrice', 'itemDescription', 'itemInventoryNum', 'itemSaleStatus', 'providerTakeHome', 'managerTakeHome')

class BroadmoorProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = BroadmoorProduct
        fields = ('bm_proid', 'adminID', 'bm_proImageUrl', 'bm_proName', 'bm_proInventoryNum', 'bm_proCategory', 'bm_proAdditional')

class BroadmoorProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BroadmoorProductDetail
        fields = ('bm_detailID', 'bm_proid', 'bm_proSize', 'bm_proQuantity', 'bm_proPrice')

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('em_id', 'adminID', 'em_image', 'em_name', 'em_gender', 'em_email', 'em_password', 'em_millennial', 'em_givenbuck', 'em_usedbuck', 'em_interaction', 'em_status')

class CommonUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommonUser
        fields = ('userid', 'email', 'first_name', 'last_name', 'age', 'address', 'job', 'education', 'interests', 'relationship',
                  'place_name', 'user_lat', 'user_lon', 'photo_url', 'survey', 'em_millennial', 'phone_number')

class MailBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = MailBox
        fields = ('mail_id', 'from_mail', 'to_mail', 'text_message', 'image_message_url', 'lat_message', 'lon_message', 'name', 'photo_url', 'request_date', 'service', 'service_reqdate', 'status')

class WatercoolerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watercooler
        fields = ('id', 'name', 'email', 'photoUrl', 'company', 'category', 'content', 'link')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'info_id', 'photoUrl', 'name', 'email', 'text', 'imageUrl')



























