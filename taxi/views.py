from django.shortcuts import render


def taxi_list(request):
    return render(request, "taxi/list.html")
