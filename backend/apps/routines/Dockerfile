FROM python:3.9

# Set working directory
WORKDIR /code

# Install MkDocs and dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the application code
COPY . /code

# Expose the port that MkDocs will run on
EXPOSE 8000

# Command to run MkDocs
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]