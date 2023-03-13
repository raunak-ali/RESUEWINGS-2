from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from User.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import*
from django.contrib import*
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from django.contrib.auth.forms import AuthenticationForm
from  User.Recommendation_system import*
from django.contrib import messages
from django.contrib.auth.models import User
#from Recommendation_system import FORMING_DATAFRAME
from User.Hungarian import*
from itertools import chain

def AlertView(request):
    User=request.user
    Profile=Profiles.objects.get(User=User)
    Posts=Post.objects.filter(User=User).order_by('Timestamp')
    return render(request=request, template_name="users/Alert.html", context={'User':User,'Profile':Profile,'Posts':Posts})

def PostMakeView(request):
    if request.method == "POST":
        Post_Form = PostForm(request.POST, request.FILES)
        Post_Form.User=request.user
        if Post_Form.is_valid():
            PF=Post_Form.save(commit=False)
            PF.User=request.user
            PF.User.User_id=request.user.id
            PF.save()
            messages.success(request, ('Your Post was successfully updated!'))
            return redirect("POSTMAKE")
        else:
            messages.error(request, 'Error saving form')
        return redirect("detail")
    Post_Form = PostForm()
    return render(request=request, template_name="projectfinal/Postmake.html", context={'form':Post_Form})
def index(request):
    Profile=Profiles.objects.filter(Type_of_User='Volunteer').order_by('-Timestamp')
    Blogs=Post.objects.all().order_by('Timestamp')
    return render(request=request, template_name="projectfinal/index.html",context={'Profile':Profile,'Blogs':Blogs})
def home(request):
    if request.method == "POST":
        Profile_form = ProfileForm(request.POST, request.FILES)
        Profile_form.User=request.user
        Profile_form.Paired_with_ID='0'
        if Profile_form.is_valid():
            PF=Profile_form.save(commit=False)
            PF.User=request.user
            PF.User.User_id=request.user.id
            PF.Paired_with_ID='0'
            PF.save()
            messages.success(request, ('Your Profile was successfully updated!'))
            return redirect("detail")
        else:
            messages.error(request, 'Error saving form')
        return redirect("home")
    Profile_form = ProfileForm()
    Profile = Profiles.objects.all()
    return render(request=request, template_name="projectfinal/Request.html", context={'form':Profile_form, 'Profiles':Profile})
    
def serachView(request):
    Search_form= SearchForm(request.POST)
    RESULT=None
    if request.method == "POST":
        if Search_form.is_valid():
            T=Search_form.cleaned_data['Type_of_User']
            TT=Profiles.objects.filter(Type_of_User=T).exclude(Pair_Found=True)
            S=Search_form.cleaned_data['State']
            SS=Profiles.objects.filter(State=S).exclude(Pair_Found=True)
            TD=Search_form.cleaned_data['Type_of_disaster']
            TDD=Profiles.objects.filter(Type_of_disaster=TD).exclude(Pair_Found=True)
            RRE=Search_form.cleaned_data['Rehabilitation_Recovery_estimated_time_in_days']
            RREE=Profiles.objects.filter(Rehabilitation_Recovery_estimated_time_in_days=RRE).exclude(Pair_Found=True)
            SD=Search_form.cleaned_data['Service_Domain']
            SDD=Profiles.objects.filter(Service_Domain=SD).exclude(Pair_Found=True)
            C=Search_form.cleaned_data['Ciity']
            CC=Profiles.objects.filter(Ciity=C).exclude(Pair_Found=True)
            IE=Search_form.cleaned_data['Incentive_Expected']
            IEE=Profiles.objects.filter(Incentive_Expected=IE).exclude(Pair_Found=True)
            E=Search_form.cleaned_data['Experience']
            EE=Profiles.objects.filter(Experience=E).exclude(Pair_Found=True)
            print(EE)
            #print(TT)
            #model_combination = list(chain(TT,SS,TDD,RREE,SDD,CC,IEE,EE))
            model_combination=TT.union(SS).union(TDD).union(RREE).union(SDD).union(CC).union(IEE).union(EE)
            if(model_combination):
                model_combination=model_combination
            else:
                model_combination=None
            print(model_combination)
            return render(request=request, template_name="projectfinal/Searchresults.html", context={'form':Search_form,'Profiles':model_combination})
    else:
        return render(request=request, template_name="projectfinal/Searchresults.html", context={'form':Search_form})
    return redirect("search")

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('detail')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')
    
    else:
        form = AuthenticationForm()
    return render(request, 'projectfinal/login.html', {'form': form})
def BlogView(request):
    Blogs=Post.objects.all().order_by('-Timestamp')
    return render(request, 'projectfinal/blog.html', {'Blogs': Blogs})
def BlogView_single(request,B):
    Blogs=Post.objects.get(id=B)
    ALL_Blogs=Post.objects.all().order_by('-Timestamp')
    print(Blogs.Title)
    return render(request, 'projectfinal/blog-single.html', {'Blogs': Blogs,'ALL_Blogs':ALL_Blogs})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
        else:
            messages.error(request,'THIS USER ALREADY EXISTS,Please select  Another one')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'projectfinal/SignUp.html', context)
# Create your views here.
def OthersProfile(request,P):
    Us=User.objects.get(username=P)
    Profile=Profiles.objects.filter(User=Us).order_by('Timestamp')
    Posts=Post.objects.filter(User=Us).order_by('Timestamp')
    return render(request, 'projectfinal/OtherProfile.html',context={'Profiles':Profile,'Blogs':Posts,'User':Us})

def DetailView(request):
    User=request.user
    if(User.is_authenticated):
        if(Profiles.objects.filter(User=User).exists()):
            Profile=Profiles.objects.filter(User=User).order_by('Timestamp')
            Posts=Post.objects.filter(User=User).order_by('Timestamp')
            print(Profile)
            return render(request, 'projectfinal/volunteer.html',context={'Profiles':Profile,'Blogs':Posts,'User':User})
        else:
            Profile=None
            print("NOPES")
            Posts=Post.objects.filter(User=User).order_by('Timestamp')
            return render(request, 'projectfinal/volunteer.html',context={'Profiles':Profile,'Blogs':Posts,'User':User})
    else:
        return redirect("register")
    return render(request, 'projectfinal/volunteer.html',context={'User':User})


def check_if_Volunteer_or_Request_Present(df):
    if 'Volunteer' in df.values and 'Request' in df.values:
        print("COntinue")
        return True
    else:
        return False

def AssignView(request):
    Query=Profiles.objects.filter(Pair_Found=False).values()
    df = pd.DataFrame(list(Query))
    #df.to_csv('Users.csv')
    df.sort_values(by='Timestamp', inplace = True)
    df['Timestamp'] = df['Timestamp'].apply(lambda a: pd.to_datetime(a).date()) 
    df.to_excel('Users.xlsx')
    df = pd.DataFrame(pd.read_excel("Users.xlsx"))
    print(df.head())
    print(df.info())
    original = pd.DataFrame(pd.read_excel("Users.xlsx"))
    original.head()
    #FIRST CHECK IF  ENOUGH RECORDS  ARE  PRESENT IN THE DATAFRAME
    if 'Volunteer' in df.values and 'Request' in df.values:
        similarities=SIMILARITY_VECTOR(df)#Makig Our Similarity Matrix
        #print(similarities)
        df=FORMING_DATAFRAME(similarities,df,original)# Our final dataframe which will be used for assignment
        print(df)
        Assigned={}# The dictionary which will store all assignments
        Transform(df,Assigned)#Sending it to tthe  Hungarian Algorithms
        #Making a sperate list from our dicttionary
        Requests=Assigned.keys()
        Volunteers=Assigned.values()
        print(Volunteers)
        #print(Requests)
        df_final = pd.DataFrame(pd.read_excel("Users.xlsx"))
        Request=[]
        Volunteer=[]
        #Getting names per index of our keys
        for v in Volunteers:
            Volunteer.append(v)
        for r in Requests:
            Request.append(df_final.iloc[r]['Name'])
        print(Request)
        print(df)
        UPDATE_DB_VIEW(Request,Volunteer)#Update the APir found and Pair_Found with part of thier profie
        return redirect("detail")
    else:
        print("NO MATCH FOUND")
    return redirect("detail")

def  UPDATE_DB_VIEW(Request,Volunteer):
    n=len(Request)
    v=len(Volunteer)
    
    if(v<1 or n<1):
        return
    else:
        for r in range(0,n):
            REQ=Request[r]
            VOL=Volunteer[r]
            RR=Profiles.objects.get(Name=REQ)
            VOL=Profiles.objects.get(Name=VOL)
            RR.Pair_Found=True
            VOL.Pair_Found=True
            RR.Paired_with=VOL.Name
            RR.Paired_with_ID=VOL.id
            VOL.Paired_with=RR.Name
            VOL.Paired_with_ID=RR.id
            RR.save()
            VOL.save()
            print(RR)
            print(VOL)



