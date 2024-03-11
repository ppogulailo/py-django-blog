from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=10, required=False, error_messages={
        "required": "Your name is required",
        "max_length": "Please enter a shorter name"
    })
