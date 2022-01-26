FROM pypy:3.8-7.3

WORKDIR /code

COPY requirements.txt ./
RUN pypy -m pip install --no-cache-dir -r requirements.txt

COPY . .
