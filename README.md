# **Celery Test**
# Usage
docker run -d -p 5672:5672 rabbitmq
pip install -r requirements.txt

#Commands for celery
celery -A proj worker -Q logic_operation0 -l INFO --hostname=worker1@localhost
celery -A proj worker -Q logic_operation1 -l INFO --hostname=worker1@localhost

#Commands for shell
python3
from proj.transaction import MyClass
for i in range(0,50):
    MyClass.make_transaction()