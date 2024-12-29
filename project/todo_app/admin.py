from django.contrib import admin
from .models import ToDoList, ToDoItem

class ToDoItemInline(admin.TabularInline):
    model = ToDoItem
    extra = 1

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'color')
    list_editable = ('color',)
    search_fields = ('title',)
    inlines = [ToDoItemInline]

    formfield_overrides = {
        ToDoList._meta.get_field('color'): {'widget': admin.widgets.AdminTextInputWidget(attrs={'type': 'color'})},
    }

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'subtitle', 'list', 'is_checked', 'color')
    list_editable = ('is_checked', 'color')
    search_fields = ('subtitle',)


