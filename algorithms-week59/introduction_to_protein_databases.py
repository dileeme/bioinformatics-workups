def biological_processes(go_annotations):
    return [term for aspect, term in go_annotations if aspect == "biological_process"]

go_annotations = [
    ("molecular_function", "ATP binding"),
    ("biological_process", "signal transduction"),
    ("cellular_component", "plasma membrane"),
    ("biological_process", "cell surface receptor signaling pathway"),
    ("molecular_function", "receptor activity"),
    ("biological_process", "positive regulation of cell population proliferation"),
]

for process in biological_processes(go_annotations):
    print(process)
