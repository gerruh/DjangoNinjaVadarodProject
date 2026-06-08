#!/bin/bash
# entrypoint.sh

set -e

echo "=== Запуск приложения ==="

# Ожидание PostgreSQL
if [ -n "$DATABASE_URL" ] || [ -n "$POSTGRES_HOST" ]; then
    echo "Ожидание PostgreSQL..."
    while ! nc -z db 5432; do
        sleep 0.5
    done
    echo "PostgreSQL доступен"
fi

# Ожидание Redis (если используется)
if [ -n "$REDIS_URL" ] || [ -n "$CELERY_BROKER_URL" ]; then
    echo "Ожидание Redis..."
    while ! nc -z redis 6379; do
        sleep 0.5
    done
    echo "Redis доступен"
fi

# Применение миграций
echo "Применение миграций..."
python manage.py migrate --noinput

# Создание суперпользователя (только в dev)
if [ "$DEBUG" = "True" ]; then
    echo "Проверка суперпользователя..."
    python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    print('Создание суперпользователя...')
    User.objects.create_superuser('admin', 'admin@dnp.local', 'admin123')
else:
    print('Суперпользователь уже существует')
" || true
fi

# Запуск основной команды
echo "Запуск команды: $@"
exec "$@"