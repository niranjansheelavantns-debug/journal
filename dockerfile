#use official python image
FROM python:3.12

#use working directory
WORKDIR /app

#copy all files to container
COPY fitness_app.py .

#command to run python file
CMD ["python","fitness_app.py"]