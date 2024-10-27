from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms

from melqui_system.apps.subscription.models import Subscription


class RegistrationSubscriptionForm(forms.ModelForm):
    birthday = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder': 'dd/mm/aaaa'},
        ),
        label='Data de Nascimento',
    )

    class Meta:
        model = Subscription
        exclude = (
            'created_at',
            'updated_at',
            'indicated_by',
        )

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('full_name', css_class='form-group col-md-6 mb-0'),
                Column('cpf', css_class='form-group col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('titulo', css_class='form-group col-md-6 mb-0'),
                Column('rg', css_class='form-group col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('cell_phone', css_class='form-group col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('birthday', css_class='form-group col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('cep', css_class='form-group col-md-5 mb-0'),
                Column('state', css_class='form-group col-md-3 mb-0'),
                Column('city', css_class='form-group col-md-4 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('neighborhood', css_class='form-group col-md-5 mb-0'),
                Column('street', css_class='form-group col-md-5 mb-0'),
                Column('number', css_class='form-group col-md-2 mb-0'),
                css_class='form-row',
            ),
            Submit('submit', 'Cadastrar'),
        )
