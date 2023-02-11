from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            form.cleaned_data
            raise ValidationError('Основным может быть только один раздел!')
        return super().clean() 


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_view = ['name']


