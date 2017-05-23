from django.http import HttpResponseRedirect


def premium_required(function):
    def wrapper(request, *args, **kwargs):
        user = request.user.userprofile
        if user.type_of_user == 2:
            return HttpResponseRedirect('/user/profile')
        else:
            return function(request, *args, **kwargs)
    return wrapper