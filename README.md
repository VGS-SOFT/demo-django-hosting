# 🚀 Demo Django Hosting

<div align="center">
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/Deployed-Success-brightgreen?style=for-the-badge" alt="Deployed">
</div>

<p align="center">
  <strong>A modern Django web application showcasing best practices for deployment and hosting</strong>
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

This project demonstrates a production-ready Django application with modern hosting configurations. It's designed to serve as a template for deploying Django applications with industry-standard practices.

## ✨ Features

- ⚡ **Fast & Scalable** - Optimized for performance
- 🔒 **Secure** - Implements Django security best practices
- 🎨 **Modern UI** - Clean and responsive design
- 📱 **Mobile Friendly** - Works seamlessly on all devices
- 🔧 **Easy Configuration** - Environment-based settings
- 📊 **Database Support** - PostgreSQL, MySQL, SQLite
- 🚀 **CI/CD Ready** - Automated deployment pipelines

## 🛠️ Tech Stack

- **Backend:** Django 4.x
- **Database:** PostgreSQL / SQLite
- **Server:** Gunicorn / uWSGI
- **Web Server:** Nginx (recommended)
- **Static Files:** WhiteNoise / AWS S3
- **Python:** 3.8+

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (recommended)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/vrajvithalani/demo-django-hosting.git
   cd demo-django-hosting
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### Database Configuration

By default, the application uses SQLite for development. For production, configure PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🎯 Usage

### Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

### Production Server

```bash
gunicorn your_project.wsgi:application --bind 0.0.0.0:8000
```

### Running Tests

```bash
python manage.py test
```

## 🚀 Deployment

### Option 1: Traditional VPS (Ubuntu/Debian)

1. Set up a server with Nginx and Gunicorn
2. Configure SSL with Let's Encrypt
3. Use systemd for process management
4. Set up database backups

### Option 2: Platform-as-a-Service

Supported platforms:
- **Heroku** - Easy deployment with git push
- **Railway** - Modern hosting with automatic deployments
- **DigitalOcean App Platform** - Scalable and managed
- **AWS Elastic Beanstalk** - Enterprise-grade hosting

### Option 3: Docker

```bash
docker build -t demo-django-hosting .
docker run -p 8000:8000 demo-django-hosting
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/vrajvithalani">Vraj Vithalani</a></p>
  <p>
    <a href="https://github.com/vrajvithalani/demo-django-hosting/issues">Report Bug</a>
    ·
    <a href="https://github.com/vrajvithalani/demo-django-hosting/issues">Request Feature</a>
  </p>
</div>
