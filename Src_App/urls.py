from django.urls import path
from . import views



urlpatterns = [

    path('' , views.Home , name='homepage'),
    
    path('comments/' , views.Comments , name='comments_page'),
    
    path('post_comment/' , views.Post_Comment , name='comment_page'),
    
    path('make_post/' , views.Make_Post , name='Post_Making_page'),
    
    path('make_profile/' , views.Make_Profile , name='Make_Profile_Page'),
    
    path('login/' , views.Login , name='login_page'),
    
    path('sign_up/' , views.Register , name='sign_up_page'),
    
    path('logout/' , views.Logout , name='logout_function'),

    path('user_profile/' , views.User_Profile , name='user_profile_page'),
    
    path('user_required/' , views.Other_User , name='other_user_profile_page'),
    
    path('like/' , views.Like_Post , name='like_function'),
    
    path('dislike/' , views.Dislike_Post , name='dislike_function'),

    path('notifications/' , views.Notifications , name='notifications_page'),

    path('follow/' , views.Follow , name='follow_functionality'),

    path('unfollow/' , views.UnFollow , name='unfollow_function'),

]