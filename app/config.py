# ==========================================
# WHAT IS THIS FILE?
# ------------------------------------------
# This file loads configuration values
# from the .env file.
#
# Examples:
# - Database Host
# - Database Port
# - Database Username
# - Database Password
# - Database Name
#
# WHY DO WE NEED IT?
# ------------------------------------------
# Instead of hardcoding values in many files,
# we keep them in one place.
#
# If the database password changes,
# we only update the .env file.
# ==========================================

# Load environment variables from the .env file
from dotenv import load_dotenv

# Used to access environment variables
import os

# Read the .env file
load_dotenv()

# ==========================
# DATABASE CONFIGURATION
# ==========================

# Database Host
DB_HOST = os.getenv("DB_HOST")

# Database Port
DB_PORT = os.getenv("DB_PORT")

# Database Username
DB_USER = os.getenv("DB_USER")

# Database Password
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Database Name
DB_NAME = os.getenv("DB_NAME")