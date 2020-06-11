import base64
from itertools import cycle

message = 'ShJDQFNVXF0eS1MLFRdSQlNYWkpAUxZWX1lcU1hJGAlUEQ8QElVFTUsIARZVEhwVF1NfSAIeB0IS EA8QEVBADh4WVVxSWVURFQ5KDRBZXFVDVVtcQBlLUwsVF0BeWlZNBgkXFhkQEkJXW0wEGAAWFQoV F0VYSAhLXxESVlpfERkUTUsEWFsREk0='


key = bytes('1505069.mls', "utf8")

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))