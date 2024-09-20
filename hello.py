import re
from pathlib import Path

from stringsext.core import Stringsext
from stringsext.encoding import EncodingName, UnicodeBlockFilter

UUID_PATTERN = r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"


def extract_uuids(content: str) -> list[str]:
    uuid_pattern = r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"
    return list(set(re.findall(uuid_pattern, content)))


def main():
    # Build the stringsext command
    extractor = Stringsext()
    findings = (
        extractor.encoding(EncodingName.UTF_16LE, 36)
        .encoding(EncodingName.UTF_16BE, 36)
        .encoding(EncodingName.UTF_8, 36)
        .encoding(EncodingName.BIG5, 36)
        .unicode_block_filter(UnicodeBlockFilter.ARABIC)
        .add_file(Path("example/test.bin"))
        .run(verbose=True)
        .parse()
    )

    for finding in findings:
        uuids = extract_uuids(finding.content)
        if uuids:
            for uuid in uuids:
                print(
                    f"Found UUID: {uuid}, encoding: {finding.encoding_info.name}, file: {finding.input_file}"
                )


if __name__ == "__main__":
    main()
