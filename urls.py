from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from qna import views
import views

from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', views.home),
	(r'^(?P<lid>\d*)/$', views.level),

	#search 
	(r'^(?P<subj_id>\d*)/search/(?P<type>\d*)(?P<tp>\d*)(?P<searchtext>\d*)',views.search),
	(r'^(?P<lid>\d*)/view/(?P<qid>\d*)/$', views.viewquestion),
	
	#study
	(r'^(?P<subj_id>\d*)/study/(?P<tp>\d*)', views.study),	
	
	#statistics
	(r'^(?P<subj_id>\d*)/statistics/(?P<type>\d*)', views.statistics),	
	
	#account
    (r'^accounts/login/$', views.account_login),
    (r'^accounts/logout/$', views.account_logout),
    (r'^accounts/register/$', views.account_register),
    (r'^accounts/activate/$', views.account_activate),
    (r'^accounts/forgot/$', views.account_forgot),
    (r'^accounts/reset/$', views.account_reset),
	(r'^accounts/profile/$', views.profile),
	
	#qna
	url(r'^(?P<subj_id>\d*)/qna/', include('ExamPapers.qna.urls')),
	
	#dajax
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
	
	#comments
	url(r'^comments/', include('django.contrib.comments.urls')),
	
	url(r'^(?P<subj_id>\d*)/test/', views.test),
)

# This is needed to serve static files like images and css
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()