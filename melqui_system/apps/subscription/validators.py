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


def validate_cpf(value):
    if not __is_valid_cpf(value):
        raise ValidationError(
            'Numero do CPF invalido', code='invalid', params={'value': value}
        )
    return True


def __is_valid_cpf(cpf):
    # Remover caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)

    # Verificar se o CPF tem 11 dígitos ou se é uma sequência inválida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Validar primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10
    if primeiro_digito != int(cpf[9]):
        return False

    # Validar segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10
    if segundo_digito != int(cpf[10]):
        return False

    return True
