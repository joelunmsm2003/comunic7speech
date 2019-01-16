killall -9 python 
killall -9 node
python manage.py runserver 0.0.0.0:8000&
npm run build&
cd ../redis-5.0.2
src/redis-server&
