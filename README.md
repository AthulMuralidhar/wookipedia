## To get things started

Make sure that you have:
- `docker` setup in your local machine
- `docker-compose` setup in your local machine

then you can start the containers using: `docker-compose up`
## kafka
- create three topics called country city and continent and added it to the init command in the docker file
## References
- the docker scaffolding is directly from [docker docs](https://docs.docker.com/compose/django/)
- the kafka part was soueced from:
 - https://medium.com/big-data-engineering/hello-kafka-world-the-complete-guide-to-kafka-with-docker-and-python-f788e2588cfc
 - https://github.com/wurstmeister/kafka-docker