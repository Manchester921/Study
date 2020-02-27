import xadmin
from xadmin import views
from app.models import BookCategory, Book

# Register your models here.

class BasicSetting():
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BasicSetting)



class GlobalSettings():
    site_title = '图书管理服务平台'
    site_footer = 'Manchester'

xadmin.site.register(views.CommAdminView, GlobalSettings)

@xadmin.sites.register(BookCategory)
class BookCategoryAdmin():
    list_display = ('id', 'name','user',)
    search_fields = ('name',)
    ordering = ('id',)
    
    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()


class ImageDescAdmin():
    list_display = ('bname', 'image_tag', 'publish', 'author', 'bookcategory', 'create_time')

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()
        
    def queryset(self):
        qs = super(ImageDescAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.sites.site.register(Book, ImageDescAdmin)
