#!/usr/bin/env python
"""Simple STUN client for getting external IP address.
Based on stun.py from https://github.com/myers/html5_udp_to_server,
but heavily simplified (dropped Twisted dependency, only supports old RFC 3489)
"""

import os, socket, struct, math

BINDING_REQUEST = 0x0001
BINDING_RESPONSE = 0x0101
MAPPED_ADDRESS = 0x0001
FAMILY_IPV4 = 0x01

STUN_SERVERS = [
    ("stun.l.google.com", 19302),
    ("stun1.l.google.com", 19302),
    ("stun2.l.google.com", 19302),
    ("stun3.l.google.com", 19302),
    ("stun4.l.google.com", 19302),
    ("stun.iptel.org", 3478)
]


class StunClient(object):
    """Simple STUN client for getting external IP address"""
    def __init__(self, timeout=5, attempts=3):
        self._timeout = timeout
        self._attempts = attempts
        self._transaction_id = b""

    def get_ip(self, stun_host="", stun_port=3478, source_address="", source_port=54320):
        """Get external IP address and port"""
        if stun_host:
            stun_servers = [(stun_host, stun_port)]
        else:
            stun_servers = STUN_SERVERS

        # If no stun_host is specified, try more servers from STUN_SERVERS list
        # (max. number of attempted servers is specified by self._attempts)
        ext_address = ""
        ext_port = 0
        attempt = 0
        for stun_host, stun_port in stun_servers:
            attempt += 1
            if attempt > self._attempts:
                break

            try:
                # Create socket, send request and receive response
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(self._timeout)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.bind((source_address, source_port))
                sock.sendto(self._generate_request(), (stun_host, stun_port))
                data, addr = sock.recvfrom(2048)
                sock.close()

                # Parse response
                ext_address, ext_port = self._parse_response(data)
                if ext_address:
                    break
            except:
                continue

        if not ext_address:
            raise RuntimeError("Couldn't get external IP address from STUN server!")

        return (ext_address, ext_port)

    def _generate_id(self):
        """Generate random Transaction ID"""
        return os.urandom(16)

    def _generate_request(self):
        """Generate Binding Request"""
        self._transaction_id = self._generate_id()
        request = [struct.pack(">H", BINDING_REQUEST),  # Message Type
                   struct.pack(">H", 0),                # Message Length
                   self._transaction_id]
        return b"".join(request)

    def _parse_response(self, data):
        """Parse server response to get mapped address"""
        packet_type, length = struct.unpack(">2H", data[:4])
        if packet_type != BINDING_RESPONSE:
            raise ValueError("Invalid response type!")
        if data[4:20] != self._transaction_id:
            raise ValueError("Invalid response transaction ID!")

        # Walk through all response attributes to find MAPPED_ADDRESS
        for attr_id, value_length, value, start_offset in self._parse_attributes(data[20:length + 20]):
            if attr_id == MAPPED_ADDRESS:
                ip_address, port = self._parse_mapped_address(value)
                break

        return (ip_address, port)

    def _parse_attributes(self, data):
        """Generator which walks through response attributes"""
        ptr = 0
        while ptr < len(data):
            attr_type, length = struct.unpack(">2H", data[ptr:ptr + 4])
            yield attr_type, length, data[ptr + 4:ptr + 4 + length], ptr + 20
            attr_length = 4 + 4 * int(math.ceil(length / 4.0))
            ptr += attr_length

    def _parse_mapped_address(self, value):
        """Get IP address and port from MAPPED_ADDRESS attribute"""
        family, recv_port = struct.unpack(">xBH", value[:4])
        if family != FAMILY_IPV4:
            raise ValueError("IPv6 is not supported!")
        ip_address = socket.inet_ntoa(value[4:])
        return (ip_address, recv_port)


if __name__ == "__main__":
    stun = StunClient()
    ext_address, ext_port = stun.get_ip()
    print("External IP: {}".format(ext_address))
    print("External port: {}".format(ext_port))
