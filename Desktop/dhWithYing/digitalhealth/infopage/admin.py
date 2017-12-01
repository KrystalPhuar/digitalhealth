# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Approach
from .models import Specialty
from .models import Entry
from .models import Bsi, Bsm, Bsds, Bshf, Cci, Ccm, Ccds, Cchf, Chi, Chm, Chds, Chhf, Mi, Mm, Mds, Mhf

admin.site.register(Approach)
admin.site.register(Specialty)
admin.site.register(Entry)
admin.site.register(Bsi)
admin.site.register(Bsm)
admin.site.register(Bsds)
admin.site.register(Bshf)
admin.site.register(Cci)
admin.site.register(Ccm)
admin.site.register(Ccds)
admin.site.register(Cchf)
admin.site.register(Chi)
admin.site.register(Chm)
admin.site.register(Chds)
admin.site.register(Chhf)
admin.site.register(Mi)
admin.site.register(Mm)
admin.site.register(Mds)
admin.site.register(Mhf)
