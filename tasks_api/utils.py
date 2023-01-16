import os
from fastapi_mail import FastMail, ConnectionConfig
from dotenv import load_dotenv

load_dotenv('.env')


class Envs:
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_FROM = os.getenv('MAIL_FROM')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_FROM_NAME = os.getenv('MAIL_FROM_NAME')


class MailConfig:

    @staticmethod
    def connection_config():
        """
        :return: connection config object.
        """
        return ConnectionConfig(
            MAIL_USERNAME=Envs.MAIL_USERNAME,
            MAIL_PASSWORD=Envs.MAIL_PASSWORD,
            MAIL_FROM=Envs.MAIL_FROM,
            MAIL_PORT=Envs.MAIL_PORT,
            MAIL_SERVER=Envs.MAIL_SERVER,
            MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
            MAIL_TLS=True,
            MAIL_SSL=False,
            USE_CREDENTIALS=True,
            VALIDATE_CERTS=True,
            TEMPLATE_FOLDER="./templates/email"
        )


class Mail:

    @staticmethod
    async def send_mail(msg_schema, mail_conf, template_name):
        """
        mail send functionality.
        :param msg_schema: msg schema
        :param mail_conf: mail conf
        :param template_name: template name
        :return:send the mail
        """
        fm = FastMail(mail_conf)
        await fm.send_message(msg_schema, template_name=template_name)

