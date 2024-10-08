#!/bin/bash
####################################################################
#AUTHOR : FAREED SAYED
#DATE : 22 SEPTEMBER 2024
#DESCRIPTION : ALL THE NECCESARY COMMAND LINE FOR THIS PROJECT
####################################################################


# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Update and upgrade system packages
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install Python, pip, and virtual environment
if command_exists python3 && command_exists pip3; then
    echo "Python and pip are already installed."
else
    echo "Installing Python, pip, and virtual environment..."
    sudo apt install python3 python3-pip python3-venv -y
fi

# Install SQLite3
if command_exists sqlite3; then
    echo "SQLite3 is already installed."
else
    echo "Installing SQLite3..."
    sudo apt install sqlite3 -y
fi

# Install Node.js and npm
if command_exists node && command_exists npm; then
    echo "Node.js and npm are already installed."
else
    echo "Installing Node.js and npm..."
    sudo apt install nodejs npm -y
fi

# Ask user if they want to install PostgreSQL and set up a database
echo "Do you want to install PostgreSQL and set up a database? (y/n)"
read install_postgres
if [ "$install_postgres" == "y" ]; then
    if command_exists psql; then
        echo "PostgreSQL is already installed."
    else
        echo "Installing PostgreSQL and required libraries..."
        sudo apt install postgresql postgresql-contrib libpq-dev -y

        # Create PostgreSQL user and database (optional)
        echo "Do you want to create a PostgreSQL user and database? (y/n)"
        read create_postgres_db
        if [ "$create_postgres_db" == "y" ]; then
            echo "Enter PostgreSQL username:"
            read postgres_user
            echo "Enter PostgreSQL database name:"
            read postgres_db

            sudo -u postgres psql -c "CREATE USER $postgres_user WITH PASSWORD 'password';"
            sudo -u postgres psql -c "CREATE DATABASE $postgres_db;"
            sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $postgres_db TO $postgres_user;"
        fi
    fi
fi

# Ask user if they want to install Docker and Docker Compose
echo "Do you want to install Docker and Docker Compose? (y/n)"
read install_docker
if [ "$install_docker" == "y" ]; then
    if command_exists docker; then
        echo "Docker is already installed."
    else
        echo "Installing Docker and Docker Compose..."
        sudo apt install docker.io docker-compose -y
    fi
fi

# Install WeasyPrint dependencies for PDF generation
echo "Installing WeasyPrint dependencies..."
sudo apt install libpango-1.0-0 libgdk-pixbuf2.0-dev libffi-dev libcairo2 -y


# Installation complete
echo "Installation complete!"


