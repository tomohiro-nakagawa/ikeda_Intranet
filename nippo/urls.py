from django.urls import path,include
from .views import (
                    NippoListView ,
                    NippoDetailView, 
                    NippoCreateModelFormView, 
                    NippoUpdateModelFormView,
                    NippoDeleteView,
                    Nippo0View,
                    Nippo11View,
                    Nippo12View,
                    Nippo13View,
                    Nippo14View,
                    Nippo15View,
                    Nippo21View,
                    Nippo22View,
                    Nippo23View,
                    Nippo3View,
                    Nippo4View,
                  )

urlpatterns = [
  path("", NippoListView.as_view(), name="nippo-list"),
  path("detail/<slug:slug>/", NippoDetailView.as_view(), name="nippo-detail"),
  path("create/", NippoCreateModelFormView.as_view(), name="nippo-create"),
  path("update/<slug:slug>/", NippoUpdateModelFormView.as_view(), name="nippo-update"),
  path("delete/<slug:slug>/", NippoDeleteView.as_view(), name="nippo-delete"),
  path("0/", Nippo0View, name="nippo-0"),
  path("1-1/", Nippo11View, name="nippo-1-1"),
  path("1-2/", Nippo12View, name="nippo-1-2"),
  path("1-3/", Nippo13View, name="nippo-1-3"),
  path("1-4/", Nippo14View, name="nippo-1-4"),
  path("1-5/", Nippo15View, name="nippo-1-5"),
  path("2-1/", Nippo21View, name="nippo-2-1"),
  path("2-2/", Nippo22View, name="nippo-2-2"),
  path("2-3/", Nippo23View, name="nippo-2-3"),
  path("3/", Nippo3View, name="nippo-3"),
  path("4/", Nippo4View, name="nippo-4"),


  
]