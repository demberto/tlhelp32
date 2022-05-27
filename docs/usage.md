# Usage

!!! caution "Context manager"
    Always use a `Snapshot` instance as a context manager, i.e. instantiating
    it via a `with` statement. If not close it explicitly with `close` after
    use.

## Traversing heaps

```python
import tlhelp32

with tlhelp32.HeapListSnapshot() as snapshot:
    for idx, heap in enumerate(snapshot):
        print(f"Heap #{idx}")
        print("  Heap ID:       %s\n" % heap.id_,
              "  Process ID:    %s\n" % heap.pid,
              sep="")
        for idx, block in enumerate(heap):
            print(f"  Block #{idx}")
            print("    Base address:    %s\n" % block.start_addr,
                  "    Size:            %s\n" % block.size,
                  "    Type:            %s\n" % block.kind.name,
                  "    Process ID:      %s\n" % block.pid,
                  "    Handle:          %s\n" % block.handle,
                  sep="")
```

## Traversing modules

```python
import tlhelp32

with tlhelp32.ModuleSnapshot(include_32bit=True) as snapshot:
    for idx, module in enumerate(snapshot):
        print(f"Module #{idx}")
        print("  Name:              %s\n" % module.name,
              "  Base address:      %s\n" % module.base_addr,
              "  File size (bytes): %s\n" % module.size,
              "  Path:              %s\n" % str(module.path),
              "  Handle:            %s\n" % module.handle,
              sep="")
```

## Traversing processes

```python
import tlhelp32

with tlhelp32.ProcessSnapshot() as snapshot:
    for idx, process in enumerate(snapshot):
        print(f"Process #{idx}")
        print("ID:              %s\n" % process.pid,
              "  Thread count:  %s\n" % process.num_threads,
              "  Parent PID:    %s\n" % process.parent,
              "  Base priority: %s\n" % process.priority,
              "  Name:          %s\n" % process.name,
              sep="")
```

## Traversing threads

```python
import tlhelp32

with tlhelp32.ThreadSnapshot() as snapshot:
    for idx, thread in enumerate(snapshot):
        print(f"Thread #{idx}")
        print("  ID:            %s\n" % thread.pid,
              "  Owner PID:     %s\n" % thread.owner,
              "  Base priority: %s\n" % thread.priority,
              sep="")
```
