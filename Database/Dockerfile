# Use an official MySQL 8.0 image as the base image
FROM mysql:8.0

# Set environment variables for MySQL configuration
ENV MYSQL_ROOT_PASSWORD=password


# Copy the SQL script to initialize the database
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port
EXPOSE 3306