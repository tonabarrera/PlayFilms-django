from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator


def premium_required(function):
    def wrapper(request, *args, **kwargs):
        user = request.user.userprofile
        if user.type_of_user == 2:
            return HttpResponseRedirect('/user/profile')
        else:
            return function(request, *args, **kwargs)

    return wrapper


class PremiumRequiredMixin(object):
    @method_decorator(premium_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PremiumRequiredMixin, self).dispatch(request, *args, **kwargs)
