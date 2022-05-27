import tlhelp32

print("Heap Walker\n")

with tlhelp32.HeapListSnapshot() as snapshot:
    for idx, heap in enumerate(snapshot):
        print(f"Heap #{idx}")
        print(
            "  Heap ID:       %s\n" % heap.id_,
            "  Process ID:    %s\n" % heap.pid,
            sep="",
        )
        for idx, block in enumerate(heap):
            print(f"  Block #{idx}")
            print(
                "    Base address:    %s\n" % block.start_addr,
                "    Size:            %s\n" % block.size,
                "    Type:            %s\n" % block.kind.name,
                "    Process ID:      %s\n" % block.pid,
                "    Handle:          %s\n" % block.handle,
                sep="",
            )
