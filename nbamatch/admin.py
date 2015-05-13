from django.contrib import admin
from .models import Post
from .models import Center
from .models import SmallForward
from .models import PointGuard
from .models import PowerForward
from .models import ShootingGuard

# Register your models here.
admin.site.register(Center)
admin.site.register(SmallForward)
admin.site.register(PointGuard)
admin.site.register(PowerForward)
admin.site.register(ShootingGuard)
admin.site.register(Post)
