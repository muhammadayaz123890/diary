from django.contrib import admin

from Src_App.models import Comment, Post, Profile



class Profile_Admin(admin.ModelAdmin):

    list_display = ['first_name' , 'last_name' , ]
    readonly_fields = ['followers' , 'following' , 'first_name' , 'last_name' , 'profile_img' , 'cover_img' , 'user'  , 'contact_info' , 'bios']

class Post_Admin(admin.ModelAdmin):

    list_display = ['user' ]
    readonly_fields = ['likers' , 'user' , 'profile' , 'likes' , 'img' ]

class Comment_Admin(admin.ModelAdmin):

    list_display = ['user' , 'text']
    readonly_fields = ['user' , 'text' , 'profile' , 'post' ]


admin.site.register(Comment , Comment_Admin)
admin.site.register(Profile , Profile_Admin)

admin.site.register(Post , Post_Admin)
