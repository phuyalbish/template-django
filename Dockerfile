FROM python:3.10.16-bookworm AS dev

ARG DJANGO_ENV 

ENV  \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.8.2 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    wget \
    default-libmysqlclient-dev \
    pkg-config \
 && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2-binary \
  && pip install poetry==${POETRY_VERSION} \
  && poetry --version



# For Development


WORKDIR /backend

COPY pyproject.toml poetry.lock ./

RUN poetry lock
RUN poetry install --no-root

CMD ["bash", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8081"]




# For Production


# RUN poetry lock
# RUN poetry install

# COPY . .


# RUN chmod +x /backend/build.sh



# CMD ["/bin/sh", "-c", "/backend/build.sh"]



# To run and build Directly without using docker-compose 


# To Build

# docker build -t prosthetics-backend-prod-image -f Dockerfile.production .

# To Run
# docker run -it --rm -e DJANGO_ENV=production  -p 8081:8081  --name prosthetics-backend-prod   prosthetics-backend-prod-image


# From env file
# docker run -it --rm --env-file .env  -p 8081:8081  --name prosthetics-backend-prod  prosthetics-backend-prod-image