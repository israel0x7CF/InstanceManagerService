from app.schema.DeploymentConfig import DeploymentConfig
import paramiko


class DeploymentEngine:
    def get_deployment_config(self,config:DeploymentConfig):
        if config.host == "local":
            pass
        pass

class RemoteDeploymentEngine:
    def __init__(self,username,password,host):
        self._host=host
        self._username=username
        self._password = password

    def __remote_client(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        client.connect(
            hostname=self._host,
            username=self._username,
            password=self._password,
            look_for_keys=False,
            allow_agent=False,
        )
        return client
    def create_container(self):
        pass


class LocalDeploymentEngine:
    pass
