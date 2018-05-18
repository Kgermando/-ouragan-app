from django.urls import path
from formation.views import FormationList, OfficeList, InfographieList, ArtList, EnglishList, ProgrammationList

app_name = 'formation'
urlpatterns = [
    path('', FormationList.as_view(), name='formation-list'),
    path('office/', OfficeList.as_view(), name='office-list'),
    path('infographie/', InfographieList.as_view(), name='infographie-list'),
    path('art_culture/', ArtList.as_view(), name='art-list'),
    path('english/', EnglishList.as_view(), name='english-list'),
    path('programmation/', ProgrammationList.as_view(), name='programmation-list'),
]
