from django.contrib import admin
from django.urls import path, include

from .views import PrimaryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PrimaryView.as_view(), name="primary"),
    path('blog/', include('blog.urls'))
]
