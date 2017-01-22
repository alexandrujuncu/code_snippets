#!/usr/bin/env python3

from scapy.sendrecv import sniff
from scapy.layers import all as layers


def get_sources_from_capture(capture_interface, capture_filter,
                             capture_duration):
    sources = {}

    def process(pkt):
        if type(pkt) is layers.Ether:
            payload = pkt.payload
            if type(payload) is layers.IP or type(payload) is layers.IPv6:
                dst = payload.fields.get("dst")
                count = sources.get(dst, 0)
                sources[dst] = count + 1

    sniff(
        iface=capture_interface,
        filter=capture_filter,
        timeout=capture_duration * 60,
        prn=process)

    return [{"source": k, "count": v} for k, v in a.items()]


sources = get_sources_from_capture("wlp3s0", "tcp port 80", 1)
print(sources)
