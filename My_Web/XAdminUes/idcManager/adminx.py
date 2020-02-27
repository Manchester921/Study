import xadmin
from xadmin import views
from idcManager.models import IDC, ImageDesc

# Register your models here.

class BasicSetting():
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BasicSetting)



class GlobalSettings():
    site_title = 'Manchester管理服务器平台'
    site_footer = 'Manchester'

xadmin.site.register(views.CommAdminView, GlobalSettings)

@xadmin.sites.register(IDC)
class IDCAdmin():
    list_display = ('name', 'desc', 'phone', 'address', 'create_time', 'user')
    search_fields = ('name',)
    ordering = ('id',)

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()
    
    list_per_page = 3
    list_filter = ('name',)


# @xadmin.sites.register(ImageDesc)
class ImageDescAdmin():
    list_display = ('name', 'image_tag', 'user')

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()
        
    def queryset(self):
        qs = super(ImageDescAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.sites.site.register(ImageDesc, ImageDescAdmin)
