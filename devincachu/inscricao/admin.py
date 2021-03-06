# -*- coding: utf-8 -*-

# Copyright 2013 Dev in Cachu authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from django.contrib import admin

from . import models


class CheckoutAdmin(admin.ModelAdmin):
    list_display = (u"codigo", u"nome_participante", u"email_participante",)
    search_fields = (u"codigo", u"participante__nome", u"participante__email",)

    def has_add_permission(self, *args, **kwargs):
        return False

    def nome_participante(self, chk):
        return chk.participante.nome

    def email_participante(self, chk):
        return chk.participante.email


class ConfiguracaoAdmin(admin.ModelAdmin):

    def has_add_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False


def confirmar_presenca(modeladmin, request, queryset):
    queryset.update(presente=True)
confirmar_presenca.short_description = u"Confirmar presença"


class ParticipanteAdmin(admin.ModelAdmin):
    list_display = (u"nome", u"cidade", u"email", u"empresa",
                    u"instituicao_ensino", u"presente",
                    u"status")
    list_filter = (u"sexo", u"status", u"presente")
    search_fields = (u"nome", u"email",)
    actions = (confirmar_presenca,)

try:
    admin.site.register(models.Checkout, CheckoutAdmin)
    admin.site.register(models.Configuracao, ConfiguracaoAdmin)
    admin.site.register(models.Participante, ParticipanteAdmin)
except admin.sites.AlreadyRegistered:
    pass
