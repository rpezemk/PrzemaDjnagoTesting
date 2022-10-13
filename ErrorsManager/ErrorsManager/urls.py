"""ErrorsManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ErrorBrowser.views import doc_view, browseFilters_view, doc_view2

urlpatterns = [
    path('doc2/', doc_view2, name='doc2'),
    path('doc/', doc_view, name='doc'),
    path('browseFilters/', browseFilters_view, name='browseFilters'),
    path('home/', doc_view, name='home'),
    path('admin/', admin.site.urls),
]
