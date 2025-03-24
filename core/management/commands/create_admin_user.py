from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        from django.contrib.auth.models import User
        from decouple import config
        
        username = config('ADMIN_USERNAME', default='admin')
        email = config('ADMIN_EMAIL', default=None)
        password = config('ADMIN_PASSWORD', default='admin')

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'User {username} already exists!'))
            return

        User.objects.create_superuser(username, email, password)
        self.stdout.write(self.style.SUCCESS(f'User {username} created successfully!'))

        