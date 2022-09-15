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
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_wishlist_json(request: HttpRequest):
    data = BarangWishlist.objects.all()
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_id_json(request: HttpRequest, id: int):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_id_xml(request: HttpRequest, id: int):
    data = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )
