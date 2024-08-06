source myvenv/bin/activate &&\
	./manage.py migrate &&\
	./manage.py collectstatic --no-input &&\
	sudo cp -r static /var/www/piggy &&\
	sudo chown -R www-data:www-data /var/www/piggy