import tlhelp32

print("Thread Walker\n")

with tlhelp32.ThreadSnapshot() as snapshot:
    for idx, thread in enumerate(snapshot):
        print(f"Thread #{idx}")
        print(
            "  ID:            %s\n" % thread.pid,
            "  Owner PID:     %s\n" % thread.owner,
            "  Base priority: %s\n" % thread.priority,
            sep="",
        )
