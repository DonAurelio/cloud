from django.contrib.auth import views


class LoginView(views.LoginView):
    """Deals with user authentication and login processes."""

    # The name of a template to display for the view used to log the user in.
    template_name = 'authentication/login.html'
    # A boolean that controls whether or not authenticated users accessing the 
    # login page will be redirected as if they had just successfully logged in. 
    redirect_authenticated_user = True
    # The redirec URL is defined in settings LOGIN_REDIRECT_URL


class LogoutView(views.LogoutView):
    """Deals with user logout process."""

    # The URL to redirect to after logout. Defaults to settings.LOGOUT_REDIRECT_URL.
    next_page = '/'
