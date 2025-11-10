# ===== Stage 1: Builder =====
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app

# Install system dependencies for building Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .

# Upgrade pip and install Python dependencies with increased timeout
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --default-timeout=100 --ignore-installed -r requirements.txt

# Copy app code
COPY . .

# ===== Stage 2: Final runtime image =====
FROM python:3.11-slim

WORKDIR /app

# Install runtime system dependencies
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages and executables from builder
COPY --from=builder /usr/local /usr/local

# Copy app code
COPY --from=builder /app /app

# Expose Streamlit port
EXPOSE 8501
ENV STREAMLIT_SERVER_HEADLESS=true

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
