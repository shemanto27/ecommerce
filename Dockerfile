# Base image
FROM python:3.12-slim-bullseye

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1

# Install uv
RUN pip install uv

# Set the working directory
WORKDIR /app

# Copy only dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync

# adding venv's bin to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Collect static files
RUN uv run python manage.py collectstatic --noinput


# Start server (for dev)
CMD ["uv", "run", "gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]