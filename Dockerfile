from python:latest

run pip install --upgrade google-cloud-pubsub
run git clone https://github.com/gshilo/dataform.git
run chmod +x ./dataform/generator.py
copy dataform-demo-365207-169853468c7b.json /tmp/dataform-demo-365207-169853468c7b.json
ENV GOOGLE_APPLICATION_CREDENTIALS=/tmp/dataform-demo-365207-169853468c7b.json

CMD python ./dataform/generator.py CTMX 1