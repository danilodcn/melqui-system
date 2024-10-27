import re

from django.forms import ValidationError


def cell_phone_validator(value):
    """
    Valida um número de telefone. Aceita formatos nacionais e internacionais:
    - Formato internacional com código de país, como: +55 11 91234-5678 ou +1 (123) 456-7890
    - Formato nacional, como: (11) 91234-5678 ou 1234-5678
    - Com ou sem espaços, hífens e parênteses.

    Retorna True se o número é válido, False caso contrário.
    """

    # Regex para números internacionais e nacionais
    expression = re.compile(
        r'^(?:\+?\d{1,3})?[-.\s]?(?:\(?\d{2,3}\)?)?[-.\s]?\d{4,5}[-.\s]?\d{4}$'
    )

    if not bool(expression.match(value)):
        raise ValidationError(
            'Numero de telefone invalido',
            code='invalid',
            params={'value': value},
        )
