import json
import pathlib
path = pathlib.Path(__file__).parent.absolute()



with open(f'{path}/minio_config.json') as f:
    minio_config = json.load(f)

with open(f'{path}/pyorient.json') as f:
    pyorient_config = json.load(f)