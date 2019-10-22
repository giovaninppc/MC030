FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY server_python/app /app

RUN pip install -r /app/requirements.txt

COPY downloader /app/downloader

COPY video /app/video

COPY image /app/image

COPY neural /app/neural

COPY out /app/out