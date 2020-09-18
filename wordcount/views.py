from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, "home.html", {"key" : "This is a wordcount web application. Enter your text here:"})

# def eggs(request):
#     return HttpResponse("<h1>EGGS are rich in protein</h1>")

def count(request):
    text = request.GET["fulltext"]
    list = text.split()
    for i in list:
        if i == "--":
            list.remove("--")
        if i == "-":
            list.remove("-")
    dict = {}
    for i in list:
        if i[-1] == '.' or i[-1] == ',':
            i = i[:-1]
        if i in dict:
            dict[i] += 1
        if i not in dict:
            dict[i] = 1
    sortedwords = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html",{"fulltext": text,"count": len(list),"sorteddict":sortedwords })

def aboutpage(request):
    return render(request, "about.html")
