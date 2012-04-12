from django.core.management.base import BaseCommand, CommandError
from src.users.models import UserProfile
from src.payment_manager.models import PaymentsHistory
from django.conf import settings
from django.utils.translation import ugettext as _


class Command(BaseCommand):

    def handle(self, *args, **options):
		return 'it is working'
		try:
			profiles = UserProfile.objects.all()
		except UserProfile.DoesNotExist:
			raise CommandError(_('no user profiles found'))
        
		for profile in profiles:
			PaymentsHistory.objects.create(user=profile, paid=profile.paid)
			profile.paid = 0
			profile.save()
            