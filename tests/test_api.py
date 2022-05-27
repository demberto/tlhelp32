import tlhelp32


def test_heap_snapshot():
    with tlhelp32.HeapListSnapshot() as heaplist_snapshot:
        for heap in heaplist_snapshot:
            repr(heap)
            for block in heap:
                repr(block)


def test_module_snapshot():
    with tlhelp32.ModuleSnapshot(include_32bit=True) as module_snapshot:
        for module in module_snapshot:
            repr(module)


def test_process_snapshot():
    with tlhelp32.ProcessSnapshot() as process_snapshot:
        for process in process_snapshot:
            repr(process)


def test_thread_snapshot():
    with tlhelp32.ThreadSnapshot() as thread_snapshot:
        for thread in thread_snapshot:
            repr(thread)


def test_snapshot():
    with tlhelp32.Snapshot(include_32bit=True) as snapshot:
        repr(snapshot.heaps)
        repr(snapshot.modules)
        repr(snapshot.processes)
        repr(snapshot.threads)
