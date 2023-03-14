from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from User.models import*


state=(
    ('Assam','Assam'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
    ('',''),
)
city=(
    ('Amaravati','Amaravati'),
    ('Itanagar','Itanagar'),
    ('Dispur','Dispur'),
    ('Raipur','Raipur'),
    ('Panaji','Panaji'),
    ('Gandhinagar','Gandhinagar'),
    ('Chandigarh','Chandigarh'),
    ('Shimla','Shimla'),
    ('Ranchi','Ranchi'),
    ('Bengaluru','Bengaluru'),
    ('Patna','Patna'),
    ('Thiruvananthapuram','Thiruvananthapuram'),
    ('Bhopal','Bhopal'),
    ('Mumbai','Mumbai'),
    ('Imphal','Imphal'),
    ('Shillong','Shillong'),
    ('Aizawl','Aizawl'),
    ('Bhubaneswar','Bhubaneswar'),
    ('Kohima','Kohima'),
    ('Chandigarh','Chandigarh'),
    ('Jaipur','Jaipur'),
    ('Gangtok','Gangtok'),
    ('Chennai','Chennai'),
    ('Hyderabad','Hyderabad'),
    ('Lucknow','Lucknow'),
    ('',''),
)
type_of_user=(
    ('Volunteer','Volunteer'),
    ('Request','Request'),

)
type_of_disaster=(
    ('Agricultural diseases & pests','Agricultural diseases & pests'),
    ('Damaging Winds','Damaging Winds'),
    ('Drought and water shortage','Drought and water shortage'),
    ('Earthquakes','Earthquakes'),
    ('Emergency diseases (pandemic influenza)','Emergency diseases (pandemic influenza)'),
    ('Extreme heat','Extreme heat'),
    ('Floods and flash floods','Floods and flash floods'),
    ('Hail','Hail'),
    ('','')


)
service_domain=(

    ('Financial Aid','Financial Aid'),
    ('Medical Aid','Medical Aid'),
    ('Rehabilitation(Shelter) Aid','Rehabilitation(Shelter) Aid'),
    ('Resources Aid(Food,and other amenities)','Resources Aid(Food,and other amenities)'),
    ('Man-Power','Man-Power'),
    ('','')
)
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('Title','Description','Tags','Image')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('Name','Type_of_User','Email', 'Phone', 'Ciity', 'State', 'ID_Proof','Skill_certificates','Incentive_Expected','Experience','Type_of_disaster','Rehabilitation_Recovery_estimated_time_in_days','Service_Domain')
class SearchForm(forms.Form):
    Type_of_User=forms.ChoiceField(choices=type_of_user)
    Type_of_disaster=forms.ChoiceField(choices=type_of_disaster,required=False)
    Rehabilitation_Recovery_estimated_time_in_days=forms.IntegerField(required=False)
    Service_Domain=forms.ChoiceField(choices=service_domain,required=False)
    State=forms.ChoiceField(choices=state,required=False)
    Ciity=forms.ChoiceField(choices=city,required=False)
    Incentive_Expected=forms.IntegerField(required=False)
    Experience=forms.IntegerField(required=False)