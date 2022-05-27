import tlhelp32

print("Module Walker (32-bit modules included)\n")

with tlhelp32.ModuleSnapshot(include_32bit=True) as snapshot:
    for idx, module in enumerate(snapshot):
        print(f"Module #{idx}")
        print(
            "  Name:              %s\n" % module.name,
            "  Base address:      %s\n" % module.base_addr,
            "  File size (bytes): %s\n" % module.size,
            "  Path:              %s\n" % str(module.path),
            "  Handle:            %s\n" % module.handle,
            sep="",
        )
