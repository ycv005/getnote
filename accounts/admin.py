from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# A form for creating new users.
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    # (https://stackoverflow.com/questions/39476334/why-class-meta-is-necessary-while-creating-a-model-form)
    class Meta: #class Meta sets the what model and field this form will use
        model = User
        fields = ('email','name')

    # clean_attribute is used to provide validation
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    # A form for updating users.
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'active', 'admin','staff')

    def clean_password(self):
        return self.initial["password"]
    
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'admin')
    list_filter = ('admin','name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email','name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
# since we are not using django built-in permission , thus unregistering the Group Model
admin.site.unregister(Group)