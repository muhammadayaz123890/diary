from django.http import HttpResponse , response 
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth

from django.contrib import messages
from django.contrib.auth.decorators import login_required



def Home(request):

    current_profile = None
    all_posts = None
    all_people = None
    

    try:
        current_user = request.user
        current_profile = Profile.objects.get(user=current_user)
        user = request.user
        all_people = Profile.objects.all()

        all_posts = Post.objects.all()[::-1]




    except:
        pass

    return render(request , 'index.html' , {'profile' : current_profile , 'posts' : all_posts , 'all_users' : all_people })

################################################################

def Comments(request):

    post = None
    profile = None
    user = None
    post_id = None
    comments = None


    try:
        
        if request.method == 'GET':
            post_id = request.GET.get('post_id')

        post_id = int(post_id)

        print(post_id)

        post = Post.objects.get(id=post_id)

        profile = Profile.objects.get(user=request.user)


        comments = Comment.objects.filter(post=post)
        print(comments)
    except:
        pass


    return render(request , 'comments.html' , {'comments' : comments , 'post' : post , 'profile' : profile} )

#################################################################

def Post_Comment(request):

    post = None
    post_id = None
    comment_text = None
    user = None
    profile = None

    try:
        if request.method == 'POST':

            comment_text = request.POST.get('comment_text')
            post_id = request.POST.get('post_id')
        
        post_id = int(post_id)

        user = request.user
        post = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        new_comment = Comment.objects.create(
            user=user,
            post=post,
            profile=profile,
            text=comment_text,
        )
        new_comment.save()
    except:
        pass

    return redirect('homepage')

#################################################################

def Like_Post(request):

    post = None
    user = None
    post_id = None
    likers = None
    has_been_liked = False

        
    if request.method == 'POST':



            post_id = request.POST.get('post_id')
        
            print(post_id)
            post_id = int(post_id)

            post = Post.objects.get(id=post_id)
            user = request.user
            
            post_likers = post.likers.all()


            if user not in post_likers:
                post.likers.add(user)
                post.likes += 1
                post.save()

    return redirect('homepage')
    
#################################################################

def Dislike_Post(request):

    post_id = None
    post = None
    user = None

    try:
        if request.method == 'POST':
            post_id = request.POST.get('post_id')
        
        post_id = int(post_id)
        user = request.user
        post = Post.objects.get(id=post_id)

        likers = post.likers.all()

        if user in likers:
            post.likers.remove(user)
            post.likes -= 1
            post.save()
        
    except:
        pass
    
    return redirect('homepage')

    
#################################################################

def Make_Post(request):
    profile = None
    try:
        profile = Profile.objects.get(user=request.user)
        if request.method == 'POST':
            post_img = request.FILES.get('post_img')
        
        new_post = Post.objects.create(user=request.user , profile=profile , img=post_img)
        new_post.save()

        return redirect('homepage')
    except:
        pass

    return render(request , 'make_post.html' , {'profile' : profile})

#################################################################

def Follow(request):

    user = None
    user_id = None
    current_profile = None


    try:
        if request.method == 'POST':
            user_id = request.POST.get('user_id')
        

        user_id = int(user_id)
        current_profile = Profile.objects.get(user=request.user)

        user = User.objects.get(id=user_id)

        if user:
            current_profile.following.add(user)
            current_profile.save()
        
        required_profile = Profile.objects.get(user=user)

        required_profile.followers.add(request.user)
        required_profile.save()

    except:
        pass

    return redirect('homepage')
#################################################################


def UnFollow(request):

    user_id = None
    user = None 
    profile = None
    current_user = None
    current_profile = None

    try:
        if request.method == 'POST':

            user_id = request.POST.get('user_id')
        
        user_id = int(user_id)

        user = User.objects.get(id=user_id)
        
        required_profile = Profile.objects.get(user=user)
        current_user = request.user

        required_profile.followers.remove(current_user)
        required_profile.save()

        current_profile = Profile.objects.get(user=request.user)
        
        current_profile.following.remove(current_user)
        print(f"{request.user} was removed")
        current_profile.save()

    except:
        pass

    return redirect('homepage')



#################################################################

def Other_User(request):
    profile = None

    try:
        profile = Profile.objects.get(user=request.user)

    except:
        pass

    return render(request , 'other_users_profile_page.html' , {'profile' : profile})

#################################################################

@login_required(login_url='sign_up_page')
def Make_Profile(request):
    print('It did happen')
    try:
        
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            contact =request.POST.get('contact_number')
            profile_bio = request.POST.get('profile_bio')
            profile_img = request.FILES.get('profile_img')
            cover_img = request.FILES.get('cover_img')
            
        new_profile = Profile.objects.create(user = request.user , first_name = first_name , last_name=last_name , bios=profile_bio, contact_info=contact , profile_img=profile_img , cover_img=cover_img)
        new_profile.save()
        return redirect('homepage')

    except:
        pass

    return render(request , 'make_profile.html' , )

#################################################################

def Login(request):

    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
        
        all_users = User.objects.all()

    

        for user in all_users:
            
            if user.check_password(password):


                if user.username == username and user.email == email:
                    auth.login(request , user)
                    return redirect('homepage')
            


        
    except:
        pass
    
    return render(request , 'login.html' )

#################################################################

def Register(request):

    try:
        if request.method == 'POST':

            username = request.POST.get('username')
            email = request.POST.get('email_address')
            password = request.POST.get('password')
        
        all_users = User.objects.all()

        for user in all_users:

            if user.username == username:
                messages.info(request , 'USERNAME IS TAKEN')
            elif user.email == email:
                messages.info(request , 'EMAIL ALREADY EXISTS')
            else:
                new_user = User.objects.create(username=username , email=email , password=password)
                
                new_user.save()
                auth.login(request , new_user)

                return redirect('Make_Profile_Page')

    except:
        pass

    return render(request , 'sign_up.html')

#############################################################

def User_Profile(request):
    profile = None
    user_posts = None
    num_of_posts = None
    try:
        user_posts = Post.objects.filter(user=request.user)
        num_of_posts = len(user_posts)
        profile = Profile.objects.get(user=request.user)
    except:
        pass

    return render(request , 'user_profile.html' , {'profile' : profile , 'posts' : user_posts , 'num_of_posts' : num_of_posts})

###############################################################

def Notifications(request):

    return render(request , 'notifications.html' )

###################################################

def Logout(request):

    auth.logout(request)

    return redirect('sign_up_page')

##########################################################
