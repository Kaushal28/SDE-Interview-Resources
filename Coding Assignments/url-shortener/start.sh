# start the gunicorn server with uvicorn worker on port 80
echo "Starting gunicorn server..."
gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:80 -t 300 src.main:app