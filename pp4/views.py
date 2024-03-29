from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "404.html", status=404)


def handler403(request, exception):
    """ Error Handler 403 - Insufficient rights to resource """
    return render(request, "403.html", status=403)


def handler500(request):
    """ Error Handler 500 - Server Error """
    return render(request, "500.html", status=500)
