from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from members.models import Member 

def defaults():
    Member.objects.create(firstname = 'Gaurav', lastname = 'Mahajan', phone=8080251000)
    Member.objects.create(firstname = 'Piyush', lastname = 'Mahajan', phone=8080351000)
    Member.objects.create(firstname = 'Asha', lastname = 'Mahajan', phone=8080151000)
    Member.objects.create(firstname = 'Abhiman', lastname = 'Mahajan', phone=8080123444)

class Command(BaseCommand):
    help = "Add members to the database's Member table"
    
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--firstname', type=str, help='Firstname of the member')
        parser.add_argument('--lastname', type=str, help='Lastname of the member')
        parser.add_argument('--phone', type=str, help='Phone number of the member')
        return super().add_arguments(parser)

    def handle(self, *args, **kwargs) -> str | None:
        
        firstname = kwargs.get('firstname')
        lastname = kwargs.get('lastname')
        phone = kwargs.get('phone')
        
        if firstname and lastname and phone:
            Member.objects.create(firstname=firstname, lastname=lastname, phone=phone)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully added the member: {firstname} {lastname}')
            )
            return
        else:
            defaults()
            self.stdout.write(
                self.style.SUCCESS('Successfully added 4 default members to the Members table')
            )
            return
        