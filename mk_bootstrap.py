# mk_bootstrap.py
import glob, struct, os, sys
SRC_DIR = "/home/makewalletfirst/.bitcoin/blocks"   # 원본 blk*.dat 위치
OUT     = "/home/makewalletfirst/bootstrap-e2c3a9fc.dat"
OLD = bytes.fromhex("f9beb4d9")
NEW = bytes.fromhex("e2c3a9fc")

files = sorted(glob.glob(os.path.join(SRC_DIR, "blk*.dat")))
assert files, "no blk files"
n=0
with open(OUT, "wb") as out:
    for p in files:
        d=open(p,"rb").read(); i=0; L=len(d)
        while True:
            j=d.find(OLD,i)
            if j<0 or j+8>L: break
            (blen,)=struct.unpack_from("<I",d,j+4)
            k=j+8+blen
            if k>L: break
            out.write(NEW); out.write(struct.pack("<I",blen)); out.write(d[j+8:k])
            n+=1; i=k
print("wrote", n, "blocks to", OUT)

