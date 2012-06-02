from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.core import serializers
from attendee.models import Event
class Command(BaseCommand):
 
    def handle(self, **kwargs):
        
        singleObject =  not True;
        obj = None
        queryset = None
        if singleObject:
            #obj = Entity.objects.get(id=4)
            pass
        else:
            queryset = Event.objects.all()
            pass
        
        # Save to file
        out = open("model_fixture.json", "w")
        json_serializer = serializers.get_serializer("json")()
        if singleObject:
            json_serializer.serialize([obj], stream=out, sort_keys=True, indent=4)
        else:
            items = []
            print "Total rows: %d " % len(queryset)
            for item in queryset:
                items.append(item)
            json_serializer.serialize(items, stream=out, sort_keys=True, indent=4)
        out.close()
