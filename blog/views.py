from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
import logging

# Create a logger for this app
logger = logging.getLogger(__name__)

# ===========================
# Index view with caching
# ===========================
@cache_page(300)
def index(request):
    from django.http import HttpResponse
    return HttpResponse(str(request.user).encode("ascii"))
    posts = Post.objects.filter(published_at__lte=timezone.now())
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html", {"posts": posts})
# ===========================
# Question 5 view
# ===========================
def question5(request):
    logger.debug("A Debug Message")
    logger.warning("A Warning Message")
    logger.critical("A Critical Message")
    return HttpResponse("Hello World")
