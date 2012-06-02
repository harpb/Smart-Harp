from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User as WebUser
from django.core import serializers
from articles.models import Attachment, Article
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
 
    def handle(self, **kwargs):
        
        singleObject =  True;
        related =  not True;
        #list_id = [31814,34537,331381,453651,134324,257037,109249,118444]
        obj = None
        queryset = None
        if singleObject:
#            obj = Attachment.objects.get(id = 1)
#            obj = Article.objects.get(id = 1)
            obj = WebUser.objects.get(id = 1)
        else:
            queryset = Attachment.objects.filter() 
        
        # Save to file
        out = open("auth_user.json", "w")
        json_serializer = serializers.get_serializer("json")()
        if singleObject:
            json_serializer.serialize([obj], stream=out, sort_keys=True, indent=4)
        else:
            items = []
            print "Total rows: %d " % len(queryset)
            for item in queryset:
                # If want to get related objects
                if related:
                    #app_id = item.id;
                    id = item.entity.id;
                    print "Related Obj. ID: %d" % id
                    try:
                        #item = ApplicationInfo.objects.get(application=app_id)
#                        item = Entity.objects.get(pk=id)
                        #print item.id
                        items.append(item)
                    except ObjectDoesNotExist:
                        pass
                else:
                    #item.user = AppsocialUser(id=1)
                    items.append(item)
            json_serializer.serialize(items, stream=out, sort_keys=True, indent=4)
        out.close()
