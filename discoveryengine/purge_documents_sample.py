# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# [START genappbuilder_purge_documents]
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine

# TODO(developer): Uncomment these variables before running the sample.
# project_id = "YOUR_PROJECT_ID"
# location = "YOUR_LOCATION"            # Values: "global", "us", "eu"
# data_store_id = "YOUR_DATA_STORE_ID"


def purge_documents_sample(
    project_id: str, location: str, data_store_id: str
) -> discoveryengine.PurgeDocumentsMetadata:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.DocumentServiceClient(client_options=client_options)

    operation = client.purge_documents(
        request=discoveryengine.PurgeDocumentsRequest(
            # The full resource name of the search engine branch.
            # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
            parent=client.branch_path(
                project=project_id,
                location=location,
                data_store=data_store_id,
                branch="default_branch",
            ),
            filter="*",
            # If force is set to `False`, return the expected purge count without deleting any documents.
            force=True,
        )
    )

    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()

    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.PurgeDocumentsMetadata(operation.metadata)

    # Handle the response
    print(response)
    print(metadata)

    return metadata


# [END genappbuilder_purge_documents]