import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """
    Simple WebSocket consumer that echoes messages back to the client.
    In production, you'd broadcast to a group/room.
    """

    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()
        
        # Send welcome message
        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected to the WebSocket!'
        }))

    async def disconnect(self, close_code):
        # Clean up when connection closes
        pass

    async def receive(self, text_data):
        """
        Receive message from WebSocket and echo it back
        """
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', '')

            # Echo the message back to the client
            await self.send(text_data=json.dumps({
                'type': 'chat_message',
                'message': f'Echo: {message}',
                'original': message
            }))
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid JSON format'
            }))


class NotificationConsumer(AsyncWebsocketConsumer):
    """
    Example of a broadcast consumer using channel groups.
    All connected clients receive the same notifications.
    """

    async def connect(self):
        self.room_group_name = 'notifications'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Send welcome message
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': 'Connected to notification channel!'
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Broadcast message to all connected clients
        """
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', '')

            # Send message to room group (broadcast to all)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'notification_message',
                    'message': message
                }
            )
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid JSON format'
            }))

    async def notification_message(self, event):
        """
        Receive message from room group and send to WebSocket
        """
        message = event['message']

        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': message
        }))
