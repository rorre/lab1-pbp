from django.http import HttpRequest
from django.shortcuts import render

from wishlist.models import BarangWishlist


def show_wishlist(request: HttpRequest):
    items = BarangWishlist.objects.all()
    ctx = {"list_barang": items, "nama": "Ren"}
    return render(request, "wishlist.html", ctx)
