from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import Case, DecimalField, F, When

from students.models import DummyTable


class Command(BaseCommand):
    help = "Run bulk update queries on DummyTable"

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            DummyTable.objects.update(
                salary=Case(
                    When(department_name="Engineering", then=F("salary") * 2.25),
                    When(department_name="Sales", then=F("salary") * 1.10),
                    When(department_name="HR", then=F("salary") * 1.02),
                    When(department_name="Support", then=F("salary") * 10),
                    default=F("salary") * 1.01,
                    output_field=DecimalField(),
                )
            )
        self.stdout.write(self.style.SUCCESS("Successfully updated the records"))
