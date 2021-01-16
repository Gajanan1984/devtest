how to build and run container
copy whole folder in docker host machine 
run following command

docker build . -t test-image
docker run -it --name test-container test-image
