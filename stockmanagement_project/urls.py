from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

API_TITLE = "Stock Management API"
API_DESCRIPTION = "A WEB API for managing stocks."
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    # Built-in Django urls
    path("admin/", admin.site.urls),

    # API
    path("api/v1/", include("api.urls")),

    # Built-in Django Rest url
    path(
        "api-auth/", include("rest_framework.urls")
    ),  # Built-in login & log out feature.
    # Django-rest-auth app url
    path(
        "api/v1/rest-auth/", include("rest_auth.urls")
    ),  # Django-rest-auth. Log in & out, pass reset. Install via pipenv.
    # /login/ page. Also /password/reset/ and /password/reset/confirm/ page.
    path(
        "api/v1/rest-auth/registration/",
        include("rest_auth.registration.urls"),
    ),  # For user registration in API.

    # Schema & Documentation
    path("swagger-docs/", schema_view),
    path(
        "docs/",
        include_docs_urls(title=API_TITLE, description=API_DESCRIPTION),
    ),
]
