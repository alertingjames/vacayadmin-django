from django.db import models

# Create your models here.

class AdminUser(models.Model):
    adminID=models.CharField(max_length=11)
    adminEmail=models.CharField(max_length=80)
    adminName = models.CharField(max_length=50)
    adminPassword = models.CharField(max_length=30)
    adminImageUrl = models.CharField(max_length=500)
    adminBroadmoor = models.CharField(max_length=2)
    adminLogoImageUrl = models.CharField(max_length=500)
    adminCompany = models.CharField(max_length=50)

class Provider(models.Model):
    proid=models.CharField(max_length=11)
    adminID=models.CharField(max_length=11)
    proProfileImageUrl = models.CharField(max_length=500)
    proFirstName = models.CharField(max_length=50)
    proLastName = models.CharField(max_length=50)
    proEmail = models.CharField(max_length=80)
    proPassword = models.CharField(max_length=30)
    proPhone = models.CharField(max_length=30)
    proCity = models.CharField(max_length=50)
    proAddress = models.CharField(max_length=50)
    proCompany = models.CharField(max_length=50)
    proToken = models.CharField(max_length=500)
    proServicePercent = models.CharField(max_length=8)
    proSalary = models.CharField(max_length=20)
    proProductSalePercent = models.CharField(max_length=20)
    proAvailable = models.CharField(max_length=5)

class Service(models.Model):
    serviceid=models.CharField(max_length=11)
    proid = models.CharField(max_length=11)
    adminID=models.CharField(max_length=11)
    proServicePictureUrl = models.CharField(max_length=500)
    proBeautyCategory = models.CharField(max_length=100)
    proBeautySubCategory = models.CharField(max_length=100)
    proServicePrice = models.CharField(max_length=20)
    proServiceDescription = models.CharField(max_length=4000)
    providerTakeHome = models.CharField(max_length=15)
    managerTakeHome = models.CharField(max_length=15)
    video_url = models.CharField(max_length=500)
    youtube_url = models.CharField(max_length=500)
    imageA = models.CharField(max_length=500)
    imageB = models.CharField(max_length=500)
    imageC = models.CharField(max_length=500)
    imageD = models.CharField(max_length=500)
    imageE = models.CharField(max_length=500)
    imageF = models.CharField(max_length=500)
    descA = models.CharField(max_length=500)
    descB = models.CharField(max_length=500)
    descC = models.CharField(max_length=500)
    descD = models.CharField(max_length=500)
    descE = models.CharField(max_length=500)
    descF = models.CharField(max_length=500)

class Product(models.Model):
    itemid=models.CharField(max_length=11)
    proid=models.CharField(max_length=11)
    itemPictureUrl = models.CharField(max_length=500)
    itemBrand = models.CharField(max_length=80)
    itemProduct = models.CharField(max_length=80)
    itemName = models.CharField(max_length=200)
    itemSize = models.CharField(max_length=200)
    itemPrice = models.CharField(max_length=20)
    itemDescription = models.CharField(max_length=4000)
    itemInventoryNum = models.CharField(max_length=11)
    itemSaleStatus = models.CharField(max_length=20)
    providerTakeHome = models.CharField(max_length=15)
    managerTakeHome = models.CharField(max_length=15)
    video_url = models.CharField(max_length=500)
    youtube_url = models.CharField(max_length=500)
    imageA = models.CharField(max_length=500)
    imageB = models.CharField(max_length=500)
    imageC = models.CharField(max_length=500)
    imageD = models.CharField(max_length=500)
    imageE = models.CharField(max_length=500)
    imageF = models.CharField(max_length=500)
    descA = models.CharField(max_length=500)
    descB = models.CharField(max_length=500)
    descC = models.CharField(max_length=500)
    descD = models.CharField(max_length=500)
    descE = models.CharField(max_length=500)
    descF = models.CharField(max_length=500)

class BroadmoorProduct(models.Model):
    bm_proid=models.CharField(max_length=11)
    adminID=models.CharField(max_length=11)
    bm_proImageUrl = models.CharField(max_length=500)
    bm_proName = models.CharField(max_length=300)
    bm_proInventoryNum = models.CharField(max_length=11)
    bm_proCategory = models.CharField(max_length=100)
    bm_proAdditional = models.CharField(max_length=4000)
    video_url = models.CharField(max_length=500)
    youtube_url = models.CharField(max_length=500)
    imageA = models.CharField(max_length=500)
    imageB = models.CharField(max_length=500)
    imageC = models.CharField(max_length=500)
    imageD = models.CharField(max_length=500)
    imageE = models.CharField(max_length=500)
    imageF = models.CharField(max_length=500)
    descA = models.CharField(max_length=500)
    descB = models.CharField(max_length=500)
    descC = models.CharField(max_length=500)
    descD = models.CharField(max_length=500)
    descE = models.CharField(max_length=500)
    descF = models.CharField(max_length=500)

class BroadmoorProductDetail(models.Model):
    bm_detailID = models.CharField(max_length=11)
    bm_proid=models.CharField(max_length=11)
    bm_proSize = models.CharField(max_length=100)
    bm_proQuantity = models.CharField(max_length=11)
    bm_proPrice = models.CharField(max_length=8)

class Employee(models.Model):
    em_id=models.CharField(max_length=11)
    adminID=models.CharField(max_length=11)
    em_image = models.CharField(max_length=500)
    em_name = models.CharField(max_length=80)
    em_gender = models.CharField(max_length=20)
    em_email = models.CharField(max_length=80)
    em_password = models.CharField(max_length=30)
    em_millennial = models.CharField(max_length=20)
    em_givenbuck = models.CharField(max_length=11)
    em_usedbuck = models.CharField(max_length=11)
    em_interaction = models.CharField(max_length=11)
    em_status = models.CharField(max_length=2)


class Job(models.Model):
    job_id=models.CharField(max_length=11)
    adminID=models.CharField(max_length=11)
    job_name = models.CharField(max_length=200)
    job_req = models.CharField(max_length=11)
    job_department = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100)
    job_description = models.CharField(max_length=4000)
    job_postdate = models.CharField(max_length=30)
    job_empty = models.CharField(max_length=500)
    job_survey = models.CharField(max_length=500)
    video_url = models.CharField(max_length=500)
    youtube_url = models.CharField(max_length=500)


class Announce(models.Model):
    an_id=models.CharField(max_length=11)
    adminID=models.CharField(max_length=11)
    an_image = models.CharField(max_length=500)
    an_title = models.CharField(max_length=300)
    an_audience = models.CharField(max_length=300)
    an_subject = models.CharField(max_length=300)
    an_description = models.CharField(max_length=4000)
    an_callofaction = models.CharField(max_length=300)
    an_owneremail = models.CharField(max_length=80)
    an_viewnum = models.CharField(max_length=11)
    an_responsenum = models.CharField(max_length=11)
    an_postdate = models.CharField(max_length=30)
    an_survey = models.CharField(max_length=500)
    video_url = models.CharField(max_length=500)
    youtube_url = models.CharField(max_length=500)
    imageA = models.CharField(max_length=500)
    imageB = models.CharField(max_length=500)
    imageC = models.CharField(max_length=500)
    imageD = models.CharField(max_length=500)
    imageE = models.CharField(max_length=500)
    imageF = models.CharField(max_length=500)
    descA = models.CharField(max_length=500)
    descB = models.CharField(max_length=500)
    descC = models.CharField(max_length=500)
    descD = models.CharField(max_length=500)
    descE = models.CharField(max_length=500)
    descF = models.CharField(max_length=500)

class AnnounceView(models.Model):
    v_id=models.CharField(max_length=11)
    an_id=models.CharField(max_length=11)
    em_id = models.CharField(max_length=11)
    is_signup = models.CharField(max_length=10)

class ProviderSchedule(models.Model):
    availableid=models.CharField(max_length=11)
    proid=models.CharField(max_length=11)
    availableStart = models.CharField(max_length=80)
    availableEnd = models.CharField(max_length=80)
    availableComment = models.CharField(max_length=2000)

class Account(models.Model):
    stripe_id=models.CharField(max_length=30)
    country=models.CharField(max_length=10)
    email = models.CharField(max_length=80)
    created_on = models.CharField(max_length=30)
    modified_on = models.CharField(max_length=30)
    status = models.CharField(max_length=2)

class CommonUser(models.Model):
    userid = models.CharField(max_length=11)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    age = models.CharField(max_length=5)
    address = models.CharField(max_length=200)
    job = models.CharField(max_length=300)
    education = models.CharField(max_length=200)
    interests = models.CharField(max_length=2000)
    relationship = models.CharField(max_length=300)
    place_name = models.CharField(max_length=200)
    user_lat = models.CharField(max_length=200)
    user_lon = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=500)
    survey = models.CharField(max_length=5000)
    em_millennial = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

class MailBox(models.Model):
    mail_id = models.CharField(max_length=11)
    from_mail=models.CharField(max_length=100)
    to_mail=models.CharField(max_length=100)
    text_message = models.CharField(max_length=6000)
    image_message_url = models.CharField(max_length=500)
    lat_message = models.CharField(max_length=100)
    lon_message = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=500)
    request_date = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    service_reqdate = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

class Watercooler(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    photoUrl=models.CharField(max_length=500)
    company=models.CharField(max_length=30)
    category = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    link = models.CharField(max_length=1000)
    comments = models.CharField(max_length=11)

class Comment(models.Model):
    info_id = models.CharField(max_length=11)
    photoUrl=models.CharField(max_length=500)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=80)
    text = models.CharField(max_length=5000)
    imageUrl = models.CharField(max_length=500)

class TipsTricks(models.Model):
    adminID=models.CharField(max_length=11)
    image = models.CharField(max_length=500)
    title = models.CharField(max_length=300)
    audience = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    description = models.CharField(max_length=4000)
    callofaction = models.CharField(max_length=300)
    owneremail = models.CharField(max_length=80)
    viewnum = models.CharField(max_length=11)
    responsenum = models.CharField(max_length=11)
    postdate = models.CharField(max_length=30)
    survey = models.CharField(max_length=500)
    video = models.CharField(max_length=500)
    youtube = models.CharField(max_length=500)
    op_admin = models.CharField(max_length=20)
    op_buy = models.CharField(max_length=20)
    op_free = models.CharField(max_length=20)
    imageA = models.CharField(max_length=500)
    imageB = models.CharField(max_length=500)
    imageC = models.CharField(max_length=500)
    imageD = models.CharField(max_length=500)
    imageE = models.CharField(max_length=500)
    imageF = models.CharField(max_length=500)
    descA = models.CharField(max_length=500)
    descB = models.CharField(max_length=500)
    descC = models.CharField(max_length=500)
    descD = models.CharField(max_length=500)
    descE = models.CharField(max_length=500)
    descF = models.CharField(max_length=500)

class Img(models.Model):
    admin_id = models.CharField(max_length=11)
    image_url = models.CharField(max_length=1000)

















