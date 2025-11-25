# 🚀 Django DRF + Channels + Redis WebSocket Project

<div align="center">
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/DRF-red.svg?style=for-the-badge&logo=django&logoColor=white" alt="DRF">
  <img src="https://img.shields.io/badge/Channels-092E20?style=for-the-badge" alt="Channels">
  <img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white" alt="Redis">
  <img src="https://img.shields.io/badge/WebSockets-010101?style=for-the-badge" alt="WebSockets">
</div>

<p align="center">
  <strong>A production-ready Django REST Framework + WebSockets project using Django Channels and Redis</strong>
</p>

<p align="center">
  Learn how to deploy a real-time Django application with WebSocket support!
</p>

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#-tech-stack)
- [💻 Quick Start](#-quick-start)
  - [Local Development](#local-development)
  - [Docker Setup](#docker-setup)
- [🧪 Testing WebSockets](#-testing-websockets)
- [🔧 Project Structure](#-project-structure)
- [⚙️ Configuration](#-configuration)
- [🚀 Deployment Guide](#-deployment-guide)
  - [VPS Deployment](#1-vps-deployment-ubuntudebian)
  - [Railway Deployment](#2-railway-deployment)
  - [AWS Deployment](#3-aws-elastic-beanstalk)
- [💡 How It Works](#-how-it-works)
- [🔍 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)

---

## 🌟 Overview

This project is a **learning-focused** implementation of Django REST Framework with **real-time WebSocket** capabilities using **Django Channels** and **Redis** as the channel layer backend.

Perfect for:
- Learning Django Channels & WebSocket implementation
- Understanding ASGI vs WSGI deployment
- Hosting real-time applications in production
- Building chat apps, live notifications, real-time dashboards

## ✨ Features

- ⚡ **REST API** - Django REST Framework endpoints
- 🗣️ **WebSocket Support** - Real-time bi-directional communication
- 💬 **Echo Chat Consumer** - Simple message echoing demo
- 🔔 **Broadcast Notifications** - Group-based message broadcasting
- 🔄 **Redis Channel Layer** - Scalable message passing between consumers
- 🐳 **Docker Ready** - Complete Docker Compose setup
- 🎯 **Production Ready** - Environment-based configuration
- 📦 **Easy Deployment** - Multiple hosting options covered

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Web Framework** | Django 4.2 |
| **API** | Django REST Framework 3.14 |
| **WebSockets** | Django Channels 4.0 |
| **Channel Layer** | Redis 5.x + channels-redis |
| **ASGI Server** | Daphne 4.0 |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **Python** | 3.11+ |

---

## 💻 Quick Start

### Local Development

#### 1. Clone & Setup

```bash
# Clone repository
git clone https://github.com/vrajvithalani/demo-django-hosting.git
cd demo-django-hosting

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Configure Environment

```bash
# Copy environment file
cp .env.example .env

# Edit .env if needed (defaults work for local development)
```

#### 3. Install & Start Redis

**Option A: Using Docker (Recommended)**
```bash
docker run -d -p 6379:6379 redis:7-alpine
```

**Option B: Local Installation**
```bash
# macOS
brew install redis
brew services start redis

# Ubuntu/Debian
sudo apt update
sudo apt install redis-server
sudo systemctl start redis

# Verify Redis is running
redis-cli ping  # Should return "PONG"
```

#### 4. Run Migrations & Start Server

```bash
# Apply database migrations
python manage.py migrate

# Start Daphne (ASGI server)
daphne -b 0.0.0.0 -p 8000 config.asgi:application
```

#### 5. Access the Application

- **API Health Check**: http://localhost:8000/api/health/
- **WebSocket Test Page**: http://localhost:8000/api/ws-test/
- **Admin Panel**: http://localhost:8000/admin/ (create superuser first)

---

### Docker Setup

**Easiest way to run everything!**

```bash
# Build and start all services (Django + Redis)
docker-compose up --build

# Access application at http://localhost:8000
```

**Stop services:**
```bash
docker-compose down
```

---

## 🧪 Testing WebSockets

### Method 1: Built-in Test Page (Easiest)

1. Start the server (see Quick Start above)
2. Open browser: http://localhost:8000/api/ws-test/
3. Click **"Connect"** button
4. Type a message and click **"Send"**
5. Watch the echo response appear!

### Method 2: Browser Console

Open your browser's JavaScript console and run:

```javascript
// Connect to echo chat
const socket = new WebSocket('ws://localhost:8000/ws/chat/');

socket.onopen = () => console.log('Connected!');
socket.onmessage = (e) => console.log('Received:', JSON.parse(e.data));

// Send a message
socket.send(JSON.stringify({ message: 'Hello WebSocket!' }));
```

### Method 3: Python Test Script

```python
import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:8000/ws/chat/"
    async with websockets.connect(uri) as websocket:
        # Receive welcome message
        response = await websocket.recv()
        print(f"Connected: {response}")
        
        # Send test message
        await websocket.send(json.dumps({"message": "Hello from Python!"}))
        
        # Receive echo
        response = await websocket.recv()
        print(f"Echo: {response}")

asyncio.run(test_websocket())
```

### Available WebSocket Endpoints

| Endpoint | Purpose |
|----------|----------|
| `ws://localhost:8000/ws/chat/` | Echo chat - messages echoed back to sender |
| `ws://localhost:8000/ws/notifications/` | Broadcast - messages sent to all connected clients |

---

## 🔧 Project Structure

```
demo-django-hosting/
├── config/                 # Django project settings
│   ├── __init__.py
│   ├── settings.py        # Main settings (Channels, Redis, DRF)
│   ├── asgi.py            # ASGI config with WebSocket routing
│   ├── urls.py            # URL configuration
│   └── wsgi.py            # WSGI config (not used with Channels)
├── chat/                  # WebSocket app
│   ├── consumers.py       # WebSocket consumers (ChatConsumer, NotificationConsumer)
│   ├── routing.py         # WebSocket URL routing
│   ├── views.py           # DRF API views
│   └── urls.py            # HTTP URL patterns
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── Dockerfile             # Docker image definition
├── docker-compose.yml     # Multi-container setup (Django + Redis)
├── manage.py              # Django management script
└── README.md              # This file
```

---

## ⚙️ Configuration

### Environment Variables

Edit `.env` file:

```env
# Django
SECRET_KEY=your-secret-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Redis (Channel Layer)
REDIS_HOST=localhost     # Use 'redis' for Docker
REDIS_PORT=6379
```

### Key Settings Explained

**config/settings.py:**

```python
# Must be at the top of INSTALLED_APPS
INSTALLED_APPS = [
    'daphne',  # ASGI server
    'django.contrib.admin',
    # ... other apps
    'channels',
    'rest_framework',
    'chat',
]

# ASGI application (replaces WSGI for Channels)
ASGI_APPLICATION = 'config.asgi.application'

# Redis as channel layer backend
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [("localhost", 6379)],
        },
    },
}
```

---

## 🚀 Deployment Guide

### Prerequisites for All Platforms

- Redis server (managed or self-hosted)
- PostgreSQL database (recommended for production)
- ASGI-compatible server (Daphne, Uvicorn)

---

### 1. VPS Deployment (Ubuntu/Debian)

**Perfect for: Learning server administration, full control**

#### Step 1: Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python & dependencies
sudo apt install python3-pip python3-venv nginx redis-server postgresql postgresql-contrib -y

# Start Redis
sudo systemctl start redis
sudo systemctl enable redis
```

#### Step 2: Clone & Configure Project

```bash
# Clone repository
git clone https://github.com/vrajvithalani/demo-django-hosting.git
cd demo-django-hosting

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
nano .env  # Edit with production values
```

#### Step 3: Configure PostgreSQL

```bash
# Create database
sudo -u postgres psql
CREATE DATABASE django_channels_db;
CREATE USER django_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE django_channels_db TO django_user;
\q

# Update settings.py to use PostgreSQL
```

#### Step 4: Run Migrations & Collect Static

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

#### Step 5: Create Systemd Service

Create `/etc/systemd/system/daphne.service`:

```ini
[Unit]
Description=Daphne ASGI Server for Django Channels
After=network.target redis.service

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/demo-django-hosting
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/daphne -b 0.0.0.0 -p 8000 config.asgi:application

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl start daphne
sudo systemctl enable daphne
sudo systemctl status daphne
```

#### Step 6: Configure Nginx

Create `/etc/nginx/sites-available/django-channels`:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # HTTP requests
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # WebSocket requests
    location /ws/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Static files
    location /static/ {
        alias /path/to/demo-django-hosting/staticfiles/;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/django-channels /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 7: SSL with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com
```

**Update WebSocket URL to `wss://` in production!**

---

### 2. Railway Deployment

**Perfect for: Quick deployment, managed Redis**

#### Setup Steps:

1. **Create Railway Account**: https://railway.app
2. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   railway login
   ```

3. **Initialize Project**:
   ```bash
   railway init
   railway link
   ```

4. **Add Redis Service**:
   - Dashboard → New → Database → Redis
   - Copy connection URL

5. **Set Environment Variables**:
   ```bash
   railway variables set SECRET_KEY="your-secret-key"
   railway variables set DEBUG="False"
   railway variables set ALLOWED_HOSTS="your-app.railway.app"
   railway variables set REDIS_HOST="redis.railway.internal"
   ```

6. **Create Procfile**:
   ```
   web: daphne -b 0.0.0.0 -p $PORT config.asgi:application
   ```

7. **Deploy**:
   ```bash
   railway up
   ```

**Update WebSocket URLs to use your Railway domain!**

---

### 3. AWS Elastic Beanstalk

**Perfect for: Enterprise applications, AWS ecosystem**

1. **Install EB CLI**:
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB**:
   ```bash
   eb init -p python-3.11 django-channels-app
   ```

3. **Create Environment**:
   ```bash
   eb create django-channels-env
   ```

4. **Configure Redis**: Use AWS ElastiCache for Redis
5. **Set Environment Variables** in EB Console
6. **Deploy**:
   ```bash
   eb deploy
   ```

---

## 💡 How It Works

### ASGI vs WSGI

- **WSGI** (Traditional Django): Synchronous, HTTP only
- **ASGI** (Django Channels): Asynchronous, supports WebSockets, HTTP/2

### Architecture

```
Client (Browser)
    ↓ HTTP Request
    ↓ WebSocket Connection
Nginx (Reverse Proxy)
    ↓
Daphne (ASGI Server)
    ↓
Django Channels
    ├─ HTTP → Django Views (REST API)
    └─ WebSocket → Consumers
         ↓
    Redis (Channel Layer)
         ↓
    Inter-consumer communication
```

### WebSocket Flow

1. **Client connects** to `ws://domain.com/ws/chat/`
2. **Nginx forwards** to Daphne (upgrades to WebSocket)
3. **Daphne routes** to `ChatConsumer` via `routing.py`
4. **Consumer accepts** connection
5. **Messages exchanged** via `receive()` and `send()`
6. **Redis enables** multi-server broadcasting

---

## 🔍 Troubleshooting

### Redis Connection Failed

```bash
# Check Redis is running
redis-cli ping

# Check connection
redis-cli -h localhost -p 6379 ping

# Restart Redis
sudo systemctl restart redis
```

### WebSocket 403 Forbidden

- Check `ALLOWED_HOSTS` in settings.py
- Verify CORS settings if connecting from different domain
- Check Nginx WebSocket configuration

### WebSocket Closes Immediately

- Verify Redis is accessible from Django
- Check `CHANNEL_LAYERS` configuration
- Review Daphne logs: `journalctl -u daphne -f`

### "No module named 'channels'"

```bash
pip install -r requirements.txt
```

### Port 8000 Already in Use

```bash
# Kill process on port 8000
sudo lsof -t -i:8000 | xargs kill -9

# Or use different port
daphne -b 0.0.0.0 -p 8080 config.asgi:application
```

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📚 Resources

- [Django Channels Documentation](https://channels.readthedocs.io/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Redis Documentation](https://redis.io/documentation)
- [WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)

---

## 📝 License

MIT License - feel free to use for learning and production!

---

<div align="center">
  <p><strong>Built for learning Django Channels & WebSocket deployment</strong></p>
  <p>Made with ❤️ by <a href="https://github.com/vrajvithalani">Vraj Vithalani</a></p>
  <p>
    <a href="https://github.com/vrajvithalani/demo-django-hosting/issues">Report Bug</a>
    ·
    <a href="https://github.com/vrajvithalani/demo-django-hosting/issues">Request Feature</a>
    ·
    <a href="https://github.com/vrajvithalani/demo-django-hosting/discussions">Ask Question</a>
  </p>
</div>
