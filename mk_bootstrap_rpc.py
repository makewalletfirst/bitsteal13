#!/usr/bin/env python3
import json, subprocess, struct, sys

BITCOIND_CLI = "./src/bitcoin-cli"
DATADIR = "/home/makewalletfirst/.bitcoin"  # 원본(메인넷 매직) datadir
RPCUSER = "user"
RPCPASS = "pass"
OUT = "/home/makewalletfirst/bootstrap-e2c3a9fc.dat"

NEW_MAGIC = bytes.fromhex("e2c3a9fc")

def cli(*args):
    cmd = [BITCOIND_CLI, f"-datadir={DATADIR}", f"-rpcuser={RPCUSER}", f"-rpcpassword={RPCPASS}"] + list(args)
    out = subprocess.check_output(cmd)
    return out.decode().strip()

def main():
    height = int(cli("getblockcount"))
    print("tip height:", height)
    n_written = 0
    with open(OUT, "wb") as f:
        for h in range(0, height + 1):
            bh = cli("getblockhash", str(h))
            # verbosity=0 → raw block hex
            rawhex = cli("getblock", bh, "0")
            raw = bytes.fromhex(rawhex)
            # 레코드: magic(4) + length(4) + payload
            f.write(NEW_MAGIC)
            f.write(struct.pack("<I", len(raw)))
            f.write(raw)
            n_written += 1
            if n_written % 500 == 0:
                print("written", n_written)
    print("done. total blocks:", n_written, "->", OUT)

if __name__ == "__main__":
    main()

