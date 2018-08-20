1. docker build --rm -f Dockerfile.amd64.debug -t python-amd64-debug:latest .
2. docker run -d -p 4000:3000 --name python-test python-amd64-debug:latest