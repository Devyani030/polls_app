from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path ("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("question/", views.get_name, name="question"),
    path("<int:pk>/delete/" , views.delete_question, name="delete")

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)