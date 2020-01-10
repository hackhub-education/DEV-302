from django import forms


class Subscribe(forms.Form):
    Phone = forms.IntegerField()
    status =  forms.IntegerField(default= 0)

    def __str__(self):
        return self.Phone
