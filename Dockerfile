FROM python:alpine as builder

WORKDIR /app

COPY . /app

RUN pip install jinja2

RUN cd scripts && python generate.py

# ------

FROM nginx:alpine

COPY --from=builder /app/index.html /usr/share/nginx/html

COPY --from=builder /app/assets /usr/share/nginx/html/assets

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

