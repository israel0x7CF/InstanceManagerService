from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.KafkaManager.listener import _handle_create_instance
from app.schema.instance import CreateInstanceMsg
from app.utils.kafka import start_kafka, stop_kafka
from app.utils.kafkaResponse.kafka_response import send_response


#register routes later


@asynccontextmanager
async def lifespan(app:FastAPI):
    await start_kafka()
    yield
    await  stop_kafka()

    #

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def test():
    print("test")
    return "test"

@app.get("/test")
async  def home():
    data = CreateInstanceMsg(
        instanceName="jeff",
        moduleName="jeff",
        modulePath="/opt/modules/login_user_detail",
        
    )
    _handle_create_instance(data)