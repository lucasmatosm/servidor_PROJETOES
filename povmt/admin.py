from django.contrib import admin

from povmt.models import Usuario
from povmt.models import Atividade
from povmt.models import Tag
from povmt.models import Tinvestido


admin.site.register(Usuario)
admin.site.register(Tinvestido)
admin.site.register(Tag)
admin.site.register(Atividade)

