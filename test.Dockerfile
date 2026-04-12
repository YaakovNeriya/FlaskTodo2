FROM python
WORKDIR /tests
COPY testserver.py .
RUN pip install requests
CMD ["python", "testserver.py"]