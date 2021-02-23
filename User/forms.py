# From Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# From Apps
from .models import User


# Customization Forms

class SignUpForm(UserCreationForm):
    use_required_attribute = False

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        exclude = ("password1", "password2")

    def clean_username(self):
        username = self.cleaned_data['username']
        return username


class SignInForm(AuthenticationForm):
    use_required_attribute = False

