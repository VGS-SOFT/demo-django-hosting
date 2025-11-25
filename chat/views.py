from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


class HealthCheckView(APIView):
    """
    Simple health check endpoint for monitoring
    """
    def get(self, request):
        return Response({
            'status': 'healthy',
            'message': 'Django DRF + Channels + Redis is running!',
            'debug_mode': settings.DEBUG,
            'websocket_endpoints': [
                'ws://localhost:8000/ws/chat/',
                'ws://localhost:8000/ws/notifications/'
            ]
        }, status=status.HTTP_200_OK)


class WebSocketTestView(APIView):
    """
    Returns HTML page for testing WebSocket connections
    """
    def get(self, request):
        html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        .container {
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        input, button {
            padding: 10px;
            margin: 5px;
        }
        #messages {
            height: 300px;
            overflow-y: auto;
            border: 1px solid #ccc;
            padding: 10px;
            background: #f9f9f9;
        }
        .message {
            margin: 5px 0;
            padding: 5px;
            background: white;
            border-left: 3px solid #007bff;
        }
    </style>
</head>
<body>
    <h1>WebSocket Test Page</h1>
    
    <div class="container">
        <h2>Echo Chat (ws://localhost:8000/ws/chat/)</h2>
        <button onclick="connectChat()">Connect</button>
        <button onclick="disconnectChat()">Disconnect</button>
        <br>
        <input type="text" id="chatMessage" placeholder="Type message...">
        <button onclick="sendChatMessage()">Send</button>
        <div id="messages"></div>
    </div>

    <script>
        let chatSocket = null;

        function connectChat() {
            chatSocket = new WebSocket('ws://localhost:8000/ws/chat/');
            
            chatSocket.onopen = function(e) {
                addMessage('Connected to chat!');
            };
            
            chatSocket.onmessage = function(e) {
                const data = JSON.parse(e.data);
                addMessage('Received: ' + JSON.stringify(data));
            };
            
            chatSocket.onclose = function(e) {
                addMessage('Chat disconnected');
            };
            
            chatSocket.onerror = function(e) {
                addMessage('Error occurred');
            };
        }

        function disconnectChat() {
            if (chatSocket) {
                chatSocket.close();
            }
        }

        function sendChatMessage() {
            const messageInput = document.getElementById('chatMessage');
            const message = messageInput.value;
            
            if (chatSocket && message) {
                chatSocket.send(JSON.stringify({
                    'message': message
                }));
                messageInput.value = '';
            }
        }

        function addMessage(message) {
            const messagesDiv = document.getElementById('messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message';
            messageDiv.textContent = message;
            messagesDiv.appendChild(messageDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }

        // Allow Enter key to send message
        document.getElementById('chatMessage').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendChatMessage();
            }
        });
    </script>
</body>
</html>
        """
        from django.http import HttpResponse
        return HttpResponse(html_content, content_type='text/html')
