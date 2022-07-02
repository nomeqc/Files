import re

'''
item example：
"category": "zip",
"content_hash": "A4E1E3811603A86637470E87FD570BEF45EE8851",
"created_at": "2021-11-05T10:23:35.352Z",
"drive_id": "2389069",
"file_extension": "7z",
"file_id": "618506274dc70de9af884a95a270f47b4c56dc6f",
"mime_type": "application/x-7z-compressed",
"name": "TinyPNG.JPG.2.5.0.Ph.7z",
"parent_file_id": "618505f6c6eee5280a844a67b5f04d992e072c64",
"size": 3711869,
"starred": false,
"type": "file",
"updated_at": "2021-11-05T10:23:39.933Z",
"url": "https://bj29.cn-beijing.data.alicloudccp.com/K9oLSqY6%2F2389069%2F618506274dc70de9af884a95a270f47b4c56dc6f%2F61850627b091ff2c930b4e3b982ef54a4cd7055e?di=bj29\u0026dr=2389069\u0026f=618506274dc70de9af884a95a270f47b4c56dc6f\u0026u=27fad97991e046e4b9431eff0831cd3f\u0026x-oss-access-key-id=LTAIsE5mAn2F493Q\u0026x-oss-additional-headers=referer\u0026x-oss-expires=1650016804\u0026x-oss-signature=t4ygJsBC%2BtQne0Uf49ea7%2Fhqk8id6TZLgSXRQaudlsc%3D\u0026x-oss-signature-version=OSS2",
"user_meta": "{\"client\":\"desktop\"}"
'''
def filter_func(item: dict):
    type = item.get('type')
    ext = item.get('file_extension')
    if type != 'file' or ext != 'wma':
        return False
    name = item.get('name', '')
    result = re.search(r'(\d+)', name)
    ep_number = int(result.group(1)) if result else -1
    return ep_number >= 120
