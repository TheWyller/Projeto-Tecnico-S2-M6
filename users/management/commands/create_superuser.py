from django.core.management.base import BaseCommand
from users.models import User

from dotenv import load_dotenv
import os

load_dotenv()


class Command(BaseCommand):
    help = 'Create a ADM user'

    def handle(self, *args, **kwargs):
        User.objects.create_superuser(
                username=os.getenv('ADMIN_USERNAME'),
                password=os.getenv('ADMIN_PASSWORD')
        )
