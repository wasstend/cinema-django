from django.contrib import admin
from .models import Hall, Movie, Session, Ticket

admin.site.register(Hall)
admin.site.register(Movie)
admin.site.register(Session)
admin.site.register(Ticket)
