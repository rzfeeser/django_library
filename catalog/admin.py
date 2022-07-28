from django.contrib import admin
  
# Register your models here.

from .models import Author, Genre, Book, BookInstance

# admin.site.register(Book)           # comment out
# admin.site.register(Author)         # comment out
admin.site.register(Genre)
# admin.site.register(BookInstance)   # comment out


## Below this line is NEW code ##
# Define the admin class
# This is our admin page modification
# this will add the "DATE OF BIRTH" and "DIED"
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]



# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# This class must appear above "BookAdmin"
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

### New lines using the @register decorator
# Register the Admin classes for Book using the decorator
# the decorator does the same thing as admin.site.register()
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
