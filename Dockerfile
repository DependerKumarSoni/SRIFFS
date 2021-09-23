FROM jupyter/base-notebook:python-3.7.6

COPY docker/docker-entrypoint.sh /home/
COPY requirements.txt /home/requirements.txt
RUN rm -rf /home/jovyan/work

RUN pip install -r /home/requirements.txt

ENTRYPOINT ["sh", "/home/docker-entrypoint.sh"]