FROM python
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir requests numpy beautifulsoup4 openpyxl
CMD ["python", "crypto.py"]