# -*- coding: utf-8 -*-

# Copyright 2013 Dev in Cachu authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import unittest

from django import forms as django_forms
from django.core import management

from .. import forms, models


class FormValidacaoCertificadoTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        management.call_command("loaddata", "certificados.yaml", verbosity=0)

    @classmethod
    def tearDownClass(cls):
        management.call_command("flush", interactive=False, verbosity=0)

    def test_deve_ser_um_form(self):
        assert issubclass(forms.ValidacaoCertificado, django_forms.Form)

    def test_error_css_class_deve_ser_error(self):
        self.assertEqual(u"error", forms.ValidacaoCertificado.error_css_class)

    def test_deve_ter_campo_codigo_certificado(self):
        self.assertIn("codigo", forms.ValidacaoCertificado.base_fields)

    def test_campo_codigo_deve_ser_CharField(self):
        f = forms.ValidacaoCertificado.base_fields["codigo"]
        self.assertIsInstance(f, django_forms.CharField)

    def test_campo_codigo_deve_ter_no_maximo_30_caracteres(self):
        f = forms.ValidacaoCertificado.base_fields["codigo"]
        self.assertEqual(f.max_length, 30)

    def test_obter_certificado_deve_retornar_certificado_pelo_codigo(self):
        form = forms.ValidacaoCertificado({"codigo": "2012080439"})
        esperado = models.Certificado.objects.get(codigo="2012080439")
        obtido = form.obter_certificado()
        self.assertEqual(esperado, obtido)

    def test_obter_certificado_retorna_None_se_o_formulario_for_invalido(self):
        form = forms.ValidacaoCertificado()
        obtido = form.obter_certificado()
        self.assertEqual(None, obtido)

    def test_obter_certificado_retorna_None_se_o_codigo_nao_existir(self):
        form = forms.ValidacaoCertificado({"codigo": "123bla"})
        obtido = form.obter_certificado()
        self.assertEqual(None, obtido)


class FormBuscaCertificadoTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        management.call_command("loaddata", "certificados.yaml", verbosity=0)

    @classmethod
    def tearDownClass(cls):
        management.call_command("flush", interactive=False, verbosity=0)

    def test_deve_ser_um_form(self):
        assert issubclass(forms.BuscarCertificado, django_forms.Form)

    def test_error_css_class_deve_ser_error(self):
        self.assertEqual(u"error", forms.BuscarCertificado.error_css_class)

    def test_deve_ter_campo_codigo_email(self):
        self.assertIn("email", forms.BuscarCertificado.base_fields)

    def test_campo_email_deve_ser_EmailField(self):
        f = forms.BuscarCertificado.base_fields["email"]
        self.assertIsInstance(f, django_forms.EmailField)

    def test_campo_email_deve_ter_no_maximo_100_caracteres(self):
        f = forms.BuscarCertificado.base_fields["email"]
        self.assertEqual(100, f.max_length)

    def test_obter_certificado_deve_retornar_certificado_do_usuario(self):
        form = forms.BuscarCertificado({"email":
                                        "joaozinho@devincachu.com.br"})
        esperado = models.Certificado.objects.get(pk=1)
        obtido = form.obter_certificado()
        self.assertEqual(esperado, obtido)

    def test_obter_certificado_retorna_None_se_o_formulario_for_invalido(self):
        form = forms.BuscarCertificado({"email": "123"})
        obtido = form.obter_certificado()
        self.assertEqual(None, obtido)

    def test_obter_certificado_retorna_None_se_o_usuario_nao_existir(self):
        form = forms.BuscarCertificado({"email":
                                        "mariazinha@devincachu.com.br"})
        obtido = form.obter_certificado()
        self.assertEqual(None, obtido)
