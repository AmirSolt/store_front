from django.shortcuts import render




def index(request):
    return render(request, "index.html", {})


# ================ info ================
def explore(request):
    return render(request, "info/explore.html", {})



# ================ auth ================
def choose_username(request):
    return render(request, "auth/choose_username.html", {})


# ================ payment ================
def checkout(request):
    return render(request, "payment/checkout.html", {})



# ================ store ================
def store_page(request, username):
    return render(request, "store/store.html", {"username":username, "test":{"t":4}})

def store_edit(request, username):
    return render(request, "store/edit.html", {})

def store_edit_links(request, username):
    return render(request, "store/links.html", {})



# ================ products ================
def add_products(request, username):
    return render(request, "products/add_products.html", {})