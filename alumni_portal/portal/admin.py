from django.contrib import admin

from portal.models import Batch, Country, Department, District, ExperienceDetail, MentorPost, MentorPostResponse, MentorResponseMessage, Post, PostEducationDetail, PostResponse, ResponseMessage, State, Tag, User,Authentication,StudDetails,Finance

# Register your models here.

admin.site.register(User)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Batch)
admin.site.register(Department)
admin.site.register(PostEducationDetail)
admin.site.register(ExperienceDetail)
admin.site.register(Post)
admin.site.register(PostResponse)
admin.site.register(ResponseMessage)
admin.site.register(MentorPost)
admin.site.register(MentorPostResponse)
admin.site.register(MentorResponseMessage)
admin.site.register(Tag) 
admin.site.register(Authentication)
admin.site.register(StudDetails)
admin.site.register(Finance)