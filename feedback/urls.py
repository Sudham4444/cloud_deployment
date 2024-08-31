from django.contrib import admin
from django.urls import path
from home.views import survey_view, thank_you, survey_results

urlpatterns = [
    path('', survey_view, name='home'),  # Root URL mapped to survey_view
    path('survey_view/', survey_view),
    path('thank-you/', thank_you, name='thank_you'),
    path('results/', survey_results, name='survey_results'),
    path('admin/', admin.site.urls),
]
