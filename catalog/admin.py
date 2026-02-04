from django.contrib import admin
from .models import Author, Book, Review

# TODO აქ

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','rating')
    search_fields = ('name',)
    ordering = ('-rating',)

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'price')
    search_fields = ('genre', 'published_date')
    autocomplete_fields = ('author',)
    inlines = [ReviewInline]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)