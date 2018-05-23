from django.core.exceptions import PermissionDenied


def is_customer(function):
    def wrap(request, *args, **kwargs):
        if request.user.user_type == 1 or request.user.is_admin:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def is_restaurant(function):
    def wrap(request, *args, **kwargs):
        if request.user.user_type == 2 or request.user.is_admin:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def is_delivery(function):
    def wrap(request, *args, **kwargs):
        if request.user.user_type == 3 or request.user.is_admin:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def is_admin(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
