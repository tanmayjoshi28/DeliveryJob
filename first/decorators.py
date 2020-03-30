from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def Operator_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/users/loginoperator'):

    actual_decorator = user_passes_test(
        lambda user: user.is_active and user.is_operator,
        redirect_field_name=redirect_field_name,
        login_url=login_url
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def Manager_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/users/loginmanager'):
    '''
    Decorator for views that checks that the logged in user is a teacher,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda user: user.is_active and user.is_manager,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
