# Step 1: Use an official Python runtime as a parent image
# We use the slim-buster version for a smaller image size
FROM python:3.11-slim-buster

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container at /app
COPY ./requirements.txt /app/requirements.txt

# Step 4: Install any needed packages specified in requirements.txt
# --no-cache-dir reduces image size, --upgrade pip ensures we have the latest pip
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the application code into the container
COPY ./app /app/app

# Step 6: Expose the port the app runs on
EXPOSE 8000

# Step 7: Define the command to run your app using uvicorn
# This is the command that will be executed when the container starts
# We use 0.0.0.0 to make it accessible from outside the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]