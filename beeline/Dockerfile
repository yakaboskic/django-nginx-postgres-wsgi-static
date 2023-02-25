FROM python:3.9-alpine

# Upgrade pip
RUN pip install --upgrade pip

# Permissions and nonroot user for tighted security
RUN adduser -D nonroot
RUN mkdir /home/app/ && chown nonroot:nonroot /home/app
WORKDIR /home/app
USER nonroot

# Copy files to the container
COPY --chown=nonroot:nonroot . .

# Create a virtual
ENV VIRTUAL_ENV=/home/app/venv

# Python Setup
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip3 install -r requirements.txt --no-cache-dir

# Define the port number the container should expose
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
