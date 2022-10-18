from python:latest

run pip install --upgrade pip
run pip install --upgrade google-cloud-pubsub
run git clone https://github.com/gshilo/Generator.git
run chmod +x ./Generatorm/generator.py
run cp ./Generator/dataform-demo-365207-169853468c7b.json /tmp/dataform-demo-365207-169853468c7b.json
ENV GOOGLE_APPLICATION_CREDENTIALS=/tmp/dataform-demo-365207-169853468c7b.json

CMD python ./Generator/generator.py CTMX 1
