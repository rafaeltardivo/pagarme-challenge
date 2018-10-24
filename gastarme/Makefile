build:
	docker-compose build --no-cache

up-detached:
	docker-compose up -d
	docker-compose restart gastarme

migrate:
	docker-compose exec gastarme su -c "python manage.py migrate"

superuser:
	docker-compose exec gastarme su -c "python manage.py createsuperuser"

test:
	docker-compose exec gastarme su -c "coverage run --source ./ ./manage.py test authentications billings commons gastarme purchases users wallets && coverage report"

destroy:
	docker-compose down -v