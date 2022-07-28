"""acme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# imports always go at the top of your code
# however for clarity, they are placed just above where they are
# referenced in this example

# Use include() to add paths from the catalog application
from django.urls import include

urlpatterns += [
    # forwards requests with the pattern `catalog/` to the
    # module catalog.urls (i.e. the relative file
    # catalog/urls.py)
    path('catalog/', include('catalog.urls')),
]

# Use RedirectView to take the new relative URL
# 127.0.0.1:8000 to 127.0.0.1:8000/catalog/
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

# path('/',  ...  )        will produce an error
# use path('', ...  )      to imply "/" and avoid an error
urlpatterns += [
path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

# Enable serving static files
# Use static() to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

