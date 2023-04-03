FROM python:3.9.5

WORKDIR /app 

COPY ./requirements.txt ./ 

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . ./ 

EXPOSE 8000/tcp

RUN chmod +x /app/truck_in_career/entrypoint.sh

ENTRYPOINT ["/app/truck_in_career/entrypoint.sh"]