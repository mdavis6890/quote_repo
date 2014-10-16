from django.conf.urls import patterns, include, url
from django.conf.urls import url, include
from rest_framework import routers
from quote_app import views

router = routers.DefaultRouter()
router.register(r'vendors', views.VendorViewSet)
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	#url(r'^$', 'quote_app.views.index', name='index'),
	# url(r'^reman/', include('reman.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	#(r'^api/', include(v1_api.urls)),
	url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
