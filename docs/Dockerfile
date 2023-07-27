# v9.1.18
FROM squidfunk/mkdocs-material@sha256:dbd9dae1cff145c421536522bf01bf6b0f32b560fe7dab7d6eeedb015ff60890
# pip-compile --generate-hashes --output-file=requirements.txt requirements.in
COPY requirements.txt /tmp/
RUN pip install --require-hashes -r /tmp/requirements.txt
