import ssdp
s = ssdp.SSDP(target="positive")
p = s.run(10, "QR")
