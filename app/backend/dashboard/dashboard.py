from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.logging.logging import Logger

logger = Logger("app/logging/app.log")

@login_required
def dashboard(request):
    logger.log(f"User {request.user} viewed dashboard.")
    return render(request, "dashboard.html")