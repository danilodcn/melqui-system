from typing import TYPE_CHECKING

from django.core.validators import validate_email
from django.db import models

if TYPE_CHECKING:
    from django.contrib.auth.models import User   # noqa

from melqui_system.apps.subscription.validators import cell_phone_validator


class Subscription(models.Model):
    cpf = models.CharField('CPF', max_length=20)
    full_name = models.CharField('Nome Completo', max_length=255)
    email = models.CharField(
        'Email', validators=[validate_email], null=True, blank=True
    )

    cell_phone = models.CharField(
        'Numero de Telefone (WhatApp)',
        max_length=32,
        validators=[cell_phone_validator],
    )

    birthday = models.DateField('Data de aniversario')

    indicated_by = models.ForeignKey(
        'Subscription',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='indications',
        verbose_name='Indicado por',
    )  # type: Subscription | None

    created_at = models.DateTimeField(
        'Data de criação', editable=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Data de atualização', editable=False, auto_now=True
    )

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        ordering = ('pk',)

    def __str__(self) -> str:
        return f'{self.pk} - {self.full_name}'


class SubscriptionAddress(models.Model):
    class StatesChoices(models.TextChoices):
        AC = 'AC', 'Acre'
        AL = 'AL', 'Alagoas'
        AP = 'AP', 'Amapá'
        AM = 'AM', 'Amazonas'
        BA = 'BA', 'Bahia'
        CE = 'CE', 'Ceará'
        DF = 'DF', 'Distrito Federal'
        ES = 'ES', 'Espírito Santo'
        GO = 'GO', 'Goiás'
        MA = 'MA', 'Maranhão'
        MT = 'MT', 'Mato Grosso'
        MS = 'MS', 'Mato Grosso do Sul'
        MG = 'MG', 'Minas Gerais'
        PA = 'PA', 'Pará'
        PB = 'PB', 'Paraíba'
        PR = 'PR', 'Paraná'
        PE = 'PE', 'Pernambuco'
        PI = 'PI', 'Piauí'
        RJ = 'RJ', 'Rio de Janeiro'
        RN = 'RN', 'Rio Grande do Norte'
        RS = 'RS', 'Rio Grande do Sul'
        RO = 'RO', 'Rondônia'
        RR = 'RR', 'Roraima'
        SC = 'SC', 'Santa Catarina'
        SP = 'SP', 'São Paulo'
        SE = 'SE', 'Sergipe'
        TO = 'TO', 'Tocantins'

    subscription = models.OneToOneField(
        Subscription,
        on_delete=models.PROTECT,
        verbose_name='inscrição',
        related_name='address',
    )

    city = models.CharField('Cidade')
    state = models.CharField('Cidade', choices=StatesChoices.choices)
    neighborhood = models.CharField('Bairro')
    street = models.CharField('Rua')
    number = models.CharField('Numero')

    created_at = models.DateTimeField(
        'Data de criação', editable=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Data de atualização', editable=False, auto_now=True
    )

    class Meta:
        verbose_name = 'Endereço'

    def __str__(self) -> str:
        return f'{self.street} - {self.city}/{self.state}'


class SubscriptionReview(models.Model):
    subscription = models.OneToOneField(
        Subscription, on_delete=models.PROTECT, related_name='review'
    )
    reviewed_by = models.ForeignKey(
        'auth.user', on_delete=models.PROTECT
    )   # type: User
    reviewed_date = models.DateTimeField('Data de aprovação')
    approved = models.BooleanField('Aprovado')

    comments = models.TextField('Comentários', default='')

    created_at = models.DateTimeField(
        'Data de criação', editable=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Data de atualização', editable=False, auto_now=True
    )

    class Meta:
        verbose_name = 'Revisão'
        verbose_name_plural = 'Revisões'
