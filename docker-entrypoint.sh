# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Create database migrations
echo "Create database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate