import re

hex = ''

with open("result.txt") as f:
    for line in f:
        if re.search("Watermark Detected", line):
            match = re.search("WM=(.*)]", line)
            hex += match.group(1)

result = bytes.fromhex(hex).decode('utf-8')
print(result)