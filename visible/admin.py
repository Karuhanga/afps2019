from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    exclude = ["slug"]


# Register your models here.


admin.site.register(Post, PostAdmin)
admin.site.register(EventSummaryCard)
admin.site.register(PreviousEdition)
admin.site.register(Partner)
admin.site.register(Ad)
admin.site.register(Schedule)
admin.site.register(ImmigrationGuide)
admin.site.register(TeamMember)
admin.site.register(EventInformation)
