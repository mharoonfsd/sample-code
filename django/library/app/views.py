"""client views for library app."""

from django.views.generic import View
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.db.models import Q
from django.conf import settings
from mimetypes import MimeTypes

from .models import RackModel, BookModel


# Create your views here.
def index(request):
    """Show index page."""
    template = 'pages/index.html'
    context = {}
    response = TemplateResponse(request, template, context)

    return response

def get_favicon(request):
    """Return favicon.ico file."""
    with open(f"{settings.STATIC_ROOT}/favicon.ico", "rb") as file_:
        return HttpResponse(file_.read(), content_type="image/png")

def get_static(request, path):
    """Return static files."""
    with open(f"{settings.STATIC_ROOT}/{path}", "rb") as file_:
        mime = MimeTypes()
        mime_type = mime.guess_type(file_.name)
        return HttpResponse(file_.read(), content_type=mime_type)

class Login(View):
    """Login view for client to login."""

    def get(self, request):
        """Display login form to the user."""
        template = 'pages/login.html'
        context = {}
        response = TemplateResponse(request, template, context)

        return response

    def post(self, request):
        """Validate login info and redirect user."""
        post = request.POST
        user = authenticate(username=post.get('username'), password=post.get('password'))

        if user:
            if user.is_active:
                login(request, user)
                return redirect('rack-list')
            else:
                return redirect('login-disabled')
        else:
            return redirect('login-invalid')


def invalid_login(request):
    """Show if login is invalid."""
    response = HttpResponse()
    response.write("<p>Unable to login with provided credentials.</p>")

    return response


def disabled_login(request):
    """Show if login is deactivated."""
    response = HttpResponse()
    response.write("<p>This user is disabled.</p>")

    return response



def _logout(request):
    """Logout user and redirect to login."""
    logout(request)
    return redirect('login')

@login_required
def rack_list(request):
    """List the available racks."""
    racks = RackModel.objects.all()
    latest_books = BookModel.objects.all().order_by('-added')[:10]

    template = 'pages/rack-list.html'
    context = {"racks": racks, "latest_books": latest_books}
    response = TemplateResponse(request, template, context)

    return response


@login_required
def rack_detail(request, primary_key):
    """List the available books in rack."""
    rack = RackModel.objects.get(id=primary_key)
    racks = RackModel.objects.all().exclude(id=primary_key)
    books_in_rack = BookModel.objects.filter(rack=rack).order_by('-added')

    template = 'pages/rack-detail.html'
    context = {"rack": rack, "racks": racks, "books": books_in_rack}
    response = TemplateResponse(request, template, context)

    return response


@login_required
def book_detail(request, primary_key):
    """Show book detail."""
    book = BookModel.objects.get(id=primary_key)

    template = 'pages/book-detail.html'
    context = {"book": book}
    response = TemplateResponse(request, template, context)

    return response


class SearchList(View):
    """Search View to perform search and show results."""

    @method_decorator(login_required)
    def get(self, request):
        """Show results to the user."""
        query = request.GET.get('query')
        if query:
            results = BookModel.objects.filter(
                Q(title__contains=query) | Q(author__contains=query)
            )
        else:
            results = []

        publish_years = self.get_books_publish_range_years()

        template = 'pages/search-result.html'
        context = {"results": results, "publish_years": publish_years}
        response = TemplateResponse(request, template, context)

        return response

    @method_decorator(login_required)
    def post(self, request):
        """Perform search and redirect to results."""
        post = request.POST
        title = post.get("title") if post.get("title") else "***///**"
        author = post.get("author") if post.get("author") else "***///**"
        published = post.get("published") if post.get("published") else "3000"

        publish_years = self.get_books_publish_range_years()

        if title or author or published:
            results = BookModel.objects.filter(
                Q(title__contains=title) | Q(author__contains=author),
                published__year=published
            )
        else:
            results=[]

        template = 'pages/search-result.html'
        context = {"results": results, "publish_years": publish_years}
        response = TemplateResponse(request, template, context)

        return response

    def get_books_publish_range_years(self):
        """Return range of years books are published in."""
        earliest = BookModel.objects.order_by('published')[0].published.year
        latest = BookModel.objects.order_by('-published')[0].published.year + 1
        publish_years = range(earliest, latest)

        return publish_years
