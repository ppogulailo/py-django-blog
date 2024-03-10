from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_filter = ("author", "rating")
    list_display = ("title", "author",)

admin.site.register(Book, BookAdmin)

# Register your models here.
