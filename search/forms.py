from django import forms

class SearchForm(forms.Form):
    name = forms.CharField(
        label='アーティスト名',
        max_length=255,
        required=True,
        widget=forms.TextInput()
    )
    
class InitialForm(forms.Form):
    initial = forms.ChoiceField(choices = [
        (0, "A"), 
        (1, "B"),
        (2,"C"),
        (3,"D"), 
        (4,"E"), 
        (5,"F"),
        (6,"G"), 
        (7,"H"), 
        (8,"I"), 
        (9,"J"), 
        (10,"K"), 
        (11,"L"), 
        (12,"M"), 
        (13,"N"), 
        (14,"O"), 
        (15,"P"), 
        (16,"Q"), 
        (17,"R"), 
        (18,"S"), 
        (19,"T"), 
        (20,"U"), 
        (21,"V"), 
        (22,"W"), 
        (23,"X"),
        (24,"X"), 
        (25,"Y"), 
        (26,"Z")
    ])
    choices=[
        (0,"A"),
        (1,"B"), 
        (2,"C"),
        (3,"D"), 
        (4,"E"), 
        (5,"F"),
        (6,"G"), 
        (7,"H"), 
        (8,"I"), 
        (9,"J"), 
        (10,"K"), 
        (11,"L"), 
        (12,"M"), 
        (13,"N"), 
        (14,"O"), 
        (15,"P"), 
        (16,"Q"), 
        (17,"R"), 
        (18,"S"), 
        (19,"T"), 
        (20,"U"), 
        (21,"V"), 
        (22,"W"), 
        (23,"X"),
        (24,"X"), 
        (25,"Y"), 
        (26,"Z")
    ]
