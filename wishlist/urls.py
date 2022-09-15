from django.urls import path
from wishlist.views import show_wishlist, show_wishlist_json, show_wishlist_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name="show_wishlist_xml"),
    path('json/', show_wishlist_json, name="show_wishlist_json"),
]
