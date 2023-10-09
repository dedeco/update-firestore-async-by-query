from google.cloud import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

PROJECT_ID = "sg1708-cad-centr-scbp-scug-dev"


def update_data(key: str, new_key: str):
    db = firestore.Client(project=PROJECT_ID)

    contacts_ref = db.collection_group("Contacts")

    query = contacts_ref. \
        where(
        filter=FieldFilter("ct_type", "==", key)
    )

    docs = query.stream()
    print('starting')
    qty = 0
    for doc in docs:
        qty += 1
        if qty % 100 == 0:
            print(f"updating {qty}")
            print(f"Updating doc {doc.id} => {doc.to_dict()}")

        doc.reference.update({"ct_type": new_key})

    print('end')


if __name__ == "__main__":
    #update_data("EMAIl", "E-mail")
    update_data("PHONE", "Telefone")
