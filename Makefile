run:
	docker run -it --rm --name newspaper -p 5000:5000 vikings/newspaper
build:
	docker build -t vikings/newspaper .
release: build
	docker push vikings/newspaper