FROM pypy:3

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install requests
RUN python3 -m pip install jsonpath


COPY apiDevtest ./
COPY CreateUser.json ./


CMD [ "python3", "api_Test.py"]

