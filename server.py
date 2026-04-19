import os
import logging
import tornado.ioloop
import tornado.web

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

APP_NAME = os.getenv("APP_NAME", "Python Docker App")
APP_COLOR = os.getenv("APP_COLOR", "#0d1117")
PORT = int(os.getenv("PORT", "8888"))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template.html", title=APP_NAME, bgcolor=APP_COLOR)
        logger.info("GET / — %s", self.request.remote_ip)


class HealthHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_status(200)
        self.write({"status": "ok", "app": APP_NAME})


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/health", HealthHandler),
        ],
        template_path=os.path.dirname(__file__),
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    logger.info("Servidor iniciado na porta %d", PORT)
    tornado.ioloop.IOLoop.current().start()
