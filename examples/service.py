"""examples/service.py

This examples starts a separate :pypi:`mode` service with the app.

If you want the service instance to be generally available
you may create a subclass of app:

.. sourcecode:: python

    class App(faust.App):
        myservice: MyService

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            self.myservice = self.service(
                MyService(loop=self.loop, beacon=self.beacon),
            )

    app = App('service-example')
"""
import faust


app = faust.App('service-example')


@app.service
class MyService(faust.Service):

    async def on_start(self) -> None:
        self.log.info('STARTED')

    async def on_stop(self) -> None:
        self.log.info('STOPPED')



@app.agent(value_type=str)
async def consumer(stream):
    async for message in stream:
        print('Received: %r' % (message,))


@app.timer(1.0)
async def producer():
    await consumer.send('hello')




if __name__ == '__main__':
    app.main()