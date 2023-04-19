from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Profile


class Command(BaseCommand):
    help = "Create profiles for all existing users"

    def handle(self, *args, **options):
        users = User.objects.all()

        for user in users:
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created profile for user {user.username}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Profile already exists for user {user.username}"
                    )
                )
