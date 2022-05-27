import tlhelp32

print("Process Walker\n")

with tlhelp32.ProcessSnapshot() as snapshot:
    for idx, process in enumerate(snapshot):
        print(f"Process #{idx}")
        print(
            "ID:              %s\n" % process.pid,
            "  Thread count:  %s\n" % process.num_threads,
            "  Parent PID:    %s\n" % process.parent,
            "  Base priority: %s\n" % process.priority,
            "  Name:          %s\n" % process.name,
            sep="",
        )
