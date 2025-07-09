from pydantic import BaseModel,Field,HttpUrl


class Instance(BaseModel):
    instanceCreationStatus:str | None
    adminUserName:str | None
    adminPassword: str | None
    instanceDbAddress:str | None
    instanceAddress: str | None
    status: str | None

class InstanceDetail(BaseModel):
    container_instance:str
    module_path:str
    host:str

class InstanceInformation(BaseModel):
    db_name: str = ""
    instanceName: str = ""
    instanceDbAddress: int = ""
    configurationFileLocation: str = ""
    instanceAddress: int = ""
    custom_addons_path: str = ""
    status: bool  = False
class CreateInstanceMsg(BaseModel):
    instanceName:str
    moduleName:str
    modulePath:str
    host:str | None = None

class InstanceCreationResponse(BaseModel):
    """
    Pydantic model for the response after a Docker container instance creation.
    """
    status: str = Field(..., description="Overall status of the instance creation (True for Active, False otherwise).")
    adminUserName: str = Field(..., description="Administrator username for the created Odoo instance.")
    adminPassword: str = Field(..., description="Administrator password for the created Odoo instance.")
    instanceDbAddress: HttpUrl = Field(..., description="URL for accessing the database of the Odoo instance (e.g., http://localhost:5432).")
    instanceAddress: HttpUrl = Field(..., description="URL for accessing the Odoo instance (e.g., http://localhost:8069).")
    instanceName: str = Field(..., description="The name of the created Docker instance.")
    instanceDbAddress: str = Field(..., description="The database port number of the Odoo instance.")
    configurationFileLocation: str = Field(..., description="Path to the Docker Compose configuration file.")
    instanceAddress: str = Field(..., description="The port number of the Odoo instance.")
    custom_addons_path: str = Field(..., description="The path to the custom addons directory for the instance.")

