from django.dispatch import receiver
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
import channels
from channels.layers import get_channel_layer
from datetime import datetime
import time
import random

from channels.generic.websocket import JsonWebsocketConsumer

from .models import Vehicle, VehicleEntry
from .serializers import VehicleEntrySerializer

def send_message(instance):
    channel_layer = get_channel_layer()
    group_name = 'entry'
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'entry_message',
            'data': VehicleEntrySerializer(instance, many=False).data
        }
    )
    print('Message sent')


@receiver(post_save, sender=VehicleEntry)
def entry_post_save(sender, instance, **kwargs):
    send_message(instance)


class VehicleStatusConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.group_name = 'entry'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
        # entries = VehicleEntry.objects.all().order_by('-time_entry')
        # serializer = VehicleEntrySerializer(entries, many=True)
        # self.send_json({
        #     'entries': serializer.data
        # })

    def disconnect(self, close_code):
        pass

    def get_response(self, request, event_type):
        return {}

    def receive_json(self, request):
        self.send_json({"msg": "received"})

    def entry_message(self, event):
        self.send_json({
            "type": event['type'],
            'data': event['data']
        })
