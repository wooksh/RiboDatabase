from django.conf.urls import url
from . import views

app_name = 'database'

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^browser/ligand/$', views.ligand_browser, name='ligand_browser'),
    url(r'^browser/ligand/(?P<ligand_name>[A-Za-z]+)/$', views.ligand_details, name='ligand_details'),
    url(r'^browser/organism/$', views.organism_browser, name='organism_browser'),
    url(r'^browser/organism/(?P<organism_name>([-\w\s.()])+)/$', views.organism_details, name='organism_details'),
    url(r'^browser/class/family$', views.class_family_browser, name="class_family_browser"),
    url(r'^browser/class/family/(?P<family>([A-Za-z])+)/$', views.class_family_details, name='class_family_details'),
    url(r'^searcher/$', views.searcher, name='searcher'),
    # url(r'^searcher/results/', views.get_records_by_ajax),
    # url(r'^search/record/(?P<riboswitch_name>([A-Za-z])+/$', views.search, name='search'),
]