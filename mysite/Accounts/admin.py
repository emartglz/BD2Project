from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .utils import can_operate

# Create your models here.
class UserAdmin(BaseUserAdmin):
    # staff_fieldsets = (
    #     (None, {'fields': ('username', )}),
    #     ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
    #     # No permissions
    #     (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    #     (_('Groups'), {'fields': ('groups',)}),
    # )
    # staff_readonly_fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined', 'is_staff', 'is_active', 'is_superuser')

    # def get_fieldsets(self, request, obj=None):
    #     if not request.user.is_superuser:
    #         return self.staff_fieldsets
    #     else:
    #         return super(UserAdmin, self).get_fieldsets(request, obj)

    # def get_readonly_fields(self, request, obj=None):
    #     if not request.user.is_superuser:
    #         return self.staff_readonly_fields
    #     else:
    #         return super(UserAdmin, self).get_readonly_fields(request, obj)

    def save_model(self, request, obj, form, change):
        if obj.is_superuser and request.user.username != obj.username:
            print('No se puede editar a un superuser')
        elif request.user.is_superuser:
            super().save_model(request, obj, form, change)
        else:
            request_groups = request.user.groups.all()
            obj_groups = obj.groups.all()

            if can_operate(request_groups, obj_groups):
                super().save_model(request, obj, form, change)
            else:
                print('Permisos insuficientes')
    
    def save_related(self, request, form, formsets, change):
        obj = form.save(commit=False)

        if obj.is_superuser and request.user.username != obj.username:
            print('No se puede editar a un superuser')
        elif request.user.is_superuser:
            form.save_m2m()
        else:
            request_groups = request.user.groups.all()
            obj_groups = obj.groups.all()
            form_groups = form.cleaned_data['groups'].all()

            if can_operate(request_groups, obj_groups) and can_operate(request_groups, form_groups):
                form.save_m2m()
            else:
                print('Permisos insuficientes')
        
        for formset in formsets:
            self.save_formset(request, form, formset, change=change)

    def delete_model(self, request, obj):
        if obj.is_superuser and request.user.username != obj.username:
            print('No se puede eliminar a un superuser')
        elif request.user.is_superuser:
            super().delete_model(request, obj)
        else:
            request_groups = request.user.groups.all()
            obj_groups = obj.groups.all()

            if can_operate(request_groups, obj_groups):
                super().delete_model(request, obj)
            else:
                print('Permisos insuficientes')

        super().delete_model(request, obj)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)