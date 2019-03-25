FROM python:3.7.2
ENV IS_DOCKER 1
COPY . /home/setup
WORKDIR /home/setup/app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "build.py"]
