from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.views import View

# Base class for pages displaying posts
class BasePageView(View):
    """
    A base view for pages that display posts with pagination.
    """
    template_name = None

    def get(self, request):
        posts = Post.objects.all().order_by('date_created')  # Ensure consistent ordering
        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {"posts": page_obj}
        return render(request, self.template_name, context)

# Homepage view
class HomePageView(BasePageView):
    template_name = "index.html"

# About page view (inherits from BasePageView for consistency)
class AboutPageView(BasePageView):
    template_name = "about.html"

# Greeting view
def greet(request: HttpRequest):
    """
    Returns a greeting message based on the 'name' query parameter.
    """
    name = request.GET.get("name") or "world"
    return HttpResponse(f"Hello {name}")

# Services page view
def services(request):
    context = {"title": "Services Page"}
    return render(request, 'services.html', context)

# Fetch all posts
def return_all_posts(request: HttpRequest):
    posts = Post.objects.all()  # Fetch all posts from the database
    return HttpResponse(str(posts))

# Fetch a single post by ID
def return_one_post(request: HttpRequest, post_id):
    post = get_object_or_404(Post, id=post_id)  # Retrieve post by ID or return 404
    return HttpResponse(str(post))

# View for creating a post
@method_decorator(login_required, name='dispatch')
class CreatePostView(View):
    """
    Handles post creation, requiring user authentication.
    """
    template_name = 'createpost.html'
    form_class = PostCreationForm
    initial_values = {"key": "value"}

    def get(self, request):
        form = self.form_class(initial=self.initial_values)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_home')  # Redirect to the homepage
        context = {"form": form}
        return render(request, self.template_name, context)

# View for displaying a single post in detail
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  # Fetch the post or return 404
    context = {'post': post}
    return render(request, 'post_detail.html', context)

# View for updating a post
def update_post(request, post_id):
    """
    Handles updating an existing post.
    """
    post_to_update = get_object_or_404(Post, pk=post_id)
    form = PostCreationForm(instance=post_to_update)

    if request.method == 'POST':
        form = PostCreationForm(instance=post_to_update, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_home')  # Redirect to the homepage

    context = {'form': form}
    return render(request, 'update.html', context)
