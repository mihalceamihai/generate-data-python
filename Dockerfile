FROM python:3
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir schedule random2 requests
WORKDIR /usr/src/app
COPY ./generate_date.py .
CMD ["generate_date.py > server.log 2>&1"]
ENTRYPOINT ["python3"]
