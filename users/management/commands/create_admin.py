from django.core.management.base import BaseCommand , CommandError , CommandParser
from users.models import User

class Command(BaseCommand):
    help = 'Create users admin'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '-u', '--username', type=str ,  help='define username' 
        )
        parser.add_argument(
            '-p', '--password', type=str, help='define password'
        )
        parser.add_argument(
           '-e', '--email', type=str, help='define email'
       )
   
       

    def handle(self, *args: tuple, **options: dict) -> str | None:
        usernameprefix = options.get('username')
        passwordprefix = options.get('password')
        emailprefix = options.get('email')

        if usernameprefix :
            username = usernameprefix
        else :
            username = "admin"    

        if passwordprefix :
            password = passwordprefix
        else :
            password = "admin1234"   

        if emailprefix :
            email = emailprefix
        else :
            email = f'{username}@example.com'            

        try:
            user = User.objects.get(username=username)
            
            if user :
                raise CommandError(f'Username `{username}` already taken.')
        except User.DoesNotExist:
            pass
        try:
            user_email = User.objects.filter(email=email).first()
            if user_email :
                raise CommandError(f'Email `{email}` already taken.')
        except User.DoesNotExist:
            pass    

        User.objects.create_superuser(username=username,password=password,email=email)
        self.stdout.write(self.style.SUCCESS(f'Admin `{username}` successfully created!'))        
        