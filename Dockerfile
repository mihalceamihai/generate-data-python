FROM python:3
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir schedule random2 requests
WORKDIR /usr/src/app
COPY ./generate_date.py .
CMD ["generate_date.py"]
ENTRYPOINT ["python3"]
#CMD ["/bin/sh", "-c", "python3 index.py > server.log 2>&1"]
