import asyncio
import os
from google.api_core.exceptions import DeadlineExceeded, ServiceUnavailable
from google.cloud import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

PROJECT_ID = os.getenv("PROJECT_ID")


async def update_data(key: str, new_key: str):
    db = firestore.AsyncClient(project=PROJECT_ID)

    contacts_ref = db.collection_group("Contacts")
    query = contacts_ref. \
        where(filter=FieldFilter("ct_type", "==", key))

    docs = query.stream()
    qty = 0

    await doc_runners(docs, new_key, qty)


async def doc_runners(docs, new_key, qty):
    async for doc in docs:
        qty += 1
        if qty % 100 == 0:
            print(f"updating {qty}")
            print(f"Updating doc {doc.id} => {doc.to_dict()}")
        doc.reference.update({"ct_type": new_key})


run = True
while run:
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            update_data("PHONE", "Telefone")
        )
        run = False
    except DeadlineExceeded:
        print("error but restarting again...")
        pass
    except ServiceUnavailable:
        print("error but restarting again...")
        pass
