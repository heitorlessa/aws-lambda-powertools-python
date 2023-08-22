# v9.1.18
FROM squidfunk/mkdocs-material@sha256:db16d8c9433c94ee20c0310c2758952f3110d69c99fa61de8cb1b583badce8cc
# pip-compile --generate-hashes --output-file=requirements.txt requirements.in
COPY requirements.txt /tmp/
RUN pip install --require-hashes -r /tmp/requirements.txt
