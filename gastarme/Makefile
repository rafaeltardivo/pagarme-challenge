build:
	docker-compose build --no-cache

up:
	docker-compose up
	docker-compose restart 

up-detached:
	docker-compose up -d
	docker-compose restart gastarme

migrate:
	docker-compose exec gastarme su -c "python manage.py migrate"

test:
	docker-compose exec gastarme su -c "coverage run --source ./ ./manage.py test authentications billings commons gastarme purchases users wallets && coverage report"

destroy:
	docker-compose down