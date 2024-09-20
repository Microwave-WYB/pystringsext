import os
import uuid


def generate_binary_file(filename, size=1024):
    # Generate two random UUIDs

    # Convert UUIDs to strings and encode them
    uuid1 = str(uuid.uuid4()).encode("big5")
    uuid2 = str(uuid.uuid4()).encode("utf-16le")
    uuid3 = str(uuid.uuid4()).encode("utf-8")
    uuid4 = str(uuid.uuid4()).encode("utf-16be")

    # Calculate the size of our UUIDs
    uuid_size = len(uuid1) + len(uuid2) + len(uuid3) + len(uuid4)

    # Generate random bytes for the rest of the file
    random_bytes = os.urandom(size - uuid_size)

    # Combine everything into a single bytes object
    file_content = (
        random_bytes[:100]  # Some random bytes at the start
        + uuid1
        + random_bytes[100:200]  # More random bytes
        + uuid2
        + random_bytes[200:300]  # More random bytes
        + uuid3
        + random_bytes[300:400]  # More random bytes
        + uuid4
        + random_bytes[400:]  # Remaining random bytes
    )

    # Write the content to the file
    with open(filename, "wb") as f:
        f.write(file_content)

    print(f"File '{filename}' created successfully.")


# Usage
generate_binary_file("example/test.bin", size=2048)
