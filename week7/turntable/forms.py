from django import forms
 
class start(forms.Form):
   user_phone = forms.IntegerField()
   def __str__(self):
       return self.user_phone

class reward(forms.Form):
    user_phone = forms.IntegerField()
    prize_id = forms.IntegerField()
    