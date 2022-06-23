from django.contrib import admin
from .models import Noboro
from .models import NoboroContent
from .models import Prefecture
from .models import Mountain

# Register your models here.
admin.site.register(Noboro)
admin.site.register(NoboroContent)
admin.site.register(Prefecture)
admin.site.register(Mountain)
