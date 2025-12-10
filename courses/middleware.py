import datetime
from django.conf import settings
from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin

class AutoLogoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            
            return

        # Sessiya muddati (soniya bilan)
        max_idle_time = getattr(settings, 'AUTO_LOGOUT_DELAY', 300)  

        
        last_activity = request.session.get('last_activity')

        now = datetime.datetime.now().timestamp()

        if last_activity and now - last_activity > max_idle_time:
            auth.logout(request)
            request.session.flush()
        else:
            request.session['last_activity'] = now
