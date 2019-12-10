from django.contrib import admin
from .models import Blogpost, Books, Contact, DeliveryDetails

admin.site.register(Blogpost)
admin.site.register(Books)
admin.site.register(Contact)
admin.site.register(DeliveryDetails)
