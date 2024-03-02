# Firestore Field Updater Script

### Purpose

This script provides a tool for updating specific field values within documents in a Google Cloud Firestore database. Its primary use case is to find documents where a designated field holds a certain value and replace that value with a new one. 

### Prerequisites

* A Google Cloud Project with a Firestore database.
* The following Python libraries installed: 
    * google-cloud-firestore
    * asyncio
* A "PROJECT_ID" environment variable set to your Google Cloud Project ID.

### Setup

1. Clone or download this code.
2. Make sure you have the necessary libraries installed:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your "PROJECT_ID" environment variable. You can do this in your terminal (replace with your actual project ID):
   ```bash
   export PROJECT_ID=your-project-id
   ```

### Usage

1. Run the Python script:
   ```bash
   python main.py  
   ```

### Functionality

* The script connects to your Firestore database.
* It searches for documents in "Contacts" collections where the "ct_type" field is set to "PHONE".
* The script updates the "ct_type" field to "Telefone" for all matching documents.
* Progress is reported to the console after every 100 documents are updated.
* The script includes error handling to retry the update operation in case of timeouts or temporary service unavailability. 

### Customization

You can modify the following parameters within the code:

* PROJECT_ID: Ensure this matches your Google Cloud Project ID.
* contacts_ref = db.collection_group("Contacts"): Change the collection group name if needed.
* The values passed into the update_data function (currently "PHONE" and "Telefone") control the target field and its updated value.

### Important Notes

* This script is designed to handle updates in batches. 
* For substantial datasets, consider increasing the batch size or adding pagination. 
        
