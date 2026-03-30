FROM python:3.11-alpine

RUN pip install --root-user-action=ignore --upgrade pip

RUN adduser -D appuser
USER appuser
WORKDIR /home/appuser

COPY --chown=appuser:appuser requirements.txt .

ENV PATH="/home/appuser/.local/bin:${PATH}"

RUN pip install --user -r requirements.txt


COPY --chown=appuser:appuser app.py .


ENTRYPOINT ["python"]
CMD ["app.py"]
