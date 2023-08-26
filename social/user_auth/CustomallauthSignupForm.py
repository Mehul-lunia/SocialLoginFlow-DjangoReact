from django.forms import Form, ImageField


class SignupForm(Form):
    ProfilePhoto = ImageField(
        label="Profile photo", required=False, help_text="Provide a profile photo"
    )

    def signup(self, request, user):
        user.profilePhoto.save(
            f"{user.username}.png", self.cleaned_data["ProfilePhoto"], save=True
        )
        user.save()
