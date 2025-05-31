# Dockerfile

# 1\. Base Image: Use an official lightweight Python image.

# Using a specific version is good for reproducibility.

FROM python:3.13-slim-bookworm

# 1A\. Fixing some CVEs with updates

# This helps patch OS-level vulnerabilities and ensures pip is up-to-date.

RUN apt-get update && \
apt-get upgrade -y --no-install-recommends && \
pip install --no-cache-dir --upgrade pip && \
rm -rf /var/lib/apt/lists/\*

# 2\. Set Environment Variables (corrected format)

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3\. Set Working Directory: Define the working directory inside the container.

WORKDIR /app

# 4\. Install Dependencies:

# Copy the requirements file first (if you had one) to leverage Docker cache.

# For this simple bot, we only need discord.py. We can install it directly.

# If you had a requirements.txt, you would do:

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir discord.py

# 5\. Copy Application Code: Copy the bot script into the container.

COPY bot.py .

# 6\. Command to Run: Specify the command to run when the container starts.

# The DISCORD\_BOT\_TOKEN will be passed as an environment variable when running the container.

CMD ["python", "bot.py"]