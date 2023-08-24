#DOCKER
    # build dicker
    docker build --build-arg SECRET_KEY=${SECRET_KEY} --build-arg DB_NAME=${DB_NAME} --build-arg DB_USER=${DB_USER} --build-arg DB_PASSWORD=${DB_PASSWORD} --build-arg DB_HOST=${DB_HOST} --build-arg DB
    _PORT=${DB_PORT} -t mycoffee . --no-cache

    # run docker
    docker run -p 8000:8000 --name mycoffee-container mycoffee

#DOCKER-COMPOSE
    docker-compose up