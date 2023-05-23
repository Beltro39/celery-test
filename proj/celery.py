from celery import Celery

app = Celery('proj',
             broker='pyamqp://',
             backend='rpc://',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.config_from_object('proj.celeryconfig')
app.conf.update(
    task_routes = {
        'proj.tasks.add': {'queue': 'hipri'},
    },
)

if __name__ == '__main__':
    app.start()