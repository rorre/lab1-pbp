from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core import serializers

from wishlist.models import BarangWishlist


def show_wishlist(request: HttpRequest):
    items = BarangWishlist.objects.all()
    ctx = {"list_barang": items, "nama": "Ren"}
    return render(request, "wishlist.html", ctx)

def show_wishlist_xml(request: HttpRequest):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


