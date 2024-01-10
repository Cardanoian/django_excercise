from django.shortcuts import render
from django.http.response import (
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    HttpResponseRedirect,
)
from django.urls import reverse

# Create your views here.

articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
}


def news_view(request, topic: str):
    print(f"topic: {topic}")
    try:
        result = articles[topic]
        return HttpResponse(result)
    except KeyError:
        # result = f"<h1>No page for {topic}!</h1>"
        # return HttpResponseNotFound(result)
        raise Http404("404 Generic Not Found Error")  # 404.html


# domain.com/first_app/0 ---> domain.com/first_app/sports
def num_page_view(request, num_page: int):
    print(f"num_page: {num_page}")
    topics_list: list[str] = list(articles.keys())  # ["sports", "finance", "politics"]
    topic: str = topics_list[num_page]

    return HttpResponseRedirect(reverse("topic-page", args=[topic]))


# def add_view(request, num1, num2):
#     # domain.com/first_app/3/4 -- > 7
#     add_result = num1 + num2
#     result = f"{num1} + {num2} = {add_result}"
#     return HttpResponse(result)


def simple_view(request):
    return render(request, "first_app/example.html")  # .html
