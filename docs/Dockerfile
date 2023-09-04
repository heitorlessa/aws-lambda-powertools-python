# v9.1.18
FROM squidfunk/mkdocs-material@sha256:b90a7d9bce2d091e1b3c027c146a33108191a8f66f02ca42c95a0635dbe625ea
# pip-compile --generate-hashes --output-file=requirements.txt requirements.in
COPY requirements.txt /tmp/
RUN pip install --require-hashes -r /tmp/requirements.txt
