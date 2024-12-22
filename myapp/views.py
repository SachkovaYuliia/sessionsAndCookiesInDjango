from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        if name and age:
            response = HttpResponseRedirect("/welcome/")
            response.set_cookie("name", name, max_age=60 * 15)

            """Use Django's session backend to store data in the database"""
            request.session["age"] = age
            return response
        else:
            return render(request, "login.html", {"error": "Please provide both name and age."})

    return render(request, "login.html")

def welcome(request):
    name = request.COOKIES.get("name")
    age = request.session.get("age")

    if not name or not age:
        return redirect("/login/")

    """Extend cookie expiration if user is active"""
    response = render(request, "welcome.html", {"name": name, "age": age})
    response.set_cookie("name", name, max_age=60 * 60 * 24 * 7)

    return response

def logout(request):
    response = render(request, "logout.html")
    response.delete_cookie("name")

    """Clear session data from the database """
    request.session.flush()
    return response