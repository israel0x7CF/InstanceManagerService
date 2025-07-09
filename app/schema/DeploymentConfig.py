from pydantic import BaseModel


class DeploymentConfig(BaseModel):
    host:str
    ssh_port:int=22
    hostname:str
    password:str
    mode:str
