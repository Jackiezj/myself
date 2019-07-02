from django.conf.urls import url

from verifications import views

urlpatterns = [
    url(r'^image_codes/(?P<image_code_id>[\w-]+)/$', views.ImageCode.as_view()),
    url(r'^sms_codes/(?P<mobile>1[3-9]\d{9})/$', views.SMSCode.as_view())
]
