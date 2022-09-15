from django.urls import path
from wishlist.views import show_id_json, show_id_xml, show_wishlist, show_wishlist_json, show_wishlist_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name="show_wishlist_xml"),
    path('json/', show_wishlist_json, name="show_wishlist_json"),
    path('xml/<int:id>', show_id_xml, name="show_id_xml"),
    path('json/<int:id>', show_id_json, name="show_id_json"),
]
