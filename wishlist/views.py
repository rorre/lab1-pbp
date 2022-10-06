import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from wishlist.models import BarangWishlist


@login_required(login_url="/wishlist/login")
def show_wishlist(request: HttpRequest):
    items = BarangWishlist.objects.all()
    ctx = {
        "list_barang": items,
        "nama": "Ren",
        "last_login": request.COOKIES["last_login"],
    }
    return render(request, "wishlist.html", ctx)


@login_required(login_url="/wishlist/login")
def show_ajax(request: HttpRequest):
    ctx = {
        "nama": "Ren",
        "last_login": request.COOKIES["last_login"],
    }
    return render(request, "wishlist_ajax.html", ctx)


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


def create_wishlist(request: HttpRequest):
    if request.method == "POST":
        nama_barang = request.POST.get("nama_barang")
        harga_barang = request.POST.get("harga_barang")
        deskripsi = request.POST.get("deskripsi")

        new_barang = BarangWishlist(
            nama_barang=nama_barang,
            harga_barang=harga_barang,
            deskripsi=deskripsi,
        )
        new_barang.save()
        return HttpResponse(
            serializers.serialize("json", [new_barang]),
            content_type="application/json",
        )

    return HttpResponse("Invalid method", status_code=405)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah berhasil dibuat!")
            return redirect("wishlist:login")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, "Username atau Password salah!")
    context = {}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("wishlist:login"))
    response.delete_cookie("last_login")
    return response
