from django import forms


class Subscribe(forms.Form):
    Phone = forms.EmailField()

    def __str__(self):
        return self.Phone
